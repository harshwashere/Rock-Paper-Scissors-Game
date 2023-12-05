from tkinter import *
from tkinter import ttk
from random import *

window = Tk()
window.title("Rock Paper Scissors Game")
window.geometry("500x625")
window.config(bg="white")

rock_image = PhotoImage(file='images/rock-image.png')
paper_image = PhotoImage(file='images/paper-image.png')
scissors_image = PhotoImage(file='images/scissors.png')

imageList = [rock_image, paper_image, scissors_image]

randomNum = randint(0, 2)



def spinGame():
    randomNum = randint(0, 2)
    imageLabel.config(image=imageList[randomNum])

    if selectList.get() == "Rock":
        userValue = 0
    if selectList.get() == "Paper":
        userValue = 1
    if selectList.get() == "Scissors":
        userValue = 2
    if selectList.get() == "---Please Select---":
        userValue = 3
        textLabel.config(text="First, Please select from above\nbefore spinning the game.")
        
    if userValue == 0 and randomNum == 0:
        textLabel.config(text="It's a Tie :|", foreground="black")
    elif userValue == 0 and randomNum == 1:
        textLabel.config(text="YOU LOSE!!! TRY AGAIN :( ", foreground="red")
    elif userValue == 0 and randomNum == 2:
        textLabel.config(text="YOU WIN!!! YEAHHHHH!!! :) ", foreground="green")
        
    if userValue == 1 and randomNum == 1:
        textLabel.config(text="It's a Tie:|", foreground="black")
    elif userValue == 1 and randomNum == 2:
        textLabel.config(text="YOU LOSE!!! TRY AGAIN :( ", foreground="red")
    elif userValue == 1 and randomNum == 0:
        textLabel.config(text="YOU WIN!!! YEAHHHHH!!! :) ", foreground="green")
        
    if userValue == 2 and randomNum == 2:
        textLabel.config(text="It's a Tie:|", foreground="black")
    elif userValue == 2 and randomNum == 0:
        textLabel.config(text="YOU LOSE!!! TRY AGAIN :( ", foreground="red")
    elif userValue == 2 and randomNum == 1:
        textLabel.config(text="YOU WIN!!! YEAHHHHH!!! :) ", foreground="green")
        
def reset():
    textLabel.config(text="", background="white")
    imageLabel.config(image=imageList[0])
    selectList.current(0)


imageLabel = Label(window, image=imageList[randomNum], bd=0, height=330, background="white")
imageLabel.pack(pady=10)

selectList = ttk.Combobox(window, value=("---Please Select---","Rock", "Paper", "Scissors"))
selectList.current(0)
selectList.pack(pady=20)

spin = Button(window, text='Spin', command=spinGame, font=('Times New Roman', 18))
spin.place(y=410, x=170)

reset = Button(window, text='Reset', command=reset, font=('Times New Roman', 18))
reset.place(y=410, x=250)

textLabel = Label(window, text="", font=("Times New Roman", 18), background="white")
textLabel.place(y=490, x=150)


window.mainloop()


