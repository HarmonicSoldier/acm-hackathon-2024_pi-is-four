import tkinter as tk
from tkinter import ttk
from MatchHub import MatchHub  # Import MatchHub class from MatchHub.py

class MatchLoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Match Loading Screen")
        self.root.geometry("400x250")  # Adjusted height to accommodate the additional label
        self.root.configure(bg="lightblue")

        self.loading_frame = tk.Frame(self.root, bg="lightblue")
        self.loading_frame.pack(expand=True, fill="both")

        self.loading_label = tk.Label(self.loading_frame, text="Loading Matches...", bg="lightblue", font=("Arial", 12))
        self.loading_label.pack(pady=20)

        self.progress_bar = ttk.Progressbar(self.loading_frame, length=200, mode='determinate', style='grey.Horizontal.TProgressbar')
        self.progress_bar.pack(pady=10)

        self.go_to_matches_button = tk.Button(self.loading_frame, text="Go To Matches", command=self.go_to_matches)
        self.go_to_matches_button.pack(pady=20)
        self.go_to_matches_button.configure(state="disabled")

        # New label displaying the credit with smaller and bold font
        self.credit_label = tk.Label(self.loading_frame, text="Created by Π=4", bg="lightblue", font=("Arial", 8, "bold"))
        self.credit_label.place(relx=1.0, rely=1.0, anchor="se")  # Placing label in the bottom right corner

        self.loading_label.after(1000, self.load_matches)  # Adjusted delay to 1 second

    def load_matches(self):
        progress = 0
        while progress <= 100:
            self.progress_bar["value"] = progress
            self.root.update_idletasks()  # Update the GUI to reflect changes
            progress += 5  # Adjust the increment value as needed for desired speed
            self.root.after(100)  # Adjust the delay to control the speed of progress
        self.loading_label.config(text="Matches loaded successfully!")
        self.go_to_matches_button.configure(state="normal")

    def go_to_matches(self):
        self.root.destroy()
        root = tk.Tk()
        match_hub = MatchHub(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    loading_screen = MatchLoadingScreen(root)
    root.mainloop()