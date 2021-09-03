from pprint import pprint
import yaml
dev_list = []
dev_entry = {}

with open('lab_equip.txt') as f:
    for line in f:
        if '(' in line:
            dname = line.split()[0]
            dev_entry[dname] = {}
            dev_entry[dname]['device name'] = dname
        elif 'hostname' in line:
            hname = line.split()[-1]
            dev_entry[dname]["hostname"] = hname
        elif 'username' in line:
            usrname = line.split()[-1]
            dev_entry[dname]["username"] = usrname
        elif 'password' in line:
            passwd = line.split()[-1]
            dev_entry[dname]["password"] = passwd
        else:
            continue
    dev_list.append(dev_entry)
pprint(dev_list)
with open('lab_equip.yaml', 'w') as f:
    yaml.dump(dev_list,f,allow_unicode=True)

