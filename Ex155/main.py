class MinStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        min=self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i]<min:
                min=self.stack[i]
        return min