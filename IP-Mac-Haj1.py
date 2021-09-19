import os
import time
import threading
import json
import xmltodict
import networkx as nx
import matplotlib.pyplot as plt
import sys

def cmdcmd():
    os.popen("nmap -sP -PI -PT -oX /tmp/nmap_out.xml 10.94.208.4")

def xmltojson():
    with open("/tmp/nmap_out.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    xml_file.close()
    json_data = json.dumps(data_dict)

    with open("/tmp/nmap_data.json", "w") as json_file:
        json_file.write(json_data)

    json_file.close()

def make_graph():
    with open('nmap_out.json') as f:
        json_data = json.loads(f.read())

    G = nx.DiGraph()
    print(json_data['nmaprun']['host'])
    hosts = [elem['address']['@addr'] for elem in json_data['nmaprun']['host']]
    print(hosts)
    G.add_nodes_from(
        [elem['address']['@addr']
         for elem in json_data['nmaprun']['host']]
    )
    p = []
    for count, ip_add in enumerate(hosts):
        if count != len(hosts) - 1:
            p.append((ip_add, hosts[count + 1]))
            print(p)
    G.add_edges_from(p)

    #G.add_edges_from(
    #    (elem['from']['status'], elem['status'])
    #    for elem in json_data['host']
    #)
    nx.draw(
        G,
        with_labels=True
    )
    plt.savefig("testx1.png")
    plt.waitforbuttonpress()

make_graph()
sys.exit()

while True:
    #thread1 = threading.Thread(target=cmdcmd)
    #thread1.start()
    #print("Scanned IPs...")
    #thread1.join()
    #thread2 = threading.Thread(target=xmltojson)
    #thread2.start()
    #thread2.join()
    #print("Converted to json...")
    #time.sleep(15)
    thread3 = threading.Thread(target=make_graph)
    thread3.start()
    thread3.join()
    print("Converted to json...")

