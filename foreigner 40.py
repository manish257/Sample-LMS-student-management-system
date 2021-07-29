q=[]
count=0
z=student_number=int(input(";"))
while count <z:
    lst=[]
    a=country_name =input("country:")
    b=niversity_name =input("university:")
    c=student_name =input("name:")
    d=section=input("section:")
    e=student_roll_no=int(input("Roll No.:"))
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)
    lst.append(e)
    q.append(lst)
    count+=1
file = open('next forigner.txt','w')
q=str(q)
file.write(q)
file.close()
