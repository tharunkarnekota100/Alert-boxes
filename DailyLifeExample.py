from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title('Message Box')
main_window.iconbitmap('message.ico')

main_window.geometry('400x250')


def show_msg():

    res = messagebox.askquestion('this is a message box', 'Do You want to save the file?')
    if res=='yes':
        Label(main_window, text='file has been saved', font=('', 16)).pack(pady=(20, 0))
    else:
        messagebox.showwarning('this is a message box', 'Your File is trashed!')




Button(main_window, text="show message", font=('', 16), command=show_msg).pack(pady=(50, 0))  # pady=(x,y) x->upspace y->downspace


main_window.mainloop()
