from mitmproxy import flowfilter
from mitmproxy import ctx, http

def response(flow):
	ctx.log.info("Response detected")
	flow.response.content = flow.response.make

def request( flow):
	ctx.log.info("Request detected")
	flow.request.content = flow.request.make

