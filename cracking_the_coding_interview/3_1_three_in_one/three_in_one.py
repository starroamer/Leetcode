class TripleInOne:
    STACK_COUNT = 3
    
    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.array = [0] * self.STACK_COUNT * stackSize
        self.stackSizeList = [0] * self.STACK_COUNT

    def push(self, stackNum: int, value: int) -> None:
        index, elementCount = self.getStackTopIndex(stackNum)
        if elementCount < self.stackSize:
            self.array[index + 1] = value
            self.stackSizeList[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        index, elementCount = self.getStackTopIndex(stackNum)
        value = -1
        if elementCount > 0:
            value = self.array[index]
            self.stackSizeList[stackNum] -= 1
        return value

    def peek(self, stackNum: int) -> int:
        index, elementCount = self.getStackTopIndex(stackNum)
        value = -1
        if elementCount > 0:
            value = self.array[index]
        return value

    def isEmpty(self, stackNum: int) -> bool:
        _, elementCount = self.getStackTopIndex(stackNum)
        return elementCount == 0

    def getStackTopIndex(self, stackNum: int) -> bool:
        elementCount = self.stackSizeList[stackNum]
        index = stackNum * self.stackSize + elementCount - 1
        # print(f"index={index}, elementCount={elementCount}, array={self.array}, stackSizeList={self.stackSizeList}")
        return index, elementCount
    
        
if __name__   == "__main__":
    stackSize = 2
    obj = TripleInOne(stackSize)
    obj.push(0, 1)
    obj.push(0, 2)
    obj.push(0, 3)
    print(obj.pop(0))
    print(obj.pop(0))
    print(obj.pop(0))
    print(obj.peek(0))
    print(obj.isEmpty(0))