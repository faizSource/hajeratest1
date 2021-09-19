import os
import sys
import time
import threading
import json
import networkx as nx
import xmltodict
from matplotlib import pyplot as plt


def cmdcmd():
    os.popen("nmap -sP -PI -PT -oX nmap_out.xml 192.168.1.1/24")

def xmltojson():
    with open("nmap_out.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    xml_file.close()
    json_data = json.dumps(data_dict)

    with open("nmap_data.json", "w") as json_file:
        json_file.write(json_data)

    json_file.close()

def make_graph():
    with open('nmap_out.json') as f:
        json_data = json.loads(f.read())

    G = nx.DiGraph()
    G.add_nodes_from(
       [elem['address']['@addr']
         for elem in json_data['nmaprun']['host']]
    )
    #G.add_edges_from(
     #   (elem['address']['@addr'], elem['host'])
      #  for elem in json_data['nmaprun']['host']
     #)

    nx.draw(
        G,
        with_labels=True
    )
    plt.savefig("testx1.png")
    plt.waitforbuttonpress()

#make_graph()
#sys.exit()

while True:
    thread1 = threading.Thread(target=cmdcmd)
    thread1.start()
    print("Scanned IPs...")
    thread1.join()
    thread2 = threading.Thread(target=xmltojson)
    thread2.start()
    thread2.join()
    print("Converted to json...")
    time.sleep(15)
    thread3 = threading.Thread(target=make_graph)
    thread3.start()
    thread3.join()
    print("made graph..")
