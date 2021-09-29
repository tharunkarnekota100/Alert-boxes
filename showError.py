from tkinter import *
from tkinter import messagebox

main_window=Tk()
main_window.title('Message Box')
main_window.iconbitmap('message.ico')

main_window.geometry('400x250')

def show_msg():
   #messagebox.showerror('this is a message box','Telugu Computer World')

   res = messagebox.showerror('this is a message box', 'Telugu Computer World')
   Label(main_window, text=res, font=('', 16)).pack(pady=(20, 0))


Button(main_window,text="show message", font=('',16), command=show_msg).pack(pady=(50,0))    #pady=(x,y) x->upspace y->downspace

main_window.mainloop()