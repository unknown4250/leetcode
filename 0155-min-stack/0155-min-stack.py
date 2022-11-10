class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_val = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_val or self.min_val[-1] >= val:
            self.min_val.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        n = self.stack.pop()
        
        if self.min_val[-1] == n:
            self.min_val.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_val:
            return None
        else:
            return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()