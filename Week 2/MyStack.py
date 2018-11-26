# Naam: Niels Risseeuw
# Studentnummer: 1721586
# Klas: V2C

class MyStack:

    # Init
    def __init__(self):
        self.List = list()

    # Adds parameter NewData to the stack
    def Push(self, NewData):
        self.List.append(NewData)

    # Removes value atop of MyStack
    def Pop(self):
        if len(self.List) > 0:
            Temp = self.List.pop()
            return Temp

    # Returns value atop MyStack
    def Peek(self):
        if len(self.List) > 0:
            return self.List[len(self.List)-1]

    # Returns if list is empty
    def IsEmpty(self):
        return len(self.List) == 0

Stack = MyStack()

# Test Cases            # Expected Outputs
#=========================================
print(Stack.Pop())      # None
print(Stack.Peek())     # None
Stack.Push('Test')
print(Stack.Peek())     # Test
Stack.Push('Best')
print(Stack.Pop())      # Best
print(Stack.Peek())     # Test
Stack.Pop()
print(Stack.IsEmpty())  # True
Stack.Push('Crest')
print(Stack.IsEmpty())  # False
