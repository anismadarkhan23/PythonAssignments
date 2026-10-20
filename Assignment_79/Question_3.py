import tkinter as tk

root = tk.Tk()

root.title("Area of Circle")
root.geometry("400x300")

tk.Label(
    root, 
    text = "Calculate Area of Circle", 
    font = ("Arial", 18, "bold")
).pack(pady = 10)

tk.Label(
    root,
    text = "Enter radius of circle"
).pack()
text_box1 = tk.Entry(root)
text_box1.pack()

def calculate_area_of_circle():
    radius = float(text_box1.get())

    area_of_circle = 3.14 * (radius ** 2)

    label_result.config(text = f"Area of Circle is "+str(area_of_circle))

tk.Button(
    root,
    text = "Calculate Area",
    command = calculate_area_of_circle 
).pack(pady = 15)

label_result = tk.Label(
    root,
    text = "",
    font = ("Arial", 14)
)

label_result.pack()

root.mainloop()