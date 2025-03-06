# non optimal solution
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        self.queue = deque()

    def get(self, key: int) -> int:
        if key in self.cache: 
            #  update queue // dont use temp here -> use key
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]

        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key  in freq cache 
        if key in self.cache: 
            # remove 
            self.queue.remove(key)
        # else if capaccity at max
        elif self.capacity == len(self.queue):
            lru = self.queue.popleft()
            del self.cache[lru]
            # remove and update queue setructure 

        # insert new key val pair, update queue
        self.cache[key] = value 
        self.queue.append(key)
