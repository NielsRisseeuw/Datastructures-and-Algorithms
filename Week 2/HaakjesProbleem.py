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

    # Returns value atop of MyStack
    def Peek(self):
        if len(self.List) > 0:
            return self.List[len(self.List)-1]

    # Returns if list is empty
    def IsEmpty(self):
        return len(self.List) == 0


def VerifyParentheses(Parentheses):
    assert isinstance(Parentheses, str), 'Error: Parameter 1 is not of type String, String expected'
    Stack = MyStack()

    for Index in range(0, len(Parentheses)):
        if Parentheses[Index] == '(' or Parentheses[Index] == '<' or Parentheses[Index] == '[':
            Stack.Push(Parentheses[Index])
        if Parentheses[Index] == ')' or Parentheses[Index] == '>' or Parentheses[Index] == ']':
            if Stack.Peek() == '(' and Parentheses[Index] == ')':
                Stack.Pop()
            elif Stack.Peek() == '[' and Parentheses[Index] == ']':
                Stack.Pop()
            elif Stack.Peek() == '<' and Parentheses[Index] == '>':
                Stack.Pop()
            else:
                return False

    return Stack.IsEmpty()


# Test Case 1: True
Parentheses = '([<>])'
print(VerifyParentheses(Parentheses))

# Test Case 2: False
Parentheses = '([)]'
print(VerifyParentheses(Parentheses))

# Test Case 3: True
Parentheses = '((<>))[](())'
print(VerifyParentheses(Parentheses))

# Test Case 4: False
Parentheses = '((( < ) >))'
print(VerifyParentheses(Parentheses))

# Test Case 5: True
Parentheses = '((<>)())'
print(VerifyParentheses(Parentheses))
