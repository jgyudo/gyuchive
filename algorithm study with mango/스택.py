#10828 스택
import sys
n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    a=sys.stdin.readline().split()
    
    if a[0]=='push':
        stack.append(a[1])
    elif a[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif a[0]=='size':
        print(len(stack))
    elif a[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])


#28278 스택2
import sys
n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    a=sys.stdin.readline().split()
    if a[0]=="1":
        stack.append(a[1])
    elif a[0]=="2":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif a[0]=="3":
        print(len(stack))
    elif a[0]=="4":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif a[0]=="5":
        if len(stack)==0:
            print(-1)
        else: 
            print(stack[-1])