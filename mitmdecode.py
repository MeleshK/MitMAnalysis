from mitmproxy import ctx, http

def request(self, flow: http.HTTPFlow) -> None:
	flow.request.content = flow.request.make
	ctx.log.info("Request detected")

def response(self, flow: http.HTTPFlow) -> None:
	ctx.log.info("Response detected")
	flow.response.content = flow.response.make



