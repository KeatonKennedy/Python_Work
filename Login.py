def Login():
    Name = input('Enter Name: ')
    Pass = input('Enter Password: ')
    f = open('Login.txt','r')
    x = f.read()
    Users = x.split('\n')
    print(Users)
    if Users[0] == Name and Users[1] == Pass:
        print('Worked')
        
Login()
