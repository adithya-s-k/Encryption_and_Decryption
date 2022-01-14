from tkinter import *
# from tkinter.ttk import *
# import tkinter.ttk as ttk
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk

root = tk.Tk(className='tab1')
root.geometry("1910x1020")
root.minsize(1910,1020)
root.maxsize(1910,1020)

canvas = Canvas(root, width = 1900, height = 1060)
canvas.pack()

def roundPolygon(x, y, sharpness, **kwargs):

    # The sharpness here is just how close the sub-points
    # are going to be to the vertex. The more the sharpness,
    # the more the sub-points will be closer to the vertex.
    # (This is not normalized)
    if sharpness < 2:
        sharpness = 2

    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness

    # Array to store the points
    points = []

    # Iterate over the x points
    for i in range(len(x)):
        # Set vertex
        points.append(x[i])
        points.append(y[i])

        # If it's not the last point
        if i != (len(x) - 1):
            # Insert submultiples points. The more the sharpness, the more these points will be
            # closer to the vertex. 
            points.append((ratioMultiplier*x[i] + x[i + 1])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[i + 1])/ratioDividend)
            points.append((ratioMultiplier*x[i + 1] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[i + 1] + y[i])/ratioDividend)
        else:
            # Insert submultiples points.
            points.append((ratioMultiplier*x[i] + x[0])/ratioDividend)
            points.append((ratioMultiplier*y[i] + y[0])/ratioDividend)
            points.append((ratioMultiplier*x[0] + x[i])/ratioDividend)
            points.append((ratioMultiplier*y[0] + y[i])/ratioDividend)
            # Close the polygon
            points.append(x[0])
            points.append(y[0])

    return canvas.create_polygon(points, **kwargs, smooth=TRUE)

my_rectangle = roundPolygon([20, 596, 596, 20], [30, 30, 990, 990], 20 , width=20, outline="#B5D9CD", fill="#B5D9CD")

my_rectangle = roundPolygon([20, 596, 596, 20], [30, 30, 990, 990], 20 , width=20, outline="#B5D9CD", fill="#B5D9CD")

root.mainloop()