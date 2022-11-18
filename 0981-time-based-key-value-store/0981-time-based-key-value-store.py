class TimeMap(object):

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        
        val = self.map[key]
        
        if not val:
            return ''
        
        if timestamp > val[-1][0]:
            return val[-1][1]
        
        if timestamp < val[0][0]:
            return ''
        
        left, right = 0, len(val) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if val[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
    
        return val[left][1] if left < len(val) - 1 else val[right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)