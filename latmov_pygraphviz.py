import csv
import pyvis.network as net

# Read the CSV file
connections = []
with open('connections.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    for row in reader:
        connections.append(row)

# Initialize the graph
G = net.Network(notebook=True,directed=True, select_menu=True, cdn_resources='remote')
G.show_buttons()

# Add the nodes to the graph
for connection in connections:
    source_hostname = connection[0]
    destination_hostname = connection[1]
    G.add_node(source_hostname, shape='image', image=connection[3], label=source_hostname)
    G.add_node(destination_hostname, shape='image', image=connection[4], label=destination_hostname)

# Add the edges to the graph
for connection in connections:
    source_hostname = connection[0]
    destination_hostname = connection[1]
    username = connection[2]
    G.add_edge(source_hostname, destination_hostname, label=username, arrow=True)

# Draw the graph
G.show("lateral_movement.html")
