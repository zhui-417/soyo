from wenjian import open_r1,open_wj,open_wf
from home import home
def dele_book():
    print('提示，你只能删除未借出的书本')
    canlendbook=open_r1(r"canlend.txt")
    bookisdn=open_r1(r'bookisdn.txt')
    for b in range(0,len(canlendbook)):
      canlendbook[b]=canlendbook[b].rstrip("\n")
      bookisdn[b]=bookisdn[b].rstrip("\n")
      print(
         '1.通过书名删除\n'
         '2.通过书号删除\n'
      )
      s=input('请选择：')
      if s=="1":
         bookname=input('请输入书名：')
         for b in range(0,len(canlendbook)):
           if canlendbook[b] == bookname:
              print('确定要删除吗')
              print('确认请按Y')
              h=input('请确认Y/N')
              if h=='Y':
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
                     print('书本已经没有了')

                  for b in range(0,len(bookisdn)-1):
                     word_1=canlendbook[b+1]
                     word_2=bookisdn[b+1]
                     open_wj(r"canlend.txt",word_1)
                     open_wj(r'bookisdn.txt',word_2)
                  print("书已删除")
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
               print('确认要删除吗')
               h=input('请确认(Y/N)')
            if h=="Y":
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
                  print('书本已经没有了')
               
               for b in range(0,len(bookisdn)-1):
                  word_1=canlendbook[b+1]
                  word_2=bookisdn[b+1]
                  open_wj(r"canlend.txt",word_1)
                  open_wj(r'bookisdn.txt',word_2)
               print("书已删除")
               home()
               
            else:
               home()
         else:
            if b==len(bookisdn)-1:
               word='找不到书本'+bookname+'请检查拼写'
               print(word)
               home()


