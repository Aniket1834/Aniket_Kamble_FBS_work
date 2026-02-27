import os
import auth
import user
import admin

def main_menu():
    """Main menu for Car Rental System."""
    while True:
        print("\n--- Car Rental System ---")
        print("1. Existing User Login")
        print("2. New User Registration")
        print("3. Admin Login")
        print("4. Forgot Password")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if auth.authenticate_user(username, password):
                print(f"Login successful. Welcome, {username}.")
                user.user_menu(username)
            else:
                print("Invalid username or password.")

        elif choice == "2":
            user.register_user()

        elif choice == "3":
            username = input("Enter admin username: ").strip()
            password = input("Enter admin password: ").strip()
            if auth.authenticate_admin(username, password):
                print(f"Default Admin login successful. Welcome, {username}.")
                admin.admin_menu()
            else:
                print("Invalid admin credentials.")

        elif choice == "4":
            auth.forgot_password()

        elif choice == "5":
            print("Thank you for using the Car Rental System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
