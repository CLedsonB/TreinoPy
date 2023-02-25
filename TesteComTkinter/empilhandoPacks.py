import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill = tk.X, side=tk.TOP)

label1 = tk.Label(master=frame1, text="I'm label1", bg="purple")
label1.place(x=200, y=10)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill = tk.X, side=tk.TOP)

label2 = tk.Label(master=frame2, text="I'm label2", bg="green")
label2.place(x=200, y=5)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill = tk.X, side=tk.TOP)

frame4 = tk.Frame(master=window, width=200, height=100, bg="red")
frame4.pack(fill=tk.Y, side=tk.LEFT)

frame5 = tk.Frame(master=window, width=100, bg="yellow")
frame5.pack(fill=tk.Y, side=tk.LEFT)

frame6 = tk.Frame(master=window, width=50, bg="blue")
frame6.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()