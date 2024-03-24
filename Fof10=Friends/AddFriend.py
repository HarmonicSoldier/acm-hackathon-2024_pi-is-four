import tkinter as tk
from tkinter import messagebox

class AddFriendWindow:
    def __init__(self, parent, friend_name):
        self.parent = parent
        self.friend_name = friend_name

        self.window = tk.Toplevel(parent)
        self.window.title("User Options")
        self.window.geometry("300x150")

        self.label = tk.Label(self.window, text=f"Options for {self.friend_name}", font=("Arial", 12))
        self.label.pack(pady=5)

        self.send_button = tk.Button(self.window, text="Send Friend Request", command=self.send_friend_request)
        self.send_button.pack(pady=5)

        self.block_button = tk.Button(self.window, text="Block", command=self.confirm_block_user)
        self.block_button.pack(pady=5)

    def send_friend_request(self):
        self.label.config(text="Friend Request Sent")
        self.send_button.config(state="disabled")

    def confirm_block_user(self):
        confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to block {self.friend_name}?")
        if confirm:
            self.label.config(text="User Blocked")
            self.block_button.config(state="disabled")
            self.parent.destroy()  # Close the chat window if user is blocked

if __name__ == "__main__":
    # Test the AddFriendWindow
    root = tk.Tk()
    friend_window = AddFriendWindow(root, "TestUser")
    root.mainloop()
