# Program a stack of integers. The stack should be implemented by using arrays.


a = int(input())  

for _ in range(a):
    n, s = map(int, input().split())  
    stack = []
    for _ in range(n):
        command = input().split()
        if command[0] == "push":
            value = int(command[1])
            if len(stack) >= s:
                print("stack overflow")
            else:
                stack.append(value)
        elif command[0] == "pop":
            if not stack:
                print("stack underflow")
            else:
                print(stack.pop())
        elif command[0] == "top":
            if not stack:
                print("stack underflow")
            else:
                print(stack[-1])