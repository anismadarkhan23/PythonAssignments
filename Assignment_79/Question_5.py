import tkinter as tk

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def validate_login():
    username = username_entry.get().strip()
    password = password_entry.get()

    # Check for empty fields
    if not username or not password:
        label_result.config(text = f"Warning, Please enter both username and password.")
        return

    # Validate credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        label_result.config(text = f"Success, Login successful!\nWelcome, {username}!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        label_result.config(text = f"Access Denied, Invalid username or password.")
        password_entry.delete(0, tk.END)
        password_entry.focus()

# Create main window
root = tk.Tk()
root.title("Login Application")
root.geometry("450x300")

# Username Label and Entry
tk.Label(
    root, 
    text="Username:"
).pack(pady=(15, 2))
username_entry = tk.Entry(root)
username_entry.pack(pady=2)

# Password Label and Entry
tk.Label(
    root, 
    text="Password:"
).pack(pady=(10, 2))
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=2)

# Login Button
tk.Button(
    root, 
    text="Login", 
    command=validate_login
).pack(pady = 15)

# Bind Enter key to submit
label_result = tk.Label(
    root,
    text = "",
    font = ("Arial", 14)
)
label_result.pack()

# Start the application
root.mainloop()