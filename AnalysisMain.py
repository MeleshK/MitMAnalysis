#!/usr/bin/python3

# import whois
import AndroidDataPrivacy.AppFinder as AppFinder
import AndroidDataPrivacy.Applications.AndroidNative as AndroidNative
import AndroidDataPrivacy.Applications.AppDefault as AppDefault
import AndroidDataPrivacy.Applications.FDroid as FDroid
import AndroidDataPrivacy.Applications.GSuite as GSuite
import AndroidDataPrivacy.Applications.Session as Session
import AndroidDataPrivacy.Applications.Signal as Signal
import AndroidDataPrivacy.Applications.Telegram as Telegram
import AndroidDataPrivacy.Applications.WhatsApp as WhatsApp
import AndroidDataPrivacy.Applications.Wire as Wire
import AndroidDataPrivacy.Applications.Youtube as YouTube
import AndroidDataPrivacy.Flow as AnalysisFlow
import AndroidDataPrivacy.RawDataSearch as RawDataSearch
# import AndroidDataPrivacy.Result as Result
import AndroidDataPrivacy.syslog_client as syslog_client
from mitmproxy.io import FlowReader
# import matplotlib.pyplot as plt

# filename = '/project/mitmproxy_2021_12_03_14_56.cap'
filename = '/project/mitmproxy_2021_11_29_15_48.cap'
flows = []
results = []
appList = ['GSuite', 'WhatsApp', 'Telegram', 'Session', 'Wire', 'Signal', 'FDroid', 'AppDefault', 'AndroidNative']
log = syslog_client.Syslog()


def load_file(file_to_load):
	with open(file_to_load, 'rb') as fp:
		reader = FlowReader(fp)

		for HTTPFlow in reader.stream():
			new_flow = AnalysisFlow.AnalysisFlow()
			new_flow.import_raw_flow(HTTPFlow)
			new_flow.flowtype = HTTPFlow.type
			new_flow.user_agent = new_flow.get_user_agent()
			if new_flow.flowtype == 'http':
				app = AppFinder.find_app2(HTTPFlow, appList, str(new_flow.user_agent[1]))
				new_flow.app = app
				new_flow.url = HTTPFlow.request.pretty_url
				flows.append(new_flow)
			# print(flow.request.url)
	return


def print_flows():
	counter = 0
	for flow in flows:
		print(counter)
		print(flow.all)
		print('')
		counter = counter + 1
	return


def print_flow(num):
	print(flows[num].all)
	return


def check_for_unhelpful(flow):
	if (flow[0:14] == 'Loading script' or
				flow[0:22] == 'Proxy server listening' or flow[0:9] == 'Traceback' or
				flow[0:1] == '<' or
				flow[0:12] == 'Auto Content' or
				flow[0:10] == 'ValueError' or
				flow[0:15] == 'During handling' or
				flow[0:18] == 'UnicodeDecodeError' or
				flow[0:17] == 'Initiating HTTP/2' or
				flow[0:19] == 'EOFError: requested' or
				flow[0:54] == 'TypeError: don\'t know how to handle UnicodeDecodeError' or
				flow[0:flow.find('\n')].find('StreamClosedError') > -1 or
				flow[0:flow.find('\n')].find('HEADERS frame suppressed') > -1 or
				flow[0:flow.find('\n')].find('HTTP/2 PRIORITY frame suppressed') > -1 or
				flow[0:flow.find('\n')].find('ALPN') > -1 or
				flow[0:flow.find('\n')].find('HTTP2 Event') > -1 or
				flow[0:flow.find('\n')].find('clientconnect') > -1 or
				flow[0:flow.find('\n')].find('serverconnect') > -1 or
				flow[0:flow.find('\n')].find('clientdisconnect') > -1 or
				flow[0:flow.find('\n')].find('serverdisconnect') > -1 or
				flow[0:flow.find('\n')].find('Error in WebSocket connection') > -1 or
				flow[0:flow.find('\n')].find('WebSocket connection closed') > -1 or
				flow[flow.find('\n'):].find('-> Request') > -1 or
				flow[flow.find('\n'):].find('-> Response') > -1 or
				flow[0:flow.find('\n')].find(': CONNECT') > -1 or
				flow[0:flow.find('\n')].find('Set new server address:') > -1 or
				flow[0:flow.find('\n')].find('WebSocket 2 message') > -1 or
				flow[0:flow.find('\n')].find('WebSocket 1 message') > -1 or
				flow[0:flow.find('\n')].find('Failed to send error response to client:') > -1 or
				flow[0:flow.find('\n')].find(': HTTP/2 connection terminated by server: error code:') > -1 or
				flow[0:flow.find('\n')].find('Establish TLS') > -1 or
				flow[0:].find('Cannot establish TLS with client') > -1 or
				flow[0:].find('Error connecting to') > -1 or
				flow[0:].find('SourceFile:') > -1 or
				flow[0:].find('at java.') > -1 or
				flow[0:flow.find('\n')].find('server communication error:') > -1 or
				flow[0:flow.find('\n')].find('Connection killed') > -1 or
				flow[0:flow.find('\n')].find('NotImplementedError') > -1):
		return True
	else:
		return False


def check_flow(flow):
	# results.clear()
	# flow.app = AppFinder.find_app(flow, appList)
	# print('App: ' + flow.app)
	
	if flow.app == 'GSuite' and 'GSuite' in appList:
		GSuite.checkBehavior(flow, results)
	if flow.app == 'FDroid' and 'FDroid' in appList:
		FDroid.checkBehavior(flow, results)
	if flow.app == 'Session' and 'Session' in appList:
		Session.checkBehavior(flow, results)		
	if flow.app == 'Signal' and 'Signal' in appList:
		Signal.checkBehavior(flow, results)
	if flow.app == 'Telegram' and 'Telegram' in appList:
		Telegram.checkBehavior(flow, results)
	if flow.app == 'WhatsApp' and 'WhatsApp' in appList:
		WhatsApp.checkBehavior(flow, results)		
	if flow.app == 'Wire' and 'Wire' in appList:
		Wire.checkBehavior(flow, results)
	if flow.app == 'YouTube' and 'YouTube' in appList:
		YouTube.checkBehavior(flow, results)
	if flow.app == 'AndroidNative' and 'AndroidNative' in appList:
		AndroidNative.checkBehavior(flow, results)
	if flow.app == 'AppDefault' and 'AppDefault' in appList:
		AppDefault.checkBehavior(flow, results)
	AppDefault.syncSource(flow, results)
	if 'RawDataSearch' in appList:
		RawDataSearch.checkRawData(flow, results)
	# print(flow.all)
	# print_logs(results)
	send_logs(results)
	return


def send_logs(send_results):
	for result in send_results:
		log.send(result.logFull, syslog_client.Level.INFO)
	return


def print_logs(log_results):
	print('\n')
	count = 0
	for result in log_results:
		count += 1
		print('Record log #' + str(count) + ' of ' + str(len(results)))
		print('Application: ' + result.get_app())
		print('Source: ' + result.get_source())
		print('Destination: ' + result.get_destination())
		print('Type: ' + result.get_type())
		print('Info: ' + result.get_info())
		print()
	return


def plot_logs(log_results):
	# plt.plot([1, 2, 3, 4])
	# plt.ylabel('some numbers')
	# plt.show()
	return


def analyze_all():
	count = 0
	for flow in flows:
		# print(count)
		# check_for_unhelpful(flow.raw_flow)
		check_flow(flow)
		count = count + 1
	return


load_file(filename)
# printFlows()
analyze_all()
print_logs(results)
plot_logs(results)
# findNewFlows()
