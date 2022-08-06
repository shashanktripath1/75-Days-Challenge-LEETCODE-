class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        test=minutesToTest//minutesToDie
        i=0
        while((test+1)**i)<buckets:
            i+=1
        return i;
        