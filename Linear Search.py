# Linear Search

List = [2,4,1,9,12,15,16,20]
Find = int(input('Enter Number To Find: '))
Found = False

for count in range(0, len(List)):
    if List[count] == Find:
        count += 1
        print('Item Found on ' + str(count) + 'th search.')
        Found = True
        break

if Found == False:
    print('Item not found')
    
    
