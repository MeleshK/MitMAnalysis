from mitmproxy import flowfilter
from mitmproxy import ctx, http

def response(flow):
		flow.response.content = flow.response.assemble

def request( flow):
		flow.request.content = flow.request.assemble

