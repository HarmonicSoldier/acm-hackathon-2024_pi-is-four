import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
from ChatBot import chat_bot

def get_random_names(num_names=3):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "FriendNames.txt")
    with open(file_path, "r") as file:
        names = [name.strip() for name in file.readlines()]
    return random.sample(names, num_names)

class MatchHub:
    def __init__(self, root):
        self.root = root
        self.root.title("Match Hub")
        self.root.geometry("600x400")
        self.root.configure(bg="lightblue")

        self.matches = get_random_names()

        self.match_list_frame = tk.Frame(self.root, bg="lightblue")
        self.match_list_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.match_list_label = tk.Label(self.match_list_frame, text="Your Matches:", bg="lightblue", font=("Arial", 12, "bold"))
        self.match_list_label.pack(pady=5)

        self.match_listbox = tk.Listbox(self.match_list_frame, bg="white", font=("Arial", 10), selectmode=tk.SINGLE, height=10)
        self.match_listbox.pack(expand=True, fill="both", padx=10, pady=5)

        for match in self.matches:
            self.match_listbox.insert(tk.END, match)

        self.action_frame = tk.Frame(self.root, bg="lightblue")
        self.action_frame.pack(side="top", fill="x", padx=10, pady=(0, 10))

        self.answer_questions_button = tk.Button(self.action_frame, text="Answer More Questions", command=self.answer_questions, bg="skyblue", fg="white", font=("Arial", 10), relief=tk.FLAT)
        self.answer_questions_button.pack(side="left", padx=5)

        self.block_button = tk.Button(self.action_frame, text="Block", command=self.block_user, bg="red", fg="white", font=("Arial", 10), relief=tk.FLAT)
        self.block_button.pack(side="right", padx=5)

        self.match_listbox.bind("<Double-Button-1>", self.open_chat)

        self.credit_label = tk.Label(self.root, text="Created by Π=4", bg="lightblue", font=("Arial", 8, "bold"))
        self.credit_label.place(relx=1, rely=1, anchor="se")

    def answer_questions(self):
        print("Answering more questions...")

    def block_user(self):
        selected_match = self.match_listbox.get(tk.ACTIVE)
        confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to block {selected_match}?")
        if confirm:
            self.remove_match(selected_match)
            messagebox.showinfo("Success", f"{selected_match} blocked successfully.")

    def remove_match(self, match_name):
        index = self.matches.index(match_name)
        del self.matches[index]
        self.match_listbox.delete(index)

    def open_chat(self, event):
        selected_match = self.match_listbox.get(tk.ACTIVE)
        chat_bot(selected_match)

if __name__ == "__main__":
    root = tk.Tk()
    match_hub = MatchHub(root)
    root.mainloop()
