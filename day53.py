# Create a program that allows users to draw on a canvas using a GUI

import tkinter

root = tkinter.Tk()
root.title("Drawing App")
canvas = tkinter.Canvas(root, bg="white", height=400, width=400)


def draw(event):
  x1, y1 = (event.x - 3), (event.y - 3)
  x2, y2 = (event.x + 3), (event.y + 3)
  canvas.create_oval(x1, y1, x2, y2, fill="black")


canvas.bind('<B1-Motion>', draw)

canvas.pack()
root.mainloop()