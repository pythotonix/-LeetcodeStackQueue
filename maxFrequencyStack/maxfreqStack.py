from collections import deque
class FreqStack:

    def __init__(self):
        self.q=deque()
        self.dic={}

    def push(self, val: int) -> None:
        self.q.append(val)
        if val in self.dic:
            self.dic[val]+=1
        else:
            self.dic[val]=1

    def pop(self):
        max_freq = max(self.dic.values())
        i = len(self.q) - 1
        while i >= 0:
            top = self.q[i]
            if self.dic[top] == max_freq:
                self.dic[top] = self.dic[top] - 1
                el=self.q[i]
                self.q.reverse()
                self.q.remove(el)
                self.q.reverse()
                return el
            i = i - 1


freqStack = FreqStack()

freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.q)
print(freqStack.pop())
print(freqStack.q)
print(freqStack.pop())
print(freqStack.q)
print(freqStack.pop())
print(freqStack.q)
print(freqStack.pop())
freqStack.push(4)
print(freqStack.q)
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()