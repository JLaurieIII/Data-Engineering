a = int(input("How many elements are in your list?"))
list = []

for i in range(a):
    num = int(input("Enter number:"))
    list.insert(a, num)

b = int(input("How many rotations do you want?"))


def rotate_list(ls, k):
    
    for i in range(k):
        last = ls[-1]
        ls.pop()
        ls.insert(0, last)

    return ls

print(rotate_list(list,b))


# Check for descending order list

def isDescending(list):
    
    bool = True

    for i in range(0, len(list) - 1):
        if list[i] < list[i + 1]:
            bool = False;
    return bool        

print(isDescending(list))