import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, -item)

    def pop(self):
        if not self.is_empty():
            return -heapq.heappop(self.heap)
        else:
            return None

    def is_empty(self):
        return len(self.heap) == 0

# Create a max heap of sports cars from the 1990s
cars_1990s_sports_max_heap = MaxHeap()
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
    cars_1990s_sports_max_heap.push(len(car_model))

# Display the max heap contents by popping each item
print("Cars from the 1990s sports max heap (by length):")
while not cars_1990s_sports_max_heap.is_empty():
    print(cars_1990s_sports_max_heap.pop())
