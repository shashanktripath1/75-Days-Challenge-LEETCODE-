class MyCalendar:

    def __init__(self):
        self.meet = []

    def book(self, start: int, end: int) -> bool:
        if not self.meet:
            self.meet.append([start, end])
            return True
        
        temp = self.meet.copy()
        temp.append([start, end])
        temp.sort(key = lambda i: i[0])
        for i in range(1, len(temp)):
            if temp[i][0] < temp[i-1][1]:
                return False
        
        self.meet = temp.copy()
        return True