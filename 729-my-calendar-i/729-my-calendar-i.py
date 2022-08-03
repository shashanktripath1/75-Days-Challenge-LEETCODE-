class MyCalendar:
    def __init__(self):
        self.eventDates = []

    def book(self, start: int, end: int) -> bool:
        for laststart,lastend in self.eventDates:
            if laststart < end and start < lastend: 
                return False 
        self.eventDates.append((start,end))
        return True