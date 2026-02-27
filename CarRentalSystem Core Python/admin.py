import os

def view_cars():
    """View all cars."""
    print("\n--- Car List ---")
    if not os.path.exists("cars.txt"):
        print("No cars found.")
        return

    with open("cars.txt", "r") as file:
        for line in file:
            cid, name, status, rent = line.strip().split(",")
            print(f"{cid}. {name} - ₹{rent}/day - Status: {status}")


def add_car():
    """Add a car."""
    cid = input("Enter Car ID: ").strip()
    name = input("Enter Car Name: ").strip()
    rent = input("Enter Rent per Day: ").strip()

    with open("cars.txt", "a") as file:
        file.write(f"{cid},{name},Available,{rent}\n")
    print("Car added successfully.")


def delete_car():
    """Delete a car."""
    car_id = input("Enter Car ID to delete: ").strip()
    if not os.path.exists("cars.txt"):
        print("Car data not found.")
        return

    with open("cars.txt", "r") as file:
        cars = file.readlines()

    updated = [car for car in cars if car.strip().split(",")[0] != car_id]
    with open("cars.txt", "w") as file:
        file.writelines(updated)
    print("Car deleted successfully.")


def view_rented_history():
    """View rental records."""
    print("\n--- Rental History ---")
    if not os.path.exists("rented.txt"):
        print("No rental history found.")
        return

    with open("rented.txt", "r") as file:
        for line in file:
            user, car, rent_time, ret_time, days, total = line.strip().split(",")
            print(f"User: {user} | Car: {car} | Days: {days} | Total: ₹{total} | Rented: {rent_time} | Returned: {ret_time}")


def add_new_admin():
    """Allow any admin to add new admin."""
    print("\n--- Add New Admin ---")
    new_username = input("Enter new admin username: ").strip()
    new_password = input("Enter new admin password: ").strip()

    with open("admin.txt", "a") as file:
        file.write(f"{new_username},{new_password}\n")

    print(f"New admin '{new_username}' added successfully.")


def admin_menu():
    """Admin menu."""
    while True:
        print("\n--- Admin Menu ---")
        print("1. View Cars")
        print("2. Add Car")
        print("3. Delete Car")
        print("4. View Rental History")
        print("5. Add New Admin")
        print("6. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_cars()
        elif choice == "2":
            add_car()
        elif choice == "3":
            delete_car()
        elif choice == "4":
            view_rented_history()
        elif choice == "5":
            add_new_admin()
        elif choice == "6":
            print("Logging out of admin account...")
            break
        else:
            print("Invalid choice.")
