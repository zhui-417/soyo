from wenjian import open_r1,open_wj
from home import home
def login_your():
    your_name=open_r1('name.txt')
    your_number=open_r1('number.txt')
    for a in range(0,len(your_name)):
        your_name[a]=your_name[a].rstrip('\n')
    for b in range(0,len(your_number)):
        your_number[b]=your_number[b].rstrip('\n')
    data_1=[{'name1':your_name[a],'number1':your_number[b]}]  
      
    water=0
    water=str(water)
    print('欢迎来到登录系统\n'
          '*****请选择****\n'
          '***************\n'
          '****1.登录*****\n'
          '****2.注册*****\n')
    s=input('choose:')
    if s=='1':
        name_i=input('用户名：')
        number_i=input('密码')
        for data_2 in data_1:
            if data_2['name1'] == name_i and data_2['number1']==number_i:
                word=name_i+'登录成功'
                print(word)
                water=a
                home()
            else:
                print('用户名或密码错误')
                login_your()
    elif s=='2':
        print('即将开始注册')
        newname=input('请输入新的用户名：')
        newnumber=input('请输入密码')
        for data_2 in data_1:
            if data_2['name1']==newname:
                print('用户名已经存在')
                break
            else:
                open_wj('name.txt',newname)
                open_wj('number.txt',newnumber)
                print('注册成功')
                home()

                 
       
        
        