class LRUCache:

    def __init__(self, capacity: int):
        self.cash = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if(key not in self.cash):
            return -1
        self.cash.move_to_end(key)
        return self.cash[key]

    def put(self, key: int, value: int) -> None:
        if(key in self.cash):
            self.cash.move_to_end(key)
        self.cash[key] = value
        if(len(self.cash) > self.capacity):
            self.cash.popitem(last=False)
