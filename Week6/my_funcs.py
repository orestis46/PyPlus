import yaml
from getpass import getpass


def load_device(filename):
    with open(filename) as f:
        devices = yaml.safe_load(f)

    device = devices['arista4']
    device['password'] = getpass()
    return device



def print_output(arp_entries):
    for entry in arp_entries:
        mac = entry['hwAddress']
        ipv4 = entry['address']
        print(f'{mac} --> {ipv4}')

def print_output_routes(routes):
    for key, value in routes.items():
        route_type = value['routeType']
#        print(key, route_type)
        if route_type == 'connected':
            print(f'{key}, {route_type}, via {value["vias"][0]["interface"]}')
        elif route_type == 'static':
            print(f'{key}, {route_type}, via {value["vias"][0]["nexthopAddr"]}') 

        
