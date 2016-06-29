# This works with Version 2.7 of Python
import urllib	
import json
url = 'http://api.hostip.info/get_json.php'
info = json.loads(urllib.urlopen(url).read())
print(info['ip'])