from wenjian import open_r1,open_wj,open_wf
from home import home
def lend_book():
  canlendbook=open_r1(r"canlend.txt")
  bookisdn=open_r1(r'bookisdn.txt')
  for b in range(0,len(canlendbook)):
    canlendbook[b]=canlendbook[b].rstrip("\n")
    bookisdn[b]=bookisdn[b].rstrip("\n")

    print(
          '***请选择***\n'
          '***1.查找书名\n'
          '***2.查找书号\n'
    )
    s=input('choose:')
    if s=="1":
      bookname=input('请输入书名：')
      for b in range(0,len(canlendbook)):
        if canlendbook[b] == bookname:
          print("成功查找到书本：",bookname)
          print("即将执行借书操作，确认后按Y")
          print("-----------------信息")
          print("书籍名称：",canlendbook[b])
          print("书籍编号：",bookisdn[b]) 
          s=input('请确认（Y/N）')
          if s=="Y":
            end_1=bookisdn[b]
            end_2=canlendbook[b]
            open_wj(r'isdn.txt',end_1)
            open_wj(r'lended.txt',end_2)
            canlendbook.pop(b)
            bookisdn.pop(b)
            try:
              word_1=canlendbook[0]
              word_2=bookisdn[0]
              open_wf(r"canlend.txt",word_1)
              open_wf(r'bookisdn.txt', word_2)
            except IndexError:
              open_wf(r'canlend.txt','')
              open_wf(r'bookisdn.txt','')
              print('书已经借完了')
              
            for b in range(0,len(bookisdn)-1):
              word_1=canlendbook[b+1]
              word_2=bookisdn[b+1]
              open_wj(r"canlend.txt",word_1)
              open_wj(r'bookisdn.txt',word_2)
            print("书已经借出")
            home()
            
          else:
            home()
        else:
          if b==len(canlendbook)-1:
            word="找不到书本"+bookname+",请检查拼写或此书已经借出"
            print(word)
            home()
            
    elif s=="2":
      findisdn=input('请输入编号')
      for b in range(0,len(bookisdn)):
        if bookisdn[b]==findisdn:
          print("成功查找到书本：",bookisdn)
          print("即将执行借书操作，确认后按Y")
          print("-----------------信息")
          print("书籍名称：",canlendbook[b])
          print("书籍编号：",bookisdn[b]) 
          s=input('请确认（Y/N）')
          if s=="Y":
              end_1=bookisdn[b]
              end_2=canlendbook[b]
              open_wj(r'isdn.txt',end_1)
              open_wj(r'lended.txt',end_2)
              canlendbook.pop(b)
              bookisdn.pop(b)
              try:
                word_1=canlendbook[0]
                word_2=bookisdn[0]
                open_wf(r"canlend.txt",word_1 )
                open_wf(r'bookisdn.txt', word_2)
              except IndexError:
                open_wf(r'canlend.txt','')
                open_wf(r'bookisdn.txt','')
                print('书已经借完了')
            
              for b in range(0,len(bookisdn)-1):
                word_1=canlendbook[b+1]
                word_2=bookisdn[b+1]
                open_wj(r"canlend.txt",word_1)
                open_wj(r'bookisdn.txt',word_2)
              print("书已经借出")
              home()
              
          else:
            home()
        else:
          if b==len(bookisdn)-1:
            word='找不到书本'+bookname+'请检查拼写'
            print(word)
            home()
            
