from Tkinter import *
import random
root = Tk()
cv = Canvas(root, width = 256, height = 256)
cv.pack()
for n in range(1000):
    x = random.random() * 256
    y = random.random() * 256
    cv.create_oval(x - 2, y - 2, x + 2, y + 2)
root.mainloop()