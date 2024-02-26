from time import sleep
def home():
    while 1:
        for i in range(51):
            print('\r加载进度: [%-50s]%.2f%% '%('#'*i,i*2),end='')
            sleep(0.05)
        print('\n加载完毕!','\a')
        break
    print(
        '****欢迎使用图书管理系统***\n'
        '****     请选择        ***\n'
        '****1.借书       2.还书***\n'
        '****3.添加图书 4.删除图书**\n'
        '****5.查询所有图书*********\n'
        '****6.登录/注册你的系统*****\n'
        )
    s=input("请选择：")
    
    return s
      