def reverse( ):
    str1=input("Enter the string")
    print("Method-1")
    len1=len(str1)
    str2=''
    for i in range(len1):
        str2+=str1[len1-i-1]
    print(str2)
    print("Method-2")
    print(str1[::-1])
reverse()