try:
    n=int(input("enter a value"))
    res=60/n
except zerodivisionerror:
    print("u have given 0 as the value.it is division by zero error")
else:
    print(res)
finally:
    print("bye")
