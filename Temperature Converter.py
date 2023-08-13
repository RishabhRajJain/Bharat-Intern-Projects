from tkinter import *
root = Tk()
root.geometry("585x333")
root.minsize(width= 585, height=333)
root.maxsize(width= 585, height=333)
root.title("Temperature Converter - RRJ")
root.wm_iconbitmap("Temp.ico")
root.configure(background="cadetblue3")


# Temperature conversion
def convert(event):
    global t
    text1= click1.get()
    tp1= temp1.get()
    if tp1.isdigit():
        if text1 == "Celsius" and text2 == "Fahrenheit":
            t = float((float(tp1) * 9 / 5) + 32)
            t2.set(t)
        if text1 == "Fahrenheit" and text2 == "Celsius":
            t = float((float(tp1) - 32) * 5 / 9)
            t2.set(t)
        if text1 == "Fahrenheit" and text2 == "Kelvin":
            t = float((float(tp1) - 32) * 5 / 9) + 273.15
            t2.set(t)
        if text1 == "Celsius" and text2 == "Kelvin":
            t = float(tp1) + 273.15
            t2.set(t)
        if text1 == "Kelvin" and text2 == "Celsius":
            t = float(tp1) - 273.15
            t2.set(t)
        if text1 == "Kelvin" and text2 == "Fahrenheit":
            t = float((float(tp1) - 273.15) * 1.8 + 32)
            t2.set(t)
    temp2.update()
t1= StringVar()
t1.set("")
text1= Label(root, text="Enter the Temperature", font="oswald 30 bold", bg="cadetblue3", fg="cornsilk")
text1.grid(padx= 10,pady= 20)
f= Frame(root, bg="cadetblue3")
temp1= Entry(f, borderwidth = 3, width= 30,textvariable=t1, font= ("helvetica  17 bold"), bg="cornsilk1")
temp1.grid(ipady= 4,pady= 5)
f1= Frame(f, bg="cadetblue3")
f2= Frame(f, bg="cadetblue3")
option= ["Fahrenheit","Celsius", "Kelvin"]
click1=StringVar()
click1.set("Fahrenheit")
drop1= OptionMenu(f1, click1, *option)
drop1.grid()
drop1.config(bg="coral3", fg="cornsilk")
click2=StringVar()
click2.set("Celsius")
drop2= OptionMenu(f2, click2, *option)
drop2.grid()
drop2.config(bg="coral3", fg="cornsilk")
t2= StringVar()
t2.set("")
temp2= Entry(f, borderwidth = 3, width= 30,textvariable=t2, font= ("helvetica  17 bold"), bg="cornsilk1")
temp2.grid(ipady= 4,pady=10)
f1.grid(row=0,column=1, padx=10)
f2.grid(row=1,column=1, padx=10)
f.grid(row=1,column=0,padx=10)

b=Button(root, text="Convert", borderwidth= 3, bg="cornsilk3", fg="black")
b.grid(ipady=3,ipadx=5)
b.bind("<Button-1>", convert)


root.mainloop()