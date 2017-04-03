from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")
    
count = 0
for map in crypto_map:
    crypto_child = crypto_map[count]
    count += 1
    print map.text
    for child in crypto_child.children:
        print child.text
