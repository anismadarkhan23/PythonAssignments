import tkinter as tk

root = tk.Tk()

root.title("Addition Calculator")
root.geometry("400x300")

tk.Label(
    root, 
    text = "Addition Calculator", 
    font = ("Arial", 18, "bold")
).pack(pady = 10)

tk.Label(
    root,
    text = "Enter first number"
).pack()
text_box1 = tk.Entry(root)
text_box1.pack()

tk.Label(
    root,
    text = "Enter second number"
).pack()
text_box2 = tk.Entry(root)
text_box2.pack()

def addition():
    num1 = int(text_box1.get())
    num2 = int(text_box2.get())

    result = num1 + num2

    label_result.config(text = "Addition is: "+str(result))

tk.Button(
    root,
    text = "Addition",
    command = addition 
).pack(pady = 15)

label_result = tk.Label(
    root,
    text = "",
    font = ("Arial", 14)
)

label_result.pack()

root.mainloop()