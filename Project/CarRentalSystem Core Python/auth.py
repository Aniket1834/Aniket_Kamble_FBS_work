import os

def authenticate_user(username, password):
    """Validate user credentials."""
    if not os.path.exists("users.txt"):
        print("User file not found.")
        return False

    with open("users.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                user, pwd, _ = parts
                if username == user and password == pwd:
                    return True
    return False


def authenticate_admin(username, password):
    """Validate any admin credentials (default or new)."""
    if not os.path.exists("admin.txt"):
        print("Admin file not found.")
        return False

    with open("admin.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                user, pwd = parts
                if username == user and password == pwd:
                    return True
    return False


def forgot_password():
    """Reset password for user or admin using username."""
    print("\n--- Password Recovery ---")
    print("1. User Password Reset")
    print("2. Admin Password Reset")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        file_name = "users.txt"
        print("\n--- User Password Reset ---")
        username = input("Enter your username: ").strip()
        if not os.path.exists(file_name):
            print("User data not found.")
            return
        with open(file_name, "r") as file:
            users = file.readlines()

        updated = []
        found = False
        for line in users:
            parts = line.strip().split(",")
            if len(parts) == 3:
                user, pwd, name = parts
                if user == username:
                    new_password = input("Enter new password: ").strip()
                    updated.append(f"{user},{new_password},{name}\n")
                    found = True
                    print("Password reset successfully.")
                else:
                    updated.append(line)
        if not found:
            print("Username not found.")
        else:
            with open(file_name, "w") as file:
                file.writelines(updated)

    elif choice == "2":
        file_name = "admin.txt"
        print("\n--- Admin Password Reset ---")
        username = input("Enter admin username: ").strip()
        if not os.path.exists(file_name):
            print("Admin data not found.")
            return
        with open(file_name, "r") as file:
            admins = file.readlines()

        updated = []
        found = False
        for line in admins:
            parts = line.strip().split(",")
            if len(parts) == 2:
                user, pwd = parts
                if user == username:
                    new_password = input("Enter new admin password: ").strip()
                    updated.append(f"{user},{new_password}\n")
                    found = True
                    print("Admin password reset successfully.")
                else:
                    updated.append(line)
        if not found:
            print("Admin username not found.")
        else:
            with open(file_name, "w") as file:
                file.writelines(updated)
    else:
        print("Invalid option.")
