import AndroidDataPrivacy.AnalysisFlow as Flow
import AndroidDataPrivacy.Result as Result
import AndroidDataPrivacy.Applications.AppDefault as AppDefault

urls = ['https://www.googleapis.com/auth/fitness.reproductive_health.write',
								'https://www.googleapis.com/auth/fitness.location.write',
								'https://www.googleapis.com/auth/games',
								'http://schemas.microsoft.com/DRM/2007/03/protocols/AcquireLicense',
								'https://www.googleapis.com/auth/drive.file',
								'https://www.googleapis.com/auth/plus.me',
								'https://www.googleapis.com/auth/drive',
								'https://www.googleapis.com/auth/fitness.body_temperature.write',
								'https://www.googleapis.com/auth/fitness.body.write',
								'https://www.googleapis.com/auth/fitness.activity.read',
								'https://www.googleapis.com/auth/fitness.location.read',
								'https://www.googleapis.com/auth/fitness.body_temperature.read',
								'https://www.googleapis.com/auth/datastoremobile',
								'https://www.googleapis.com/auth/fitness.activity.write',
								'http://www.gstatic.com/android/hangouts/hangouts_mms_ua_profile.xml',
								'https://www.googleapis.com/auth/fitness.nutrition.read',
								'https://www.googleapis.com/auth/fitness.blood_pressure.read',
								'https://www.googleapis.com/auth/fitness.body.read',
								'https://www.googleapis.com/auth/plus.login',
								'https://www.googleapis.com/auth/fitness.nutrition.write',
								'https://www.googleapis.com/auth/games_lite',
								'http://javax.xml.XMLConstants/feature/secure-processing',
								'https://www.googleapis.com/auth/appstate',
								'http://www.w3.org/ns/ttml#parameter',
								'https://www.googleapis.com/auth/fitness.blood_glucose.write',
								'http://ns.adobe.com/xap/1.0/',
								'https://www.googleapis.com/auth/fitness.oxygen_saturation.write',
								'https://www.googleapis.com/auth/drive.appdata',
								'https://www.googleapis.com/auth/games.firstparty',
								'https://www.googleapis.com/auth/fitness.reproductive_health.read ',
								'https://www.googleapis.com/auth/fitness.blood_pressure.write',
								'https://www.googleapis.com/auth/drive.apps',
								'http://schemas.android.com/apk/res/android',
								'https://www.googleapis.com/auth/fitness.blood_glucose.read',
								'https://www.googleapis.com/auth/fitness.oxygen_saturation.read']

partialURLs = []

userAgents = ['network.loki.messenger']

partialUserAgents = []


def checkBehavior(flow, results):
	if (flow.requestType == 'GET'):
		analyzeGetRequest(flow, results)
	if (flow.requestType == 'POST'):
		analyzePostRequest(flow, results)
	if (flow.requestType == 'HEAD'):
		analyzePostRequest(flow, results)
	if (flow.requestType == 'PUT'):
		analyzePutRequest(flow, results)
	if (flow.requestType == 'DELETE'):
		analyzeDeleteRequest(flow, results)

def analyzeGetRequest(flow, results):
	checkGetURL(flow, results)
	checkRequestHeaders(flow, flow.requestHeaders, results)
	AppDefault.checkRequestHeadersDefault(flow, flow.requestHeaders, results)
	checkResponseHeaders(flow, flow.responseHeaders, results)
	AppDefault.checkResponseHeadersDefault(flow, flow.responseHeaders, results)
	AppDefault.analyzeGetRequestDefault(flow, results)

def analyzePostRequest(flow, results):
	checkPostURL(flow, results)
	checkRequestHeaders(flow, flow.requestHeaders, results)
	AppDefault.checkRequestHeadersDefault(flow, flow.requestHeaders, results)
	checkResponseHeaders(flow, flow.responseHeaders, results)
	AppDefault.checkResponseHeadersDefault(flow, flow.responseHeaders, results)
	AppDefault.analyzePostRequestDefault(flow, results)

def analyzeHeadRequest(flow, results):
	checkHeadURL(flow, results)
	checkRequestHeaders(flow, flow.requestHeaders, results)
	AppDefault.checkRequestHeadersDefault(flow, flow.requestHeaders, results)
	checkResponseHeaders(flow, flow.responseHeaders, results)
	AppDefault.checkResponseHeadersDefault(flow, flow.responseHeaders, results)
	AppDefault.analyzeHeadRequestDefault(flow, results)

def analyzePutRequest(flow, results):
	checkPutURL(flow, results)
	checkRequestHeaders(flow, flow.requestHeaders, results)
	AppDefault.checkRequestHeadersDefault(flow, flow.requestHeaders, results)
	checkResponseHeaders(flow, flow.responseHeaders, results)
	AppDefault.checkResponseHeadersDefault(flow, flow.responseHeaders, results)
	AppDefault.analyzePutRequestDefault(flow, results)

def analyzeDeleteRequest(flow, results):
	checkDeleteURL(flow, results)
	checkRequestHeaders(flow, flow.requestHeaders, results)
	AppDefault.checkRequestHeadersDefault(flow, flow.requestHeaders, results)
	checkResponseHeaders(flow, flow.responseHeaders, results)
	AppDefault.checkResponseHeadersDefault(flow, flow.responseHeaders, results)
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
