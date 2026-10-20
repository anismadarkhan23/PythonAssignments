import tkinter as tk

root = tk.Tk()

root.title("Voting Eligibility")
root.geometry("400x300")

tk.Label(
    root, 
    text = "Check Voting Eligibility", 
    font = ("Arial", 18, "bold")
).pack(pady = 10)

tk.Label(
    root,
    text = "Enter name of person"
).pack()
text_box1 = tk.Entry(root)
text_box1.pack()

tk.Label(
    root,
    text = "Enter age of person in years"
).pack()
text_box2 = tk.Entry(root)
text_box2.pack()

def check_voting_eligibility():
    age = int(text_box2.get())

    if age > 18:
        label_result.config(text = f"{text_box1.get()} is eligibile to vote for elections")
    else:
        label_result.config(text = f"{text_box1.get()} is not eligibile to vote for elections")

tk.Button(
    root,
    text = "Check Eligibility",
    command = check_voting_eligibility 
).pack(pady = 15)

label_result = tk.Label(
    root,
    text = "",
    font = ("Arial", 14)
)

label_result.pack()

root.mainloop()