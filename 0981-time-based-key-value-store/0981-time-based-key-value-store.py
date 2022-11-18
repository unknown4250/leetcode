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
        
        # key가 저장되어 있지 않은 경우
        if not val:
            return ''
        
        # 저장된 가장 큰 timestamp 보다 찾으려는 timestamp가 큰 경우
        if timestamp > val[-1][0]:
            return val[-1][1]
        
        # 저장된 가장 작은 timestamp 보다 찾으려는 timestamp가 작은 경우
        if timestamp < val[0][0]:
            return ''
        
        # 이진탐색
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