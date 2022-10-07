class MyCalendarThree:

    def __init__(self):
        self.events = []
        self.max = 0
        self.records = []
    def book(self, start: int, end: int) -> int:
        i = bisect_right(self.events,start,key=lambda x:x[0])
        self.events.insert(i,(start,1))
        self.records.insert(i,1)
        j = bisect_left(self.events,end,key=lambda x:x[0])
        self.events.insert(j,(end,-1))
        self.records.insert(j,0)
        if i-1 >= 0:
            self.records[i] = self.records[i-1] + 1
        self.max = max(self.max,self.records[i])
        for k in range(i+1,j+1):
            self.records[k] = self.records[k-1] + self.events[k][1]
            self.max = max(self.max,self.records[k])
        return self.max