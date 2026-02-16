import os

print("Student Management System")

while True:
    print("\n1. Add Student")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll: ")

        with open("students.txt", "a") as f:
            f.write(name + "," + roll + "\n")

        print("Student Added Successfully")

        # Sound when student added (Windows)
        os.system("echo \a")

    elif choice == "2":
        print("Exiting Program")
        os.system("echo \a")
        break

    else:
        print("Invalid Choice")
