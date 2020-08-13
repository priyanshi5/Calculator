from tkinter import *
#import tkinter.messagebox
#import parser


def btn_Click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

# Clear Function


def btn_ClearD(a):
    global operator
    operator = ""
    text_Input.set("")


def btn_Equ():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


cal = Tk()
cal.title("Calculator1")
cal.iconbitmap(r"C:\Users\HP\Desktop\Software\Calculator\calci.ico")
cal.resizable(width=False, height=False)
operator = ""
text_Input = StringVar()
cal.config(background="gold3")
txt_Display = Entry(cal, font='Arial 20 bold', textvariable=text_Input, bd=60,
                    insertwidth=4, bg="aquamarine3", justify='right').grid(columnspan=4)
btn1 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='1', command=lambda: btn_Click(1)).grid(row='1', column='0')
btn2 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='2', command=lambda: btn_Click(2)).grid(row='1', column='1')
btn3 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='3', command=lambda: btn_Click(3)).grid(row='1', column='2')
btn4 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='4', command=lambda: btn_Click(4)).grid(row='2', column='0')
btn5 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='5', command=lambda: btn_Click(5)).grid(row='2', column='1')
btn6 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='6', command=lambda: btn_Click(6)).grid(row='2', column='2')
btn7 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='7', command=lambda: btn_Click(7)).grid(row='3', column='0')
btn8 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='8', command=lambda: btn_Click(8)).grid(row='3', column='1')
btn9 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='9', command=lambda: btn_Click(9)).grid(row='3', column='2')
btn0 = Button(cal, bg="lightyellow", padx=16, pady=16, bd=20, fg='black',
              font='Arial 20 bold', text='0', command=lambda: btn_Click(0)).grid(row='4', column='1')
AC = Button(cal, bg="chocolate4", padx=16, pady=16, bd=20, fg='Red',  font='Arial 20 bold',
            text='C', command=lambda: btn_ClearD(0)).grid(row='4', column='0')
#Del = Button(cal,padx=16,pady=16,bd=20,fg='black',font='Arial 20 bold',text='D',command = clear_Entry).grid(row='4',column='1')
Equ = Button(cal, bg="maroon3",  padx=16, pady=16, bd=20, fg='black',
             font='Arial 20 bold', text='=', command=btn_Equ).grid(row='4', column='2')
Add = Button(cal, bg="orange",   padx=16, pady=16, bd=20, fg='black', font='Arial 20 bold',
             text='+', command=lambda: btn_Click("+")).grid(row='1', column='3')
Sub = Button(cal, bg="orange",   padx=16, pady=16, bd=20, fg='black', font='Arial 20 bold',
             text='- ', command=lambda: btn_Click("-")).grid(row='2', column='3')
Mul = Button(cal, bg="orange",   padx=16, pady=16, bd=20, fg='black', font='Arial 20 bold',
             text='* ', command=lambda: btn_Click("*")).grid(row='3', column='3')
Div = Button(cal, bg="orange",   padx=16, pady=16, bd=20, fg='black', font='Arial 20 bold',
             text='/ ', command=lambda: btn_Click("/")).grid(row='4', column='3')
cal.mainloop()