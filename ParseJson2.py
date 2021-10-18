import ipaddress
import json
import re
from typing import List, Any
import psutil as ps

input_file=open('data_new.json', 'r')
json_decode=json.load(input_file)
ip_list = []
address_dic ={}
for item in json_decode['nmaprun']['host']:
        address_dic = item.get('address')
        if type(address_dic) is list:
         for address in address_dic:
            ipaddr = address['@addr']
            ip_list.append(ipaddr)
            print("The data structure is List and the IP List is:", ip_list)
        else:
            ip_list.append(address_dic['@addr'])
            print("The data structure is Dict and the type is dict:",ip_list)

