from data_structures import Stack


stack1 = Stack()

stack2 = Stack()


stack1.push(3)
stack1.push(6)
stack1.push(2)


stack2.push(3)
stack2.push(6)
stack2.push(2)

print(stack2 == stack1)
set1 = set()
set1.add(stack1)
set1.add(stack2)
print(set1)
