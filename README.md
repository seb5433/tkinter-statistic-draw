# tkinter-statistic-draw
With this repository you can draw statistics using tkinter and of course python.
# 1. How to use
```python
import estadistica

master = Tk()
canvas_width = 200
canvas_height = 100

view = estadistica.View(master, 450, 300)
view.make_table([45, 38, 92, 54, 100], 20, ["Geometria",
                    "Fisica", "Aritmetica", "Matematica"])

master.mainloop()
```
OUTPUT ->
![alt text](https://github.com/seb5433/tkinter-statistic-draw/blob/main/screenshot.jpeg)

