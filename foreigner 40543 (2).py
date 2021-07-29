q={}
count=0
z=student_number=int(input("Enter no of sts;"))
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
    q[e]=lst
    count+=1
file = open('forigner.txt','w')
q=str(q)
file.write(q)
file.close()
