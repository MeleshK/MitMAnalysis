# import AndroidDataPrivacy.AnalysisFlow as AnalysisFlow
# import AndroidDataPrivacy.Result as Result


def find_app(flow, app_list):
	# requestHeaders = flow.get_request_headers()
	# url = flow.raw_flow.request.pretty_host
	# flow.raw_flow.request.user
	useragent = flow.get_user_agent()
	useragentstring = str(useragent[1])
	flow.user_agent = useragentstring
	app = ''

	for application in app_list:
		# print('app:\t'+application.lower() + '\tUser Agent String\t'+useragentstring + '\n')
		found = useragentstring.find(application.lower())
		if 1 <= found:
			app = application

		else:
			app = ''
	flow.app = app
	return app


def find_app2(flow, app_list, useragentstring):
	app = ''

	for application in app_list:
		# print('app:\t'+application.lower() + '\tUser Agent String\t'+useragentstring + '\n')
		found = useragentstring.find(application)
		if 1 <= found:
			app = application
			return app
		else:
			app = ''
	return app

def identify_user_agent(agent, app_list):
	if 'AndroidNative' in app_list:
		import AndroidDataPrivacy.Applications.AndroidNative as AndroidNative
		if agent in AndroidNative.userAgents:
			return 'AndroidNative'
		for item in AndroidNative.partialUserAgents:
			if agent.find(item) > -1:
				return 'AndroidNative'

	if 'GSuite' in app_list:
		import AndroidDataPrivacy.Applications.GSuite as GSuite
		if agent in GSuite.userAgents:
			return 'GSuite'
		for item in GSuite.partialUserAgents:
			if agent.find(item) > -1:
				return 'GSuite'

	if 'Youtube' in app_list:
		import AndroidDataPrivacy.Applications.Youtube as Youtube
		if agent in Youtube.userAgents:
			return 'Youtube'
		for item in Youtube.partialUserAgents:
			if agent.find(item) > -1:
				return 'Youtube'

	if 'Reddit' in app_list:
		import AndroidDataPrivacy.Applications.Reddit as Reddit
		if agent in Reddit.userAgents:
			return 'Reddit'
		for item in Reddit.partialUserAgents:
			if agent.find(item) > -1:
				return 'Reddit'

	if 'Slack' in app_list:
		import AndroidDataPrivacy.Applications.Slack as Slack
		if agent in Slack.userAgents:
			return 'Slack'
		for item in Slack.partialUserAgents:
			if agent.find(item) > -1:
				return 'Slack'

	if 'Discord' in app_list:
		import AndroidDataPrivacy.Applications.Discord as Discord
		if agent in Discord.userAgents:
			return 'Discord'
		for item in Discord.partialUserAgents:
			if agent.find(item) > -1:
				return 'Discord'

	if 'Spotify' in app_list:
		import AndroidDataPrivacy.Applications.Spotify as Spotify
		if agent in Spotify.userAgents:
			return 'Spotify'
		for item in Spotify.partialUserAgents:
			if agent.find(item) > -1:
				return 'Spotify'

	if 'Venmo' in app_list:
		import AndroidDataPrivacy.Applications.Venmo as Venmo
		if agent in Venmo.userAgents:
			return 'Venmo'
		for item in Venmo.partialUserAgents:
			if agent.find(item) > -1:
				return 'Venmo'

	if 'Facebook' in app_list:
		import AndroidDataPrivacy.Applications.Facebook as Facebook
		if agent in Facebook.userAgents:
			return 'Facebook'
		for item in Facebook.partialUserAgents:
			if agent.find(item) > -1:
				return 'Facebook'

	if 'LinkedIn' in app_list:
		import AndroidDataPrivacy.Applications.LinkedIn as LinkedIn
		if agent in LinkedIn.userAgents:
			return 'LinkedIn'
		for item in LinkedIn.partialUserAgents:
			if agent.find(item) > -1:
				return 'LinkedIn'

	if 'Canvas' in app_list:
		import AndroidDataPrivacy.Applications.Canvas as Canvas
		if agent in Canvas.userAgents:
			return 'Canvas'
		for item in Canvas.partialUserAgents:
			if agent.find(item) > -1:
				return 'Canvas'

	if 'RocketChat' in app_list:
		import AndroidDataPrivacy.Applications.RocketChat as RocketChat
		if agent in RocketChat.userAgents:
			return 'RocketChat'
		for item in RocketChat.partialUserAgents:
			if agent.find(item) > -1:
				return 'RocketChat'

	if 'Session' in app_list:
		import AndroidDataPrivacy.Applications.Session as Session
		if agent in Session.userAgents:
			return 'Session'
		for item in Session.partialUserAgents:
			if agent.find(item) > -1:
				return 'Session'

	if 'Signal' in app_list:
		import AndroidDataPrivacy.Applications.Signal as Signal
		if agent in Signal.userAgents:
			return 'Signal'
		for item in Signal.partialUserAgents:
			if agent.find(item) > -1:
				return 'Signal'

	if 'Telegram' in app_list:
		import AndroidDataPrivacy.Applications.Telegram as Telegram
		if agent in Telegram.userAgents:
			return 'Telegram'
		for item in Telegram.partialUserAgents:
			if agent.find(item) > -1:
				return 'Telegram'

	if 'WhatsApp' in app_list:
		import AndroidDataPrivacy.Applications.WhatsApp as WhatsApp
		if agent in WhatsApp.userAgents:
			return 'WhatsApp'
		for item in WhatsApp.partialUserAgents:
			if agent.find(item) > -1:
				return 'WhatsApp'

	if 'Wire' in app_list:
		import AndroidDataPrivacy.Applications.Wire as Wire
		if agent in Wire.userAgents:
			return 'Wire'
		for item in Wire.partialUserAgents:
			if agent.find(item) > -1:
				return 'Wire'

	if 'Hulu' in app_list:
		import AndroidDataPrivacy.Applications.Hulu as Hulu
		if agent in Hulu.userAgents:
			return 'Hulu'
		for item in Hulu.partialUserAgents:
			if agent.find(item) > -1:
				return 'Hulu'

	if 'Netflix' in app_list:
		import AndroidDataPrivacy.Applications.Netflix as Netflix
		if agent in Netflix.userAgents:
			return 'Netflix'
		for item in Netflix.partialUserAgents:
			if agent.find(item) > -1:
				return 'Netflix'

	if 'KeeperSecurity' in app_list:
		import AndroidDataPrivacy.Applications.KeeperSecurity as KeeperSecurity
		if agent in KeeperSecurity.userAgents:
			return 'KeeperSecurity'
		for item in KeeperSecurity.partialUserAgents:
			if agent.find(item) > -1:
				return 'KeeperSecurity'

	if 'CertInstaller' in app_list:
		import AndroidDataPrivacy.Applications.CertInstaller as CertInstaller
		if agent in CertInstaller.userAgents:
			return 'CertInstaller'
		for item in CertInstaller.partialUserAgents:
			if agent.find(item) > -1:
				return 'CertInstaller'

	return ''


def identify_uniform_resource_locator(flow, url, app_list):
	if 'AndroidNative' in app_list:
		import AndroidDataPrivacy.Applications.AndroidNative as AndroidNative
		if url in AndroidNative.urls:
			return 'AndroidNative'
		for item in AndroidNative.partialURLs:
			if url.find(item) > -1:
				return 'AndroidNative'

	if 'GSuite' in app_list:
		import AndroidDataPrivacy.Applications.GSuite as GSuite
		if url in GSuite.urls:
			return 'GSuite'
		for item in GSuite.partialURLs:
			if url.find(item) > -1:
				return 'GSuite'

	if 'Youtube' in app_list:
		import AndroidDataPrivacy.Applications.Youtube as Youtube
		if url in Youtube.urls:
			return 'Youtube'
		for item in Youtube.partialURLs:
			if url.find(item) > -1:
				return 'Youtube'

	if 'Reddit' in app_list:
		import AndroidDataPrivacy.Applications.Reddit as Reddit
		if url in Reddit.urls:
			return 'Reddit'
		for item in Reddit.partialURLs:
			if url.find(item) > -1:
				return 'Reddit'

	if 'Session' in app_list:
		import AndroidDataPrivacy.Applications.Session as Session
		if url in Session.urls:
			return 'Session'
		for item in Session.partialURLs:
			if url.find(item) > -1:
				return 'Session'

	if 'Signal' in app_list:
		import AndroidDataPrivacy.Applications.Signal as Signal
		if url in Signal.urls:
			return 'Signal'
		for item in Signal.partialURLs:
			if url.find(item) > -1:
				return 'Signal'

	if 'Telegram' in app_list:
		import AndroidDataPrivacy.Applications.Telegram as Telegram
		if url in Telegram.urls:
			return 'Telegram'
		for item in Telegram.partialURLs:
			if url.find(item) > -1:
				return 'Telegram'

	if 'Wire' in app_list:
		import AndroidDataPrivacy.Applications.Wire as Wire
		if url in Wire.urls:
			return 'Wire'
		for item in Wire.partialURLs:
			if url.find(item) > -1:
				return 'Wire'

	if 'Wire' in app_list:
		import AndroidDataPrivacy.Applications.Wire as Wire
		if url in Wire.urls:
			return 'Wire'
		for item in Wire.partialURLs:
			if url.find(item) > -1:
				return 'Wire'

	if 'Slack' in app_list:
		import AndroidDataPrivacy.Applications.Slack as Slack
		if url in Slack.urls:
			return 'Slack'
		for item in Slack.partialURLs:
			if url.find(item) > -1:
				return 'Slack'

	if 'Discord' in app_list:
		import AndroidDataPrivacy.Applications.Discord as Discord
		if url in Discord.urls:
			return 'Discord'
		for item in Discord.partialURLs:
			if url.find(item) > -1:
				return 'Discord'

	if 'Spotify' in app_list:
		import AndroidDataPrivacy.Applications.Spotify as Spotify
		if url in Spotify.urls:
			return 'Spotify'
		for item in Spotify.partialURLs:
			if url.find(item) > -1:
				return 'Spotify'

	if 'Venmo' in app_list:
		import AndroidDataPrivacy.Applications.Venmo as Venmo
		if url in Venmo.urls:
			return 'Venmo'
		for item in Venmo.partialURLs:
			if url.find(item) > -1:
				return 'Venmo'

	if 'Facebook' in app_list:
		import AndroidDataPrivacy.Applications.Facebook as Facebook
		if url in Facebook.urls:
			return 'Facebook'
		for item in Facebook.partialURLs:
			if url.find(item) > -1:
				return 'Facebook'

	if 'LinkedIn' in app_list:
		import AndroidDataPrivacy.Applications.LinkedIn as LinkedIn
		if url in LinkedIn.urls:
			return 'LinkedIn'
		for item in LinkedIn.partialURLs:
			if url.find(item) > -1:
				return 'LinkedIn'

	if 'Canvas' in app_list:
		import AndroidDataPrivacy.Applications.Canvas as Canvas
		if url in Canvas.urls:
			return 'Canvas'
		for item in Canvas.partialURLs:
			if url.find(item) > -1:
				return 'Canvas'

	if 'RocketChat' in app_list:
		import AndroidDataPrivacy.Applications.RocketChat as RocketChat
		if url in RocketChat.urls:
			return 'RocketChat'
		for item in RocketChat.partialURLs:
			if url.find(item) > -1:
				return 'RocketChat'

	if 'Hulu' in app_list:
		import AndroidDataPrivacy.Applications.Hulu as Hulu
		if url in Hulu.urls:
			return 'Hulu'
		for item in Hulu.partialURLs:
			if url.find(item) > -1:
				return 'Hulu'

	if 'Netflix' in app_list:
		import AndroidDataPrivacy.Applications.Netflix as Netflix
		if url in Netflix.urls:
			return 'Netflix'
		for item in Netflix.partialURLs:
			if url.find(item) > -1:
				return 'Netflix'

	if 'KeeperSecurity' in app_list:
		import AndroidDataPrivacy.Applications.KeeperSecurity as KeeperSecurity
		if url in KeeperSecurity.urls:
			return 'KeeperSecurity'
		for item in KeeperSecurity.partialURLs:
			if url.find(item) > -1:
				return 'KeeperSecurity'

	if 'CertInstaller' in app_list:
		import AndroidDataPrivacy.Applications.CertInstaller as CertInstaller
		if url in CertInstaller.urls:
			return 'CertInstaller'
		for item in CertInstaller.partialURLs:
			if url.find(item) > -1:
				return 'CertInstaller'

	if url[:21] == 'https://api.branch.io':
		temp = flow.requestContent
		temp = temp[temp.find('"cd": {'):]
		temp = temp[:temp.find('}')]
		temp = temp[temp.find('"pn": "')+7:]
		temp = temp[:temp.find('"')]
		if temp[:10] == 'com.reddit':
			return 'Reddit'

	return ''


def identify_referer(referer):
	if referer == 'android-app://com.google.android.gm':
		return 'com.google.android.gm'
	elif referer == 'https://champlain.instructure.com/':
		return 'Canvas'
	elif referer == 'https://cloud.rocket.chat/trial':
		return 'RocketChat'
	return ''


def translate(app):
	if (app == 'com.google.android.apps.messaging' or
				app == 'com.google.android.googlequicksearchbox' or
				app == 'com.google.android.gms' or
				app == 'com.google.android.gm' or
				app == 'com.android.vending'):
		app = 'AndroidNative'

	elif(app == 'com.google.android.apps.tachyon' or
						app == 'com.google.android.calendar' or
						app == 'com.google.android.contacts' or
						app == 'com.google.android.apps.maps' or
						app == 'com.google.android.apps.photos' or
						app == 'com.google.android.talk' or
						app == 'com.google.android.apps.docs'):
		app = 'GSuite'

	elif app == 'com.reddit.frontpage':
		app = 'Reddit'

	elif app == 'com.google.android.youtube':
		app = 'Youtube'

	elif app == 'com.discord':
		app = 'Discord'

	elif app == 'com.spotify.music':
		app = 'Spotify'

	elif app == 'com.venmo':
		app = 'Venmo'

	elif app == 'com.instructure.candroid':
		app = 'Canvas'

	elif app == 'chat.rocket.android':
		app = 'RocketChat'

	elif app == 'com.hulu.plus':
		app = 'Hulu'

	elif app == 'com.netflix.mediaclient':
		app = 'Netflix'

	if app == '':
		app = 'AppDefault'
	return app
