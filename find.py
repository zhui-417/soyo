from wenjian import open_r1 
from home import home
def find_book():
    print(
        "查询未借出书籍请按1\n"
        '查询已经借出籍名称请按2\n'
    )
    s=input('choose')
    if s=="1":
        h=open_r1(r"canlend.txt")
        j=open_r1(r'bookisdn.txt')
        print('未借出的书本')
        print(h,j)
        home()
    elif s=="2":
        i=open_r1(r'lended.txt')
        k=open_r1(r'isdn.txt')
        print('已经借出的书本')
        print(i,k)
        home()

    
    
        
