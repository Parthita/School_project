import mysql.connector as c
from datetime import datetime
myc=c.connect(host="localhost",user="root",passwd="",database="user_database")
cursor=myc.cursor()
print("Welcome to XYZ")
def entry():
    print("If you are a new user enter 0")
    print("If you are a existing user enter 1")
    new_old_user = int(input("Enter the number:"))
    if new_old_user == 0:
        new_entry()
    elif new_old_user == 1:
        old_entry_name()
    else:
        print("Enter a valid number")
        entry()
def old_entry_name():
    old_entry_name.old_name= input("Please enter your name:")
    cursor.execute("select name from user_data")
    name = cursor.fetchall()
    on=1
    for check_name in name:
        if old_entry_name.old_name== check_name[0]:
            print("User Found")
            old_password_entry()
            on=0
            break
    if on==1:
        print("User not found")
        old_entry_name()
def old_password_entry():
    old_password = input("Please enter your password:")
    cp="select password from user_data where name=(%s)"
    cn=old_entry_name.old_name
    cursor.execute(cp,(cn,))
    password = cursor.fetchall()
    for check_password in password:
        old_password_entry.op=1

        for j in range(len(password)):
            if old_password==check_password[0]:
                print("Correct Password")
                time_calc()
                break
            elif old_password_entry.op==1:
                print("Wrong Password")
                old_password_entry()
        break
def new_entry():

    new_name = input("Please enter your name")
    cursor.execute("select name from user_data")
    name = cursor.fetchall()
    nc=1
    namel=[]
    while nc==1:
        for check_name in name:
            namel.append(check_name[0])

        if new_name in namel:
            print("Username already there enter a new name ")
            new_name = input("Please enter your name")
        else:
            nc=0
            break
    new_password = input("Please enter your password")
    new_time=int(input("How much time you want to study"))
    new_et=int(input("Jei time a entry korbe"))
    ep_1 = "INSERT INTO user_data (Name,Password,study_time,entry_time) VALUES (%s,%s,%s,%s)"
    ep_2 = (new_name, new_password,new_time,new_et)
    cursor.execute(ep_1, ep_2)
    myc.commit()
    print("you account has been created now relogin")
    old_entry_name()
def time_calc():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    a = int(current_time[0])
    b = int(current_time[1])
    c = 10 * a + b
    cet = ("Select entry_time from user_data where name=(%s)")
    cursor.execute(cet, (old_entry_name.old_name,))
    et = cursor.fetchall()
    for abd in et:
        timeet=abd[0]
    if timeet==c or timeet>c:
        a = int(input("Hello User how much time u studied today?:"))
        ct = ("Select study_time from user_data where name=(%s)")
        cursor.execute(ct, (old_entry_name.old_name,))
        time = cursor.fetchall()
        for abc in time:
            timec = abc[0]
        if a < timec:
            print("You studied ", timec - a, "hours less today")
        elif a > timec:
            print("You studied ", a - timec, "hours less today")
            print("Studying more is not bad")
        elif a == timec:
            print("Congratssss!!!!! ")
            print("You satisfied your schedule today")
    else:
        if timeet<c:
            print("You are ",c-timeet,"hours early than your data entering time that you gave")

entry()















