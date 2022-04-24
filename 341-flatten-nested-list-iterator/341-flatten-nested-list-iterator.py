class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        
        for x in nestedList:
            if x.isInteger():
                self.list += x,
            else:
                self.list += NestedIterator(x.getList()),
        
        self.index = 0
                
    def next(self) -> int:
        if isinstance(self.list[self.index], NestedIterator):
            if not self.list[self.index].hasNext():
                self.index += 1
            
            return self.list[self.index].next()
        
        else:
            val = self.list[self.index]
            self.index += 1
            return val.getInteger()
        
        return self.list[self.index].next()
        
    
    def hasNext(self) -> bool:
        
        if self.index == len(self.list):
            return False
        
        if isinstance(self.list[self.index], NestedIterator):
            if not self.list[self.index].hasNext():
                self.index += 1
                return self.hasNext()
            else:
                return True
        
        else:
            return True