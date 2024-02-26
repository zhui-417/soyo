from wenjian import open_wj
from home import home
def add_book():
    print('欢迎添加图书')
    a_name=input('请输入书本名称\n')
    a_isdn=input('请输入isdn编号\n')
    word_1=a_name
    word_2=a_isdn
    open_wj(r"canlend.txt",word_1)
    open_wj(r'bookisdn.txt',word_2)
    print(
        '*************\n'
        '**1.继续添加**\n'
        '**2.退出添加**\n'
        '*************\n'
    )
    s=input('choose:')
    if s=="1":
        add_book()
    elif s=="2":
        home()

        