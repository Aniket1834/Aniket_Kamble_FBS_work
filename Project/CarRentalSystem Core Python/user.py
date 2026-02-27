import os
import datetime

class CarNotAvailableError(Exception):
    """Raised when a car is already rented."""
    pass


def register_user():
    """Register a new user."""
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()
    name = input("Enter your full name: ").strip()

    with open("users.txt", "a") as file:
        file.write(f"{username},{password},{name}\n")

    print("User registered successfully.")


def view_available_cars():
    """Display available cars."""
    print("\n--- Available Cars ---")
    if not os.path.exists("cars.txt"):
        print("No car data found.")
        return

    with open("cars.txt", "r") as file:
        for line in file:
            cid, name, status, rent = line.strip().split(",")
            print(f"{cid}. {name} - ₹{rent}/day - Status: {status}")


def rent_car(username):
    """Rent a car."""
    view_available_cars()
    car_id = input("Enter Car ID to rent: ").strip()
    days = int(input("Enter number of days: ").strip())

    with open("cars.txt", "r") as file:
        cars = file.readlines()

    updated = []
    rented_car = None

    for car in cars:
        cid, name, status, rent = car.strip().split(",")
        if cid == car_id:
            if status == "NotAvailable":
                raise CarNotAvailableError("This car is already rented.")
            else:
                status = "NotAvailable"
                rented_car = (name, int(rent), days)
                rent_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                total = int(rent) * days
                with open("rented.txt", "a") as rfile:
                    rfile.write(f"{username},{name},{rent_time},None,{days},{total}\n")
        updated.append(f"{cid},{name},{status},{rent}\n")

    with open("cars.txt", "w") as file:
        file.writelines(updated)

    if rented_car:
        print(f"You rented {rented_car[0]} for {rented_car[2]} days.")
        print(f"Total Rent: ₹{rented_car[1] * rented_car[2]}")
    else:
        print("Invalid Car ID entered.")


def return_car(username):
    """Return a rented car by car name or ID."""
    car_input = input("Enter the Car Name or Car ID to return: ").strip()

    if not os.path.exists("cars.txt"):
        print("Car file not found.")
        return

    with open("cars.txt", "r") as file:
        cars = file.readlines()

    updated = []
    found = False
    returned_name = None

    for car in cars:
        cid, name, status, rent = car.strip().split(",")
        if (cid == car_input or name.lower() == car_input.lower()) and status == "NotAvailable":
            status = "Available"
            found = True
            returned_name = name
        updated.append(f"{cid},{name},{status},{rent}\n")

    with open("cars.txt", "w") as file:
        file.writelines(updated)

    if not found:
        print("Car not found or not rented by you.")
        return

    if not os.path.exists("rented.txt"):
        print("Rental history not found.")
        return

    with open("rented.txt", "r") as file:
        records = file.readlines()

    updated_records = []
    for rec in records:
        user, cname, rent_time, ret_time, days, total = rec.strip().split(",")
        if user == username and cname == returned_name and ret_time == "None":
            ret_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        updated_records.append(f"{user},{cname},{rent_time},{ret_time},{days},{total}\n")

    with open("rented.txt", "w") as file:
        file.writelines(updated_records)

    print(f"{returned_name} returned successfully.")


def user_menu(username):
    """User menu."""
    while True:
        print(f"\n--- User Menu ({username}) ---")
        print("1. View available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_available_cars()
        elif choice == "2":
            try:
                rent_car(username)
            except CarNotAvailableError as e:
                print(e)
        elif choice == "3":
            return_car(username)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option.")
