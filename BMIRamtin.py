from tkinter import *
from tkinter import messagebox


def bmi():
    try:
        g = float(ghad.get())
        v = float(vazn.get())
    except:
        messagebox.showerror("خطا", "لطفا مقادیر خواسته شده را درست وارد کنید")
    try:
        n = v/(g*g)
        if n<18.5:
            messagebox.showinfo("کمبود وزن",(n,"شما دچار کمبود وزن هستید با تنظیم رژیم غذایی و ورزش به وزن ایده عال برسید."))
        elif 18.5<n<24.9:
            messagebox.showinfo("وزن طبیعی",(n,"تبریک میگوییم وزن شما ایده عال است"))
        elif 25<n<29.9:
            messagebox.showinfo("اضافه وزن",(n,"شما دارای اضافه وزن هستید وزن خود را کم کنید و توده بدنی خود را به 24 برسانید"))
        elif 30<n<34.9:
            messagebox.showinfo("چاق",(n,"شما دارای چاقی هستید وزن خود را به حد مناسب برسانید"))
        elif 35<n:
            messagebox.showinfo("خیلی چاق",(n,"شما خیلی چاق هستسد این چاقی میتواند بسیار خطرناک باشد وزن خود را بسیار کاهش دهید"))
    except:
        messagebox.showerror("خطا", "لطفا مقادیر خواسته شده را درست وارد کنید")

#window
window = Tk()
window.minsize(350,220)
window.resizable(width=False, height=False)
window.title("bmi")

#labelframe
lf = LabelFrame(window, text="مشخصات")
lf.pack(fill="both",expand="yes")

#ghad
Label(lf,text=":قد\n(بر حسب متر)").pack()
ghad=Entry(lf,width=45)
ghad.pack()

#fasele
Label(lf).pack()

#vazn
Label(lf,text=":وزن\n(برحسب کیلوگرم)").pack()
vazn=Entry(lf,width=45)
vazn.pack()

#fasele
Label(lf).pack()

#mohasebe
Button(lf,text="محاسبه کن",command=bmi).pack()


window.mainloop()