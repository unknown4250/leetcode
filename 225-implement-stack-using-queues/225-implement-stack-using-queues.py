class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
        return None
        

    def pop(self):
        """
        :rtype: int
        """
        res = None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        if len(self.queue1) == 1:
            res = self.queue1.popleft()
            self.queue1, self.queue2 = self.queue2, self.queue1
        return res
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.queue1 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()