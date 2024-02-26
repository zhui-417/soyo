from lend import lend_book
from return0 import return_book
from adds import add_book
from dels import dele_book
from home import home
from find import find_book
from login import login_your
s=home()
def Controls(s:str):
    if s == '1':
        lend_book()
    elif s == '2':
        return_book()
    elif s == '3':
        add_book()
    elif s == '4':
        dele_book()
    elif s =='5':
        find_book()
    elif s =='6':
        login_your()

    exit()
Controls(s)
