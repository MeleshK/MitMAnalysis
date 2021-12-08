import mitmproxy.flow


class AnalysisFlow(mitmproxy.flow.Flow):

	raw_flow = []
	app = ''
	user_agent = ''
	url = ''
	flowtype = ''

	def __init__(self):
		self.raw_flow = []

	def get_application(self):
		return self.app

	def get_address(self):
		return self.raw_flow.server_conn.address[0]

	def getPort(self):
		return self.raw_flow.server_conn.address[1]

	def get_request_headers(self):
		return self.raw_flow.request.headers

	def get_response_headers(self):
		try:
			return self.raw_flow.response.headers
		except:
			return

	def import_raw_flow(self, flow):
		self.raw_flow = flow

	def get_source(self):
		return str(self.raw_flow.server_conn.address[0])

	def get_destination(self):
		return str(self.raw_flow.client_conn.address[0])

	def get_url(self):
		self.url = str(self.raw_flow.request.pretty_url)
		return str(self.raw_flow.request.pretty_url)

	def get_request_type(self):
		return str(self.raw_flow.request.method)

	def get_type(self):
		return str(self.raw_flow.type)

	def get_host(self):
		return str(self.raw_flow.request.pretty_host)

	def find_request_headers(self):
		if 'Referer' in self.raw_flow.request.headers:
			return True
		else:
			return False

	def get_user_agent(self):
		if self.flowtype == 'http':
			for field in self.raw_flow.request.headers.fields:
				if field[0] == b'User-Agent':
					return field


	def get_metadata(self):
		return self.raw_flow.metadata
