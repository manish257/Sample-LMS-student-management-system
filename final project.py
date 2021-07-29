#This Program is about the information of the foreign students in any university.
#you can insert,view,search,delete,count the student details.
Total_Student = []

#function is defined to insert data:
def insert():
    University_Name =input("Enter University Name of the Student :")
    Student_Name=input("Enter Name of the Student :")
    Department =input("Enter Department of the Student :" )
    Section =input("Enter Section of the Student :")
    Roll_No=input("Enter Roll Number of the Student:")
    Age=input("Enter Age of the Student:")
    Country=input("Enter Your Country of the Student:")
    Total_Student.append([University_Name,Student_Name,Department,Section,Roll_No,Age,Country])
    print('A foriegner  detail is INSERTED successfully!')

#function is defined to view all data:   
def view():
    print('~~~~'+'\t'+'~~~~~~'+'\t'+'~~~~~'+'\t'+'~~'+'\t'+'~~~'+'\t'+'~~~'+'\t'+'~~~~~~~~')
    print('Univ'+'\t'+'Name'+'\t'+'Depart'+'\t'+'Sec'+'\t'+'Roll'+'\t'+'Age'+'\t'+'Country')
    print('----'+'\t'+'-----'+'\t'+'------'+'\t'+'--'+'\t'+'---'+'\t'+'----'+'\t'+'--------')
    for Student_Detail in  Total_Student:
        for Student_Info in Student_Detail:
            z=Student_Info.upper()
            print(z+'\t',end='')
        print('')
    print('~~~~'+'\t'+'~~~~~~'+'\t'+'~~~~~'+'\t'+'~~'+'\t'+'~~~'+'\t'+'~~~'+'\t'+'~~~~~~~')
        
#function is defined to search individual data:        
def search():
    templst = []
    x = input('Input anything to search')
    for Student_Detail  in  Total_Student:
        for Student_Info in Student_Detail:
            if Student_Info == x:
                templst.append(Student_Detail)
    print('~~~~'+'\t'+'~~~~~~'+'\t'+'~~~~~'+'\t'+'~~'+'\t'+'~~~'+'\t'+'~~~'+'\t'+'~~~~~~~~')
    print('Univ'+'\t'+'Name'+'\t'+'Depart'+'\t'+'Sec'+'\t'+'Roll'+'\t'+'Age'+'\t'+'Country')
    print('----'+'\t'+'-----'+'\t'+'------'+'\t'+'--'+'\t'+'---'+'\t'+'----'+'\t'+'--------')
    for Student_Detail in templst:
        for Student_Info in Student_Detail:
            z=Student_Info.upper()
            print(z+'\t',end='')
        print('')
    print('~~~~'+'\t'+'~~~~~~'+'\t'+'~~~~~'+'\t'+'~~'+'\t'+'~~~'+'\t'+'~~~'+'\t'+'~~~~~~~')
        
#function is defined to delete data of any student:        
def delete():
    x = input('Input anything to search')
    for Student_Detail  in  Total_Student:
        for Student_Info in Student_Detail:
            if Student_Info == x:
                Total_Student.remove(Student_Detail)
    print('A foriegner  details is DELETED successfully')

#function is defined to count the number of students:
def count():
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print('Total no. of students is:',len(Total_Student))
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

#function is defined to edit data of any foreigner:
def edit():
    print('The provision is that you must re-enter all the remaining')
    print('student information along with information you want to edit.')
    x = input('Input anything to search')
    for Student_Detail  in  Total_Student:
        for Student_Info in Student_Detail:
            if Student_Info == x:
                Total_Student.remove(Student_Detail)
    University_Name =input("Enter University Name of the Student :")
    Student_Name=input("Enter Name of the Student :")
    Department =input("Enter Department of the Student :" )
    Section =input("Enter Section of the Student :")
    Roll_No=input("Enter Roll Number of the Student:")
    Age=input("Enter Age of the Student:")
    Country=input("Enter Your Country of the Student:")
    Total_Student.append([University_Name,Student_Name,Department,Section,Roll_No,Age,Country])
    print('A foriegner  detail is EDITED successfully!!')
    
#When the program is started it asks for the user login:
while True:
    
    if True:
        user = input('Please specify your username :')
        if user == 'stop':
            print('_______THANKS YOU______')
            break
        pas = input('Please input your password :')
    
    #login for vc:    
        if (user == 'vc') & (pas == 'vc'):
            print('warm welcome to respected vc of the university')
            while True:
                print('******************************************')
                print('******************************************')
                print('*********Foreigner Student Details********')
                print('******************************************')
                print('******************************************')
                print('Please choose your Desired Operation:')
                print('a Insert Foreigner\nb View all Foreigners\nc Total number of foreigners\nd Search Foreigner\ne Delete Foreigner\nf Edit Foreigner\ng EXIT')
                x = input('Please enter your desired operation code:')
                if x == 'a':
                    insert()
                elif x == 'b':
                    view()
                elif x == 'c':
                    count()
                elif x == 'd':
                    search()
                elif x == 'e':
                    delete()
                elif x=='f':
                    edit()
                elif x=='g':
                    print('_______THANKS YOU______')
                    break
                else:
                    print('Invalid Opeartion code')
                    print('PLEASE TRY AGAIN')
                
        #login for studenthead:
        elif (user == 'studenthead') & (pas == 'studenthead'):
            print('welcome')
            while True:
                print('******************************************')
                print('******************************************')
                print('*********Foreigner Student Details********')
                print('******************************************')
                print('******************************************')
                print('Please choose your Desired Operation:')
                print('a Insert Foreigner\nb View all Foreigners\nc Total number of foreigners\nd Search Foreigner\ne Delete Foreigner\nf Edit Foreigner\ng EXIT')
                x = input('Please enter your desired operation code:')
                if x == 'a':
                    insert()
                elif x == 'b':
                    view()
                elif x == 'c':
                    count()
                elif x == 'd':
                    search()
                elif x == 'e':
                    delete()
                elif x=='f':
                    edit()
                elif x=='g':
                    print('_______THANKS YOU______')
                    break
                else:
                    print('Invalid Opeartion code')
                    print('PLEASE TRY AGAIN')
                
    #login for foreigner student:
        elif (user == 'foreigner') & (pas == 'foreigner'):
            print('Welcome')
            while True:
                print('******************************************')
                print('******************************************')
                print('*********Foreigner Student Details********')
                print('******************************************')
                print('******************************************')
                print('Please choose your Desired Operation:')
                print('a Insert Foreigner\nb View all Foreigners\nc Total number of foreigners\nd Search Foreigner\ne EXIT')
                x = input('Please enter your desired operation code:')
                if x == 'a':
                    insert()
                elif x == 'b':
                    view()
                elif x == 'c':
                    count()
                elif x == 'd':
                    search()
                elif x == 'e':
                    print('_______THANKS YOU______')
                    break
                else:
                    print('Invalid Opeartion code')
                    print('PLEASE TRY AGAIN')
                
    #login for outsider:
        elif (user == 'outsider') & (pas == 'outsider'):
            print('Welcome')
            while True:
                print('******************************************')
                print('******************************************')
                print('*********Foreigner Student Details********')
                print('******************************************')
                print('******************************************')
                print('Please choose your Desired Operation:')
                print('a Insert Foreigner\nb Search Foreigner\nc For EXIT')
                x = input('Please enter your desired operation code:')
                if x == 'a':
                    insert()
                elif x == 'b':
                    search()
                elif x == 'c':
                    print('_______THANKS YOU______')
                    break
                else:
                    print('Invalid Opeartion code')
                    print('PLEASE TRY AGAIN')
    #login for editor:
        elif(user == 'editor') & (pas == 'editor'):
            print('Welcome')
            while True:
                print('******************************************')
                print('Please choose your Desired Operation Code:')
                print('a Insert Foreigner\nb View all Foreigners\nc Edit Foreigner\nd EXIT  ')
                x = input('Please enter your desired operation code:')
                if x == 'a':
                    insert()
                elif x == 'b':
                    view()
                elif x == 'c':
                    edit()
                elif x == 'd':
                    print('_______THANK YOU______')
                    break
                else:
                    print('Invalid Opeartion code')
                    print('PLEASE TRY AGAIN')
        else:#if user give wrong user name of password
            print('Invalid username or password')
            print('PLEASE TRY AGAIN')
