class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        #this self.length is a counter, used for loop
        self.length = 0
        self.arr = [None] * capacity


    def get(self, i: int) -> int:
        #returns element at index i
        return self.arr[i]



    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]
  

    def resize(self) -> None:
        #doubles the capacity
        self.capacity = self.capacity * 2
        #creates new array with new size
        new_arr = [None] * self.capacity

        #copy over the old arr to new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        #below is powerful, erases the old array and adds the updated sized array to self.arr which every other function can now utilize
        self.arr = new_arr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
        
