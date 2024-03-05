class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Create a queue of sports cars from the 1990s
cars_1990s_sports_queue = Queue()
cars_1990s_sports_queue.enqueue("Ferrari F355")
cars_1990s_sports_queue.enqueue("Porsche 911 (964)")
cars_1990s_sports_queue.enqueue("Dodge Viper RT/10")
cars_1990s_sports_queue.enqueue("Acura NSX")
cars_1990s_sports_queue.enqueue("Toyota Supra MKIV")
cars_1990s_sports_queue.enqueue("Mazda RX-7 FD")
cars_1990s_sports_queue.enqueue("Chevrolet Corvette C4 ZR-1")
cars_1990s_sports_queue.enqueue("Nissan 300ZX Z32")
cars_1990s_sports_queue.enqueue("BMW M3 E36")
cars_1990s_sports_queue.enqueue("Lotus Esprit V8")

# Display the queue contents by dequeueing each item
print("Cars from the 1990s sports queue:")
while not cars_1990s_sports_queue.is_empty():
    print(cars_1990s_sports_queue.dequeue())
