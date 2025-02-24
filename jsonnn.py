import json

# Load the JSON data from the file
with open('sample-data.json') as file:
    data = json.load(file)

# Print the header
print("Interface Status")
print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-" * 50)

# Iterate through the interfaces and print the required information
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes.get('descr', '')  # Default to empty if no description
    speed = attributes['speed']
    mtu = attributes['mtu']
    
    print(f"{dn:<50} {description:<20} {speed:<6} {mtu}")