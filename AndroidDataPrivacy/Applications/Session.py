import AndroidDataPrivacy.Flow as Flow
import AndroidDataPrivacy.Result as Result
import AndroidDataPrivacy.Applications.AppDefault as AppDefault

urls = ['https://www.whatsapp.com/security?lg=', \
'https://www.facebook.com/images/here_maps/here_maps_logo_32px.png', \
'https://maps.google.com/?q=', \
'https://www.messenger.com/groupcall/create', \
'https://static.whatsapp.net/emoji?lgs=', \
'https://l.wl.co/l?u=', \
'https://www.whatsapp.com/android/', \
'https://whatsapp.com/dl/', \
'http://www.android.com/', \
'https://maps.instagram.com/maps/static/?', \
'https://play.google.com/apps/testing/', \
'https://graph.', \
'http://www.google.com/settings/storage?emr=0&authuser=-1&utm_source=whatsapp', \
'https://wa.me/message/', \
'https://www.whatsapp.com/legal/updates/privacy-policy', \
'https://api.giphy.com/v1/gifs/search', \
'https://www.facebook.com/help/111814505650678', \
'https://wa.tenor.co/v1/trending', \
'http://www.google-analytics.com', \
'https://ssl.google-analytics.com', \
'https://(www\.)?pbs\.twimg\.com', \
'https://www.whatsapp.com/legal/updates/terms-of-service-eea', \
'https://crashlogs.whatsapp.net/wa_clb_data', \
'http://xmlpull.org/v1/doc/features.html#indent-output', \
'https://static.whatsapp.net/downloadable?', \
'https://www.whatsapp.com/legal/#terms-of-service-age', \
'https://www.whatsapp.com/android/current/WhatsApp.apk', \
'https://(www\.)?(web\.)?facebook\.com', \
'https://faq.whatsapp.com/android/chats/how-to-restore-your-chat-history', \
'https://www.whatsapp.com/legal/#privacy-policy-managing-and-deleting-your-information', \
'https://www.googleapis.com/auth/games', \
'https://www.whatsapp.com/security', \
'http://xmlpull.org/v1/doc/features.html#process-docdecl', \
'https://api.giphy.com/v1/gifs/trending', \
'https://(www\.)?pbs\.twimg\.com/profile_images', \
'https://www.whatsapp.com/legal/', \
'https://pagead2.googlesyndication.com/pagead/gen_204?id=gmob-apps', \
'https://wa.tenor.co/v1/search', \
'https://www.whatsapp.com/legal/#privacy-policy', \
'https://www.googleapis.com/auth/games_lite', \
'https://graph.facebook.com/v2.2/maps_configs?fields=base_url,static_base_url,osm_config,url_override_config&pretty=&access_token=', \
'https://expresswifi.com/maps/static/?', \
'https://www.facebook.com/maps/static/?', \
'http://xmlpull.org/v1/doc/features.html#process-namespaces', \
'http://www.w3.org/ns/ttml#parameter', \
'https://faq.whatsapp.com/payments', \
'http://schemas.android.com/apk/res-auto', \
'https://www.whatsapp.com/legal/updates/terms-of-service', \
'https://crashlogs.whatsapp.net/wa_profilo_data', \
'https://www.facebook.com/images/here_maps/here_maps_logo_64px.png', \
'https://faq.whatsapp.com/general/28030015/', \
'http://ns.adobe.com/xap/1.0/', \
'https://www.facebook.com/%s/shop/', \
'https://www.facebook.com/maps/provider_by_viewport?', \
'https://www.whatsapp.com/legal/brazil-privacy-notice', \
'https://wa.me/qr/', \
'https://crashlogs.whatsapp.net/wa_fls_upload_check', \
'https://maps.instagram.com/maps/tile/?', \
'https://www.whatsapp.com/legal/#terms-of-service', \
'http://www.w3.org/2000/svg', \
'http://www.w3.org/TR/SVG11/feature#', \
'https://www.whatsapp.com/legal/#cookies', \
'https://www.facebook.com/maps/tile/?', \
'https://www.whatsapp.com/download/', \
'http://schemas.android.com/apk/res/android', \
'https://expresswifi.com/maps/tile/?', \
'https://wa.me', \
'https://static.whatsapp.net/downloadable?category=', \
'https://faq.whatsapp.com/general/26000112/', \
'https://www.whatsapp.com/legal/updates/privacy-policy-eea', \
'https://faq.whatsapp.com/android/troubleshooting/cant-create-or-restore-a-google-drive-backup', \
'https://www.whatsapp.com/legal/#privacy-policy-our-global-operations', \
'http://www.w3.org/1999/xlink']

partialURLs = []

userAgents = []

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
	if ('referer' in headers.keys()):
		type = 'Referer'
		info = headers['referer']
		results.append(Result.Result(flow, type, info))

def checkResponseHeaders(flow, headers, results):
	return None

def checkGetURL(flow, results):
	flow.source = 'WhatsApp'

	if (flow.url.find('https://certify.alexametrics.com/atrk') == 0):
		type = 'RocketChat AlexaMetrics Session Cookie'
		info = AppDefault.findFormEntry(flow.requestContent, 'sess_cookie')
		results.append(Result.Result(flow, type, info))

	elif (flow.url.find('https://q.stripe.com/?event') == 0):
		type = 'Stripe Key'
		info = AppDefault.findFormEntry(flow.requestContent, 'key')
		results.append(Result.Result(flow, type, info))

		type = 'Stripe JS ID'
		info = AppDefault.findFormEntry(flow.requestContent, 'stripe_js_id')
		results.append(Result.Result(flow, type, info))

		type = 'Stripe Event'
		info = AppDefault.findFormEntry(flow.requestContent, 'event')
		results.append(Result.Result(flow, type, info))

	elif (flow.url.find('https://open.rocket.chat/api/v1/settings.public') == 0 and flow.url.find('RegistrationForm') > -1):
		type = 'User Action: RocketChat Screen View'
		info = 'Viewed Registration Form'
		results.append(Result.Result(flow, type, info))

	elif (flow.url == 'https://open.rocket.chat/api/v1/me'):
		type = 'User Action: Viewed Profile'
		info = 'Viewed own profile'
		results.append(Result.Result(flow, type, info))

		type = 'RocketChat ID'
		info = flow.responseContent[flow.responseContent.find('id":')+6:]
		info = info[:info.find('"')]
		results.append(Result.Result(flow, type, info))

	elif (flow.url.find('https://open.rocket.chat/api/v1/spotlight') == 0):
		type = 'User Action: RocketChat Search'
		info = AppDefault.findFormEntry(flow.requestContent, 'query')
		results.append(Result.Result(flow, type, info))

	elif (flow.url.find('https://open.rocket.chat/api/v1/channels.getAllUserMentionsByChannel') == 0):
		type = 'User Action: Viewed Channel Mentions'
		info = AppDefault.findFormEntry(flow.requestContent, 'roomId')
		results.append(Result.Result(flow, type, info))

	elif (flow.url.find('https://open.rocket.chat/api/v1/channels.files') == 0):
		type = 'User Action: Viewed Channel Files'
		info = AppDefault.findFormEntry(flow.requestContent, 'roomId')
		results.append(Result.Result(flow, type, info))


def checkPostURL(flow, results):
	flow.source = 'WhatsApp'

	if (flow.url == 'https://open.rocket.chat/api/v1/users.register'):
		type = 'User Info: Email Address'
		info = AppDefault.findJSONItem(flow.requestContent, 'email')
		results.append(Result.Result(flow, type, info))

		type = 'User Info: RocketChat Name'
		info = AppDefault.findJSONItem(flow.requestContent, 'name')
		results.append(Result.Result(flow, type, info))

		type = 'User Info: RocketChat Password'
		info = AppDefault.findJSONItem(flow.requestContent, 'pass')
		results.append(Result.Result(flow, type, info))

		type = 'User Info: RocketChat Username'
		info = AppDefault.findJSONItem(flow.requestContent, 'username')
		results.append(Result.Result(flow, type, info))

	elif (flow.url == 'https://open.rocket.chat/api/v1/login'):
		type = 'User Info: RocketChat Password'
		info = AppDefault.findJSONItem(flow.requestContent, 'pass')
		results.append(Result.Result(flow, type, info))

		type = 'User Info: RocketChat Username'
		info = AppDefault.findJSONItem(flow.requestContent, 'username')
		results.append(Result.Result(flow, type, info))

	elif (flow.url == 'https://open.rocket.chat/api/v1/push.token'):
		type = 'RocketChat GCM Token'
		info = AppDefault.findJSONItem(flow.requestContent, 'value')
		results.append(Result.Result(flow, type, info))

	elif (flow.url == 'https://open.rocket.chat/api/v1/channels.create'):
		type = 'User Action: Create Channel'
		info = flow.requestContent[flow.requestContent.find('"name":')+9:]
		info = info[:info]
		results.append(Result.Result(flow, type, info))

	elif (flow.url == 'https://open.rocket.chat/api/v1/chat.sendMessage'):
		type = 'User Action: Send Message'
		info = flow.requestContent[flow.requestContent.find('"msg":')+8:]
		info = info[:info.find('"')]
		results.append(Result.Result(flow, type, info))

	elif (flow.url.find('https://open.rocket.chat/api/v1/chat.search') == 0):
		type = 'User Action: Chat Search'
		info = AppDefault.findFormEntry(flow.requestContent, 'searchText')
		results.append(Result.Result(flow, type, info))

	elif (flow.url == 'https://open.rocket.chat/api/v1/users.deleteOwnAccount'):
		type = 'User Action: Delete Account'
		info = 'Deleted RocketChat Account'
		results.append(Result.Result(flow, type, info))

	elif (flow.url == 'https://open.rocket.chat/api/v1/logout'):
		type = 'User Action: Logout'
		info = 'Logged Out'
		results.append(Result.Result(flow, type, info))


def checkHeadURL(flow, results):
	return None

def checkPutURL(flow, results):
	return None

def checkDeleteURL(flow, results):
	return None
