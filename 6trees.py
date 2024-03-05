class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

# Create a binary search tree of sports cars from the 1990s
cars_1990s_sports_tree = None
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
    cars_1990s_sports_tree = insert(cars_1990s_sports_tree, car_model)

# Display the binary search tree contents using inorder traversal
print("Cars from the 1990s sports binary search tree:")
inorder_traversal(cars_1990s_sports_tree)
