from tkinter import *
from ResourceCollection import *
from resetResource import resetConfig


def buttonClick(i):
    global x
    if capture(str(i)):
        x[i]['state'] = DISABLED
        x[i]['text'] = 'done'


resetConfig()
root = Tk()
root.geometry("200x720+1300+50")
n = ['Peace', 'You', 'Good Job', 'Dislike', 'Ok', 'Good Luck', 'Rock', 'Bang', 'Shocker', 'Bump',
     'Help', '1', '2', '3', '4', '5', 'Sprinkle', 'Half Heart', 'Yum', 'Love', 'Naruto', 'Kaneki','Nothing']
x = list()
for j, i in enumerate(n):
    x.append(Button(root, text=i, width=15,
                    command=lambda c=j: buttonClick(c)))
    x[j].place(x=45, y=10+j*30)
root.mainloop()
