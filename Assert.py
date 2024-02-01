def calculate_rectangle_area(length, width):
    assert length != width, 'Length & Width Can Not Equal Each Other. That is a square.' 
    assert (length and width) > 0, 'Length & Width Must Be Positive.'
    return length * width

length = int(input("Enter Length: "))
width = int(input("Enter Width: "))
x = calculate_rectangle_area(length, width)
print(x)

def search_in_list(my_list, target):
    assert my_list != [], 'List is Empty.'
    count = 0
    for item in my_list:
        if item == target:
            return True
        else:
            count += 1
            if count == len(my_list):
                return False

my_list = ['8','45','10','71','24','37']
# my_list = []
target = input('Enter Number To Search: ')
x = search_in_list(my_list, target)
print(x)