class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {', '.join(neighbors)}")

# Create a graph of sports cars from the 1990s
cars_1990s_sports_graph = Graph()
cars_1990s_models = [
    "Ferrari F355",
    "Porsche 911 (964)",
    "Dodge Viper RT/10",
    "Acura NSX",
    "Toyota Supra MKIV",
    "Mazda RX-7 FD",
    "Chevrolet Corvette C4 ZR-1",
    "Nissan 300ZX Z32",
    "BMW M3 E36",
    "Lotus Esprit V8"
]

cars_1990s_sports_graph.add_edge("Ferrari F355", "Porsche 911 (964)")
cars_1990s_sports_graph.add_edge("Ferrari F355", "Dodge Viper RT/10")
cars_1990s_sports_graph.add_edge("Porsche 911 (964)", "Acura NSX")
cars_1990s_sports_graph.add_edge("Porsche 911 (964)", "Toyota Supra MKIV")
cars_1990s_sports_graph.add_edge("Dodge Viper RT/10", "Mazda RX-7 FD")
cars_1990s_sports_graph.add_edge("Dodge Viper RT/10", "Chevrolet Corvette C4 ZR-1")
cars_1990s_sports_graph.add_edge("Acura NSX", "Nissan 300ZX Z32")
cars_1990s_sports_graph.add_edge("Toyota Supra MKIV", "BMW M3 E36")
cars_1990s_sports_graph.add_edge("Toyota Supra MKIV", "Lotus Esprit V8")

# Display the graph contents
print("Graph of sports cars from the 1990s:")
cars_1990s_sports_graph.display()
