#define all variables
while True:
    user = input('Input username')
    if user == 'stop':
        break
    pas = input('Input Password')
    if (user == 'admin') & (pas == 'admin'):
        print('Welcome')
        while True:
            print('*************************')
            print('Possible operations')
            print('01  Insert  foreigner\n02 View all foreigner\n03 Search foreigners\n04 Delete data\n05 Selling mode \n06 View Bills')
            x = input('Enter any operation code')
            if x == '01':
                insert()
            elif x == '02':
                view()
            elif x == '03':
                search()
            elif x == '09':
                break
            else:
                print('Invalid Opeartion code')
    elif (user == 'cashier') & (pas == '1234'):
        print('cashire')
    else:
        print('Invalid username or password')

