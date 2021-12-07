import AndroidDataPrivacy.AnalysisFlow as Flow
import AndroidDataPrivacy.Result as Result
import AndroidDataPrivacy.Applications.AppDefault as AppDefault

urls = ['https://ss3.4sqi.net/img/categories_v2/',
								'https://developer.apple.com/streaming/emsg-id3',
								'http://dashif.org/guidelines/trickmode',
								'https://telegram.org/deactivate?phone=',
								'https://t.me/socks?',
								'https://www.googleapis.com/auth/games',
								'http://schema.org/FailedActionStatus',
								'https://firebaseremoteconfig.googleapis.com/v1/projects/%s/namespaces/%s:fetch',
								'https://www.google.com/resolve?name=',
								'https://telegram.org/dl',
								'https://www.instagram.com/explore/tags/',
								'http://www.example.com',
								'https://t.me/',
								'https://plus.google.com/',
								'https://accounts.google.com/o/oauth2/revoke?token=',
								'https://static-maps',
								'https://t.me/joinchat/',
								'http://schema.org/CompletedActionStatus',
								'https://maps.googleapis',
								'https://maps.googleapis.com/maps/api/staticmap?center=%.6f,%.6f&zoom=%d&size=%dx%d&maptype=roadmap&scale=%d&key=%s',
								'https://maps.googleapis.com/maps/api/staticmap?center=%.6f,%.6f&zoom=%d&size=%dx%d&maptype=roadmap&scale=%d&markers=color:red%%7Csize:mid%%7C%.6f,%.6f&sensor=false&key=%s',
								'https://twitter.com/hashtag/',
								'http://www.google.com',
								'https://static-maps.yandex.ru/1.x/?ll=%.6f,%.6f&z=%d&size=%d,%d&l=map&scale=%d&pt=%.6f,%.6f,vkbkm&lang=%s',
								'https://%s/%s/%s',
								'https://telegram.org/embed',
								'https://maps.googleapis.com/maps/api/staticmap?center=%.6f,%.6f&zoom=%d&size=%dx%d&maptype=roadmap&scale=%d&markers=color:red%%7Csize:mid%%7C%.6f,%.6f&sensor=false',
								'https://www.googleapis.com/auth/games_lite',
								'http://www.w3.org/ns/ttml#parameter',
								'https://developers.google.com/actions?invocation=',
								'https://instagram.com/',
								'https://t.me/proxy?',
								'http://maps.google.com/maps?saddr=%f,%f&daddr=%f,%f',
								'http://ns.adobe.com/xap/1.0/',
								'https://t.me/+',
								'https://aomedia.org/emsg/ID3',
								'https://twitter.com/',
								'https://static-maps.yandex.ru/1.x/?ll=%.6f,%.6f&z=%d&size=%d,%d&l=map&scale=%d&lang=%s',
								'https://api.stripe.com',
								'https://tgb.smart-glocal.com/cds/v1/tokenize/card',
								'https://tgb-playground.smart-glocal.com/cds/v1/tokenize/card',
								'https://dns.google.com/resolve?name=',
								'https://mozilla.cloudflare-dns.com/dns-query?name=',
								'http://schemas.android.com/apk/res/android',
								'https://maps.googleapis.com/maps/api/staticmap?center=%.6f,%.6f&zoom=%d&size=%dx%d&maptype=roadmap&scale=%d',
								'https://play.google.com/store/apps/details?id=org.telegram.messenger',
								'https://telegram.org',
								'http://dashif.org/guidelines/last-segment-number']

partialURLs = []

userAgents = ['com.telegram']

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
