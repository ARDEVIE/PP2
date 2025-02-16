import json

with open(r'C:\Users\DMR\Documents\PP2\Lab4\json\s.json', 'r') as file:
    data = json.load(file)

interfaces = data.get('imdata', [])

# Print the header
print("Interface Status")
print("=" * 90)
print(f"{'DN':<55} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 80)

# Iterate through the interfaces and print relevant details
for item in interfaces:
    attributes = item.get('l1PhysIf', {}).get('attributes', {})
    dn = attributes.get('dn', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    
    print(f"{dn:<55} {'':<20} {speed:<7} {mtu:<5}")
