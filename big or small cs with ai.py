def biggest():
    a=int(input("enter first no"))
    b=int(input("enter second no"))
    c=int(input("enter third no"))
    if(a>b)and(a>c):
        print("a is biggest")
    elif(b>a)and(b>c):
        print("b is biggest")
    else:
        print("c is biggest")
biggest()
