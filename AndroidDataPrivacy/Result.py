class Result:

	app = ''
	source = ''
	destination = ''
	type = ''
	info = ''
	flowContent = ''
	log = ''
	logFull = ''

	def __init__(self, aApp, aDestination, aSource, aType, aInfo, aflowContent):
		self.app = aApp
		self.source = aSource
		self.destination = aDestination
		self.type = aType
		self.info = aInfo
		self.flowContent = aflowContent
		self.log = self.source + ';;;;;' + \
		self.destination + ';;;;;' + \
		self.type + ';;;;;' + \
		self.info
		self.logFull = self.log + ';;;;;' + '\n\n' + self.flowContent

	def __init__(self, flow, aType, aInfo):
		self.app = flow.app
		self.source = flow.get_host()
		self.destination = flow.get_destination()
		self.type = aType
		self.info = aInfo
		self.flowContent = flow.raw_flow.request.content
		self.log = flow.get_source() + ';;;;;' + '\n'
		self.destination + ';;;;;' + '\n'
		self.type + ';;;;;' + '\n'
		self.info
		self.logFull = self.log + ';;;;;' + '\n\n' + str(self.flowContent)

	def syncSourceLog(self):
		self.log = self.source + ';;;;;'
		self.destination + ';;;;;'
		self.type + ';;;;;'
		self.info
		self.logFull = self.log + ';;;;;' + '\n\n' + str(self.flowContent)

	def get_app(self):
		return self.app

	def get_source(self):
		return self.source

	def get_destination(self):
		return self.destination

	def get_type(self):
		return self.type

	def get_info(self):
		return str(self.info)

	def get_flowContent(self):
		return self.flowContent

	def get_log(self):
		return self.log

	def get_logFull(self):
		return self.logFull