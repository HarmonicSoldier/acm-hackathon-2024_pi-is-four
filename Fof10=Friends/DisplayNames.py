import os
import tkinter as tk

def display_names():
    """
    Reads names from the "FriendNames.txt" file and displays them in a separate window.
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path
    file_path = os.path.join(current_dir, "FriendNames.txt")

    # Read the names from the file
    with open(file_path, "r") as file:
        names = [name.strip() for name in file.readlines()]

    # Function to handle adding new name
    def add_name():
        new_name = entry.get()
        if new_name:
            with open(file_path, "a") as file:
                file.write(new_name + "\n")  # Write the name followed by a newline character
            names.append(new_name)
            label.config(text="\n".join(names))

    # Create a temporary window to get screen dimensions
    temp_window = tk.Tk()
    screen_width = temp_window.winfo_screenwidth()
    screen_height = temp_window.winfo_screenheight()
    temp_window.destroy()  # Destroy the temporary window

    # Create a new window
    window = tk.Tk()
    window.title("Friend Names")
    window.configure(bg="black")  # Set background color to black

    # Set the window size to fit the screen
    window.geometry(f"{int(screen_width * 0.8)}x{int(screen_height * 0.8)}")

    # Create a label to display the names
    label = tk.Label(window, text="\n".join(names),
                     font=("Arial", 16), fg="green", bg="black")  # Set text color to green
    label.pack(padx=20, pady=20)

    # Entry widget to enter new name
    entry = tk.Entry(window, font=("Arial", 12), bg="black", fg="green")
    entry.pack(padx=20, pady=(0, 10))

    # Button to add new name
    button = tk.Button(window, text="Add Name", command=add_name, bg="green", fg="black", font=("Arial", 12))
    button.pack(padx=20, pady=(0, 20))

    # Run the main event loop
    window.mainloop()

if __name__ == "__main__":
    display_names()
