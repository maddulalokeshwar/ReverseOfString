def duplicates(l1):
    output=[]
    for i in l1:
        if i not in output:
            output.append(i)
    return output
n=int(input("Enter size of array: "))
l1=[]
for i in range(n):
    l1.append(int(input()))
l1=duplicates(l1)
print(l1)
