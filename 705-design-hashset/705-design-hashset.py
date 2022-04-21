class MyHashSet:

    def __init__(self):
        self.hm=set()
        

    def add(self, key: int) -> None:
        self.hm.add(key)

    def remove(self, key: int) -> None:
        self.hm.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.hm


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)