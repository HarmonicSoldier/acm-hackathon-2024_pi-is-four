import os
import random

def get_random_name():
    """
    Returns a random name from the "FriendNames.txt" file.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "FriendNames.txt")

    with open(file_path, "r") as file:
        names = [name.strip() for name in file.readlines()]

    return random.choice(names)

if __name__ == "__main__":
    random_name = get_random_name()
    print(f"Random name: {random_name}")
