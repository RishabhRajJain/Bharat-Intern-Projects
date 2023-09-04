from tkinter import *
import time


class QUIZ(Tk):

    def __init__(self):
        super().__init__()
        can_width = 1000
        can_height = 700
        self.geometry(f"{can_width}x{can_height}")
        self.config(background="orange")
        self.minsize(width= 1000, height= 700)
        self.maxsize(width= 1000, height= 700)
        self.title("Quiz App by Rishabh Raj Jain")
        self.wm_iconbitmap("Quiz.ico")

    def game(self):
        print("No")
        new = Toplevel()
        can_width = 1000
        can_height = 700
        new.geometry(f"{can_width}x{can_height}")
        new.config(background="aquamarine4")
        new.minsize(width=1000, height=700)
        new.maxsize(width= 1000, height= 700)
        new.title("Quiz App by Rishabh Raj Jain")
        new.wm_iconbitmap("Quiz.ico")

        tag = Label(new, text="Quizzz!", bg="aquamarine4", fg="white", font="Times 70 bold")
        tag.place(x=350, y=50)
        t = Label(new, text="30",bg="aquamarine4", fg="white", font="Times 60 bold")
        t.place(x=450,y=170)



        que = Canvas(new, width="900", height="70", bg="darkorange", borderwidth=10, relief=SUNKEN)
        que.place(x=30, y=270)
        questions = ["Who is the first President of India?", "Who was the first Prime Minister of India?"]
        options = [{"C.Rajagopalachari", "Dr. Rajendra Prasad", "Pandit Jawaharlal Nehru", "Lord Mountbatten"},
                   {"Indira Gandhi", "Narendra Modi", "Jawaharlal Nehru", "Rajiv Gandh"}]
        coropt = ["Dr. Rajendra Prasad", "Jawaharlal Nehru"]
        que.create_text(455, 50, text="Who is the first President of India?", fill="white", font="Helvetica 32 bold")
        var = IntVar()
        var.set(1)
        a = 1
        c = 390


        submit= Button(new, text="Submit", font="Roboto 15 bold", bg="darkseagreen2", fg="black", padx=10)
        submit.place(x=800,y=600)
        submit.bind("<Button-1>")

        def click(event):
            global count
            count = 0
            global w
            w = 1
            text = event.widget.cget("text")
            if text == "Submit":
                if var.get() == 2:
                    count = count + 4
                    print("2")
                    return count
                elif var.get() != 2:
                    print("3")
                    count = count - 1
                    return count

        for j in questions:

            que = Canvas(new, width="900", height="70", bg="darkorange", borderwidth=10, relief=SUNKEN)
            que.place(x=30, y=270)
            que.create_text(455, 50, text=j, fill="white", font="Helvetica 32 bold")
            for i in options:
                a = 1
                c = 390

                for k in i:
                    radio = Radiobutton(new, text=k, variable=var, value=a, bg="aquamarine4", font="helvetica 20 bold",
                                        anchor=NW)
                    radio.place(x=50, y=c + 10, width=400)
                    c = c + 50
                    a += 1

                    root.update()
                for x in range(30, -1, -1):
                    t.config(text=f"{x:02}", bg="aquamarine4", fg="white", font="Times 60 bold")
                    print(f"{x:02}")
                    root.update()
                    time.sleep(1)
                submit.bind("<Button-1>", click)








    def rules(self):
        print("Yes")

        l1.config(text="Rules"
                       "\n1. All questions contains 4 marks"
                       "\n2. Negative marking of 1 mark on each question"
                       "\n3. Result will given in the end"
                       "\n4. Click start to enter into the Game"
                       "\n5. You'll get 30 seconds to answer the question", bg="orange", fg="cadetblue4", font='Helvitica 30  bold')
        button1 = Button(f2, text="Start", bg="burlywood3", fg="beige", font='roboto 15  bold', command=root.game)
        button1.pack(anchor=NE, ipadx=5, padx=20,pady=10)



if __name__ == '__main__':
    root = QUIZ()
    f1 = Frame(root, bg="orange")
    f1.pack(expand=TRUE)
    l1 = Label(f1, text="Welcome to the Game", bg="orange", fg="cadetblue4", font='Helvitica 50  bold')
    l1.pack(pady=170)
    f2= Frame(root, bg="orange")
    f2.pack(anchor= NW, ipadx= 500)
    button = Button(f2, text="Next", bg="burlywood3", fg="beige", font='roboto 15  bold',
                    command=root.rules)
    button.pack(anchor=NW, ipadx=5, padx=20, pady=10, side= LEFT)

    # l1 = Label(f1, text="Rules", bg="orange", fg="cadetblue4", font='Helvitica 50  bold')
    # l1.pack(pady=150)





    root.mainloop()