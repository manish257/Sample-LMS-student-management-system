#defien all functions here
Total_Student = []
def insert():
    Student=[]
    University_Name =input("Enter Your University_Name :")
    Student_Name=input("Enter your name:")
    Department =input("Enter Your Department Name :" )
    Section =input(" Enter Your Section:")
    Roll_No=input("Enter Your Roll No.:")
    Country_Name=input("Enter Your country Name:")
    Total_Student.append([University_Name,Student_Name,Department,Section,Roll_No,Country_Name])
    print('A foriegner  Details is inserted successfully')
def view():
    for Student_Detail in  Total_Student:
        for Student_Info in Student_Detail:
            print(Student_Info+'\t',end='')
        print('')
def search():
    templst = []
    x = input('Input anything to search')
    for Student_Detail  in  Total_Student:
        for Student_Info in Student_Detail:
            if Student_Info == x:
                templst.append(Total_Student)
    for Total_Student in templst:
        for Student_Info in Total_Student:
            print(Student_Info+'\t\t', end = '')
        print('')
        
#define all variables
#def insert():
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
