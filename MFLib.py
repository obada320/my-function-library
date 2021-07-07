def simple1(Start,End,Step,str1):
    for i in range(Start,End,Step):
        print(str1)

def simple2(Start,End,Step):
    for i in range(Start,End,Step):
        print(i)

def simple3(int1,int3):
    i = 0
    while int1 >= int3:
        print(i)
    i += 1

def simple4(int1,int2,str1):
    i = 0
    while int1 <= int2:
        print(str1)
    i += 1

def write1(*str1):
    for i in str1:
        print(str1)

def write2(str1 = 'None'):
    print(str1)

def write3(str1 = 'None',str2 = 'None'):
    print(str1,str2,)

def write4(str1 = 'None',str2 = 'None',str3 = 'None'):
    print(str1,str2,str3)

def write5(str1 = 'None',str2 = 'None',str3 = 'None'):
    print(str1,str2,str3)

def write(*str1):
    print(str1)

def Character(name = 'Not imported',nickname = 'Not imported',age = 'Not imported',country = 'Not imported'):
    print('Hello',name,'your Age is :')
    print(age)
    print('And your Nickname is :')
    print(nickname)
    print('And your Country is:')
    print(country)


def user(User = 'Unown',Nickname = 'No Nickname',first = 'Unown',middel = 'Unown',end = 'Unown',age = 'Unown',mail = 'No Mail',password = 'No Password',Country = 'No Country',Region = 'No imported',Family_Name = 'No Family',family_surname = 'No Family surname'):
    print('Hello',User)
    print('your Nickname is:',Nickname)
    print('your first name is:',first)
    print('your middel name is:',middel)
    print('your last name is:',end)
    print('you are is:',age)
    print('your mail is:',mail)
    print('re enter your Password to contnue' )
    password2 = input('Re Enter your password')
    if password2 == password:
        print(password)
    else:
        exit()
    print(Country)
    print(Region)
    print(Family_Name)
    print(family_surname)

