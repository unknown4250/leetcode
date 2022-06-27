class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.queue1 or (not self.queue1 and not self.queue2):
            self.queue1.append(x)
        else:
            self.queue2.append(x)
        return None
        

    def pop(self):
        """
        :rtype: int
        """
        if self.queue1:
            while self.queue1:
                self.queue2.append(self.queue1.popleft())
            return self.queue2.pop()
        else:
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
            return self.queue1.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.queue1:
            while self.queue1:
                self.queue2.append(self.queue1.popleft())
            return self.queue2[-1]
        else:
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
            return self.queue1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.queue1 or self.queue2 else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()