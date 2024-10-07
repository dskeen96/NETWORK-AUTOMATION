import requests  # type: ignore
from requests.auth import HTTPBasicAuth
import xmltodict  # type: ignore
import json
#The line from requests.auth import HTTPBasicAuth is used in Python to 
# import the HTTPBasicAuth class from the requests library. 

url = 'https://devnetsandboxiosxe.cisco.com:443/restconf/data/ietf-interfaces:interfaces-state/'

#If you want to print each element of an array (or list) on a new line in Python, 
# you can use a loop or a list comprehension. Here are a few ways to do this:
List = dir(requests)
for item in List:
    print(item)

username = 'admin'
password = 'C1sco12345'
 
# (VERIFY=FALSE) SSL CONNECTION OFF 
# Warning: Disabling SSL verification can expose you to man-in-the-middle attacks. 
# Use it only for testing or in trusted environments.
response = requests.get(url,auth=HTTPBasicAuth('admin', 'C1sco12345'),verify=False)

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")


router_data = (response.text)
# Convert XML to a Python dictionary
dict_data = xmltodict.parse(router_data)

# Convert the dictionary to JSON
json_data = json.dumps(dict_data, indent=4)
print(json_data)



