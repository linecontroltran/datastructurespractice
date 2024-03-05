class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Create a stack of sports cars from the 1990s
cars_1990s_sports_stack = Stack()
cars_1990s_sports_stack.push("Ferrari F355")
cars_1990s_sports_stack.push("Porsche 911 (964)")
cars_1990s_sports_stack.push("Dodge Viper RT/10")
cars_1990s_sports_stack.push("Acura NSX")
cars_1990s_sports_stack.push("Toyota Supra MKIV")
cars_1990s_sports_stack.push("Mazda RX-7 FD")
cars_1990s_sports_stack.push("Chevrolet Corvette C4 ZR-1")
cars_1990s_sports_stack.push("Nissan 300ZX Z32")
cars_1990s_sports_stack.push("BMW M3 E36")
cars_1990s_sports_stack.push("Lotus Esprit V8")

# Display the stack contents by popping each item
print("Cars from the 1990s sports stack:")
while not cars_1990s_sports_stack.is_empty():
    print(cars_1990s_sports_stack.pop())
