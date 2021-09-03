import textfsm
from pprint import pprint

template_file = "ex2_sh_int_status.template"
template = open(template_file) 

with open("show_interfaces_status.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()

entry = dict.fromkeys(re_table.header)
final_list = []


for item in data:
    entries = dict(zip(entry, item))
    final_list.append(entries)

pprint(final_list)
