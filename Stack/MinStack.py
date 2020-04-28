class MinStack:
    # @param x, an integer
    # @return an integer
    arr=[]
    min_arr=[]
    def push(self, x):
        if self.min_arr[0]>x:
            self.min_arr.append(x)
        self.arr.append(x)
    # @return nothing
    def pop(self):
        if len(self.arr)==0:
            return
        pop_elemnt=self.arr.pop()
        if pop_elemnt==self.min_arr[0]:
            self.min_arr.pop()
        return pop_elemnt
    # @return an integer
    def top(self):
        if len(self.arr)==0:
            return -1
        return self.arr[0]
    # @return an integer
    def getMin(self):
        if len(self.min_arr)==0:
            return -1
        return self.min_arr[0]


s=MinStack()
s.push(1)
s.push(2)
s.push(-2)
print(s.getMin())

