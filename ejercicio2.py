#!/usr/bin/python
import requests

if __name__ == '__main__':
 url = 'http://localhost:8181/restconf/operational/opendaylight-inventory:nodes/'

 response = requests.get(url,auth=('admin','admin'))


 if response.status_code == 200:
  response = response.json()

  for node in response['nodes']['node']:
  	print("************************")
  	print("NODE:"+node['id'])
  	print("************************")

  	for connector in node['node-connector']:
  		print("Connector-Name: "+connector['flow-node-inventory:name'])
  		print("Connector-MAC: "+connector['flow-node-inventory:hardware-address'])
  		try:
  			for add in connector['address-tracker:addresses']:
  				print("HOSTS:")
  				print("        IP:"+add['ip'])
  				print("        MAC:"+add['mac'])
  				print("")
  		except:
  			print("")
  			pass
