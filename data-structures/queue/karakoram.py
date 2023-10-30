class Queue:
    def __init__(self, capacity):
        self.arr = []
        self.capacity = capacity
    def __repr__(self):
        out = ""
        for i in self.arr:
            out += str(i) + " "
        return out
    def enqueue(self,data):
        if self.isFull() is True:
            print("Full Queue")
            return
        else:
            print("Added to Queue:", data)
            self.arr.append(data)
    def dequeue(self):
        if self.isEmpty() is True:
            print("Empty Queue")
            return
        else:
           data = self.arr[0]
           print("Dequeue:", data)
           self.arr.pop(0)
           return data

    def isEmpty(self):
        return 0 == len(self.arr)
    def isFull(self):
        return self.capacity == len(self.arr)
    def size(self):
        return len(self.arr)

def main():
    q = Queue(100)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(4)
    print(q)
    karakoram = Queue(100)
    karakoram.enqueue("Swat Valley")
    karakoram.enqueue("K2")
    karakoram.enqueue("Broad Peak - K3")
    karakoram.enqueue("Gasherbrum I - Hidden Peak - K4")
    karakoram.enqueue("Gasherbrum II - K5")
    karakoram.enqueue("Nanga Parbat")
    karakoram.dequeue()

    himalaya = Queue(100)
    himalaya.enqueue("Everest - Sagarmatha(Nepal name)")
    himalaya.enqueue("Annapurna")
    himalaya.enqueue("Kangchenjunga")
    himalaya.enqueue("Shishapangma")
    himalaya.enqueue("Makalu")
    himalaya.enqueue("Lhotse")
    himalaya.enqueue("Manaslu")
    himalaya.enqueue("Dhaulagiri")
    himalaya.enqueue("Cho Oyu")
    print(karakoram)
    print(himalaya)
main()
