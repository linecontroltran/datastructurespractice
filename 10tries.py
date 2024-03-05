class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Create a trie of sports cars from the 1990s
cars_1990s_sports_trie = Trie()
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

for car_model in cars_1990s_models:
    cars_1990s_sports_trie.insert(car_model)

# Search for specific sports car models
print("Search results in the 1990s sports car trie:")
print("Ferrari F355:", cars_1990s_sports_trie.search("Ferrari F355"))
print("Toyota Supra MKIV:", cars_1990s_sports_trie.search("Toyota Supra MKIV"))
print("Honda Civic:", cars_1990s_sports_trie.search("Honda Civic"))
