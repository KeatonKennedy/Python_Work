# Binary Search

List = [10,20,30,40,50,60,70,80,90,100]
low, high = 0, len(List)
Found = False

find = int(input('Enter Number To Find: '))
    
while low <= high:
    mid = (high + low) // 2
    if find > List[len(List) - 1]:
        print('Item Not Found')
        Found = True
        break
    elif List[mid] == find:
        print('Item Found')
        Found = True
        break
    elif List[mid] < find:
        low = mid + 1
    else:
        high = mid - 1

if Found == False:
    print('Item Not Found')
