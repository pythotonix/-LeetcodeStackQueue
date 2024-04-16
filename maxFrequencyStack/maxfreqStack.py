from collections import deque
class FreqStack:

    def __init__(self):
        self.q=deque()

    def push(self, val: int) -> None:
        self.q.appendleft(val)

    def pop(self) -> int:
        maxfreq_item=0
        maxfreq=0
        self.q=self.q
        set_q=set(self.q)
        for el in set_q:
            # print(el)
            if self.q.count(el)>maxfreq:
                maxfreq=self.q.count(el)
                maxfreq_item=el
                n=self.q.index(el)
                # print(f'{maxfreq_item=}')
            elif self.q.count(el)==maxfreq:
                if self.q.index(el)<self.q.index(maxfreq_item):
                    maxfreq_item=el
                    n=self.q.index(el)
                    # print(f'{maxfreq_item=}')
        # a=deque(reversed(self.q))
        self.q.remove(maxfreq_item)
        # self.q.rotate(-n)
        # print(f"before popping {self.q=}")
        # # self.q.remove(maxfreq_item)
        # self.q.pop()
        # self.q.rotate(-n)
        return maxfreq_item


freqStack = FreqStack()

freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(set(freqStack.q))
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