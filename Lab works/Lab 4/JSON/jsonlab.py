import json as js

with open('json_sample_data.json', 'r') as jsFile:
    jsFile = js.load(jsFile)
    #print(js.dumps(jsFile, indent=2, sort_keys=True))

    for imdata in jsFile["imdata"]:
        print(imdata["l1PhysIf/attributes/dn"], imdata["speed"], imdata["mtu"])
#Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
"""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150
"""