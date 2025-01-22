import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node("Router")
G.add_node("Switch") 
G.add_node("Device A")
G.add_node("Device B")
G.add_node("Device C")
G.add_edge("Router", "Switch") 
G.add_edge("Switch", "Device A")
G.add_edge("Switch", "Device B")
G.add_edge("Switch", "Device C")
layout = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos=layout, with_labels=True, node_size=3000,
        node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
plt.title("Simple Network Topology")
plt.show()
