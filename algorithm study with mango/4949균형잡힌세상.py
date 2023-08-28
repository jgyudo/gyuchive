a=input()

while a[0] != ".":  
    lst=[]
    for i in a:
        if i=="(" or i=="[":
            lst.append(i)
        elif i=="]":
            if len(lst)==0:
                lst.append(i)
                break
            elif lst[-1]=="[":
                lst.pop()
            else: 
                lst.append(i)
                break


        elif i==")":
            if len(lst)==0:
                lst.append(i)
                break
            elif lst[-1]=="(":
                lst.pop()
            else:
                lst.append(i)
                break

    if len(lst)==0:
        print("YES") 
    else: 
        print("NO")           
    a=input()

