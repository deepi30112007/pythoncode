l=[12,45,7,23,89,3,56]
max=min=l[0]
for i in l:
    if(i>max):
        max=i
    if(i<min):
        min=i
print("max:",max)
print("min:",min)



l=[1,2,1,4,6,7,6,5,6,1,2]
print("occurrences of 6:",l.count(6))
print("occurrences of 1:",l.count(1))
print("occurrences of 2:",l.count(2))


l=[7,40,5,6,8,2,89,90]
l.sort()
print("ascending:",l)
l.sort(reverse="true")
print("descending:",l)
