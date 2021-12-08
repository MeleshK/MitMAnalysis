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
import AndroidDataPrivacy.AnalysisFlow as AnalysisFlow
import AndroidDataPrivacy.RawDataSearch as RawDataSearch
# import AndroidDataPrivacy.Result as Result
import AndroidDataPrivacy.syslog_client as syslog_client
from mitmproxy.io import FlowReader
import matplotlib.pyplot as plt

#filename = '/project/mitmproxy_2021_12_03_14_56.cap'
filename = '/project/mitmproxy_2021_11_29_15_48.cap'
# filename = '/project/mitmproxy_2021_11_25_20_11.cap'
flows = []
results = []
appList = ['GSuite', 'WhatsApp', 'Telegram', 'Session', 'Wire', 'Signal', 'FDroid', 'AppDefault', 'AndroidNative',
		   						 'Unknown']
flowCountList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
				# noinspection PyBroadException
				try:
					app = AppFinder.find_app2(HTTPFlow, appList, str(new_flow.user_agent[1]))
					new_flow.app = app
				except TypeError:
					new_flow.app = 'Unknown'
				# noinspection PyBroadException
				try:
					new_flow.url = HTTPFlow.request.pretty_url
				except TypeError:
					new_flow.url = 'unknown URL'
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


def check_flow(flow):

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
	try:
		flowCountList[appList.index(flow.app)] += 1
	except ValueError:
		flowCountList[appList.index('Unknown')] += 1
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
	plt.title('Flows per Application')
	plt.bar(appList, flowCountList)
	plt.xlabel('Application')
	plt.ylabel('Flow count')
	plt.show()
	return


def analyze_all():
	count = 0
	for flow in flows:
		# print(count)
		check_flow(flow)
		count = count + 1
	print('\n')
	print('flow count ' + str(count))
	return


load_file(filename)
# printFlows()
analyze_all()
print_logs(results)
plot_logs(results)
# findNewFlows()
