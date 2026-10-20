import tkinter as tk

root = tk.Tk()

root.title("Find Maximum Number Among Three Numbers")
root.geometry("400x300")

tk.Label(
    root, 
    text = "Find Maximum Number", 
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

tk.Label(
    root,
    text = "Enter third number"
).pack()
text_box3 = tk.Entry(root)
text_box3.pack()

def find_max_number():
    num1 = int(text_box1.get())
    num2 = int(text_box2.get())
    num3 = int(text_box3.get())

    result = max(num1, num2, num3)

    label_result.config(text = f"Maximum number from {num1}, {num2} & {num3} is "+str(result))

tk.Button(
    root,
    text = "Find Maximum",
    command = find_max_number 
).pack(pady = 15)

label_result = tk.Label(
    root,
    text = "",
    font = ("Arial", 14)
)

label_result.pack()

root.mainloop()