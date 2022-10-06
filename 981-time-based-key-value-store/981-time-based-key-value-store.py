class TimeMap(object):
    def __init__(self):
        self.dic = defaultdict(deque)

    def set(self, key, value, timestamp):
        self.dic[key].appendleft((timestamp, value))	#O(1) time complexity

    def get(self, key, timestamp):
        if self.dic[key]:
            for tv in self.dic[key]:	#O(N) time complexity, N = len(the key)
                if tv[0] <= timestamp:
                    return tv[1]
        return ''