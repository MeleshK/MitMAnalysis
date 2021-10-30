import mitmproxy

def response(flow):
	with decoded(flow.response):
		flow.response.content = flow.response.assemble

def request( flow):
	with decoded(flow.request):
		flow.request.content = flow.request.assemble

