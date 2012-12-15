import urllib.request
import json

up = 'online'
down = 'offline'

def check_mc_login(status_json):
	status = status_json['report']['login']['status']
	if status == 'up':
		return up
	else:
		return down

def check_mc_skins(status_json):
	status = status_json['report']['skins']['status']
	if status == 'up':
		return up
	else:
		return down

def check_mc_accounts(status_json):
	status = status_json['report']['account']['status']
	if status == 'up':
		return up
	else:
		return down

def check_mc_session(status_json):
	status = status_json['report']['session']['status']
	if status == 'up':
		return up
	else:
		return down

def check_mc_website(status_json):
	status = status_json['report']['website']['status']
	if status == 'up':
		return up
	else:
		return down	

req = urllib.request.urlopen("http://xpaw.ru/mcstatus/realtime.json").read()
req_str = req.decode("utf-8")
jsn = json.loads(req_str)
msgs = 'Minecraft servers: \n\tSession: ' + check_mc_session(jsn) \
+ '. Accounts: ' + check_mc_accounts(jsn) + '. Website: ' + check_mc_website(jsn) \
+ '. Session: ' + check_mc_session(jsn) + '. Skins: ' + check_mc_skins(jsn) + '.'
print(msgs)
