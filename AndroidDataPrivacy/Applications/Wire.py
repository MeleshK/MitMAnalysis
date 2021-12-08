import AndroidDataPrivacy.AnalysisFlow as Flow
import AndroidDataPrivacy.Result as Result
import AndroidDataPrivacy.Applications.AppDefault as AppDefault

urls = ['http://schemas.android.com/apk/res-auto',
								'http://schemas.android.com/apk/res/android',
								'http://xmlpull.org/v1/doc/features.html#indent-output',
								'https://account.wire.com',
								'https://clientblacklist.wire.com/prod/android',
								'https://plus.google.com/',
								'https://prod-nginz-https.wire.com',
								'https://prod-nginz-ssl.wire.com',
								'https://teams.wire.com',
								'https://wire.com',
								'https://www.googleapis.com/auth/games',
								'https://www.googleapis.com/auth/games_lite']

partialURLs = []

userAgents = ['com.wire']

partialUserAgents = []


def checkBehavior(flow, results):
	if flow.get_request_type() == 'GET':
		analyzeGetRequest(flow, results)
	if flow.get_request_type == 'POST':
		analyzePostRequest(flow, results)
	if flow.get_request_type == 'HEAD':
		analyzePostRequest(flow, results)
	if flow.get_request_type == 'PUT':
		analyzePutRequest(flow, results)
	if flow.get_request_type == 'DELETE':
		analyzeDeleteRequest(flow, results)


def analyzeGetRequest(flow, results):
	checkGetURL(flow, results)
	checkRequestHeaders(flow, flow.get_request_headers(), results)
	AppDefault.checkRequestHeadersDefault(flow, flow.get_request_headers(), results)
	checkResponseHeaders(flow, flow.get_response_headers(), results)
	AppDefault.checkResponseHeadersDefault(flow, flow.get_response_headers(), results)
	AppDefault.analyzeGetRequestDefault(flow, results)


def analyzePostRequest(flow, results):
	checkPostURL(flow, results)
	checkRequestHeaders(flow, flow.get_request_headers(), results)
	AppDefault.checkRequestHeadersDefault(flow, flow.get_request_headers(), results)
	checkResponseHeaders(flow, flow.get_response_headers(), results)
	AppDefault.checkResponseHeadersDefault(flow, flow.get_response_headers(), results)
	AppDefault.analyzePostRequestDefault(flow, results)


def analyzeHeadRequest(flow, results):
	checkHeadURL(flow, results)
	checkRequestHeaders(flow, flow.get_request_headers(), results)
	AppDefault.checkRequestHeadersDefault(flow, flow.get_request_headers(), results)
	checkResponseHeaders(flow, flow.get_response_headers(), results)
	AppDefault.checkResponseHeadersDefault(flow, flow.get_response_headers(), results)
	AppDefault.analyzeHeadRequestDefault(flow, results)


def analyzePutRequest(flow, results):
	checkPutURL(flow, results)
	checkRequestHeaders(flow, flow.get_request_headers(), results)
	AppDefault.checkRequestHeadersDefault(flow, flow.get_request_headers(), results)
	checkResponseHeaders(flow, flow.get_response_headers(), results)
	AppDefault.checkResponseHeadersDefault(flow, flow.get_response_headers(), results)
	AppDefault.analyzePutRequestDefault(flow, results)


def analyzeDeleteRequest(flow, results):
	checkDeleteURL(flow, results)
	checkRequestHeaders(flow, flow.get_request_headers(), results)
	AppDefault.checkRequestHeadersDefault(flow, flow.get_request_headers(), results)
	checkResponseHeaders(flow, flow.get_response_headers(), results)
	AppDefault.checkResponseHeadersDefault(flow, flow.get_response_headers(), results)
	AppDefault.analyzeDeleteRequestDefault(flow, results)


def checkRequestHeaders(flow, headers, results):
	return None


def checkResponseHeaders(flow, headers, results):
	return None


def checkGetURL(flow, results):
	return None


def checkPostURL(flow, results):
	return None


def checkHeadURL(flow, results):
	return None


def checkPutURL(flow, results):
	return None


def checkDeleteURL(flow, results):
	return None
