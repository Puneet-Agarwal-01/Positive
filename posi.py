list = []
n = int(input("Enetr no. of elements in list:"))
for i in range(0,n):
    print("Enter",i+1,"element:", end='')
    ele = int(input())
    list.append(ele)
print("The positive elements in",list,"are: ", end='')
for i in list:
    if i>0:
        print(i, end='')
