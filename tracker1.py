students = ["Ravi", "Asha", "Kiran"]

attendance = {}
attendance_history = {name: [] for name in students}


def save_to_file():
    with open("attendance_record.txt", "a") as file:
        file.write("Today's Attendance:\n")
        for name, status in attendance.items():
            file.write(f"{name} : {status}\n")
        file.write("\n")  # Blank line after each session

def mark_attendance():
    print("\nMark Attendance:")
    for name in students:
        status = input(f"Is {name} present? (p/a): ").lower()
        if status == "p":
            attendance[name] = "Present"
            attendance_history[name].append("Present")
        else:
            attendance[name] = "Absent"
            attendance_history[name].append("Absent")

    print("\nAttendance marked successfully!")

    # Save in txt file
    save_to_file()
    print("Attendance saved in 'attendance_record.txt'\n")

def show_attendance():
    print("\n--- Attendance Report ---")
    if not attendance:
        print("No attendance recorded yet!\n")
        return
    for name, status in attendance.items():
        print(f"{name} : {status}")
    print()

def add_student():
    name = input("Enter new student name: ")
    students.append(name)
    attendance_history[name] = []
    print(f"{name} added successfully!\n")

def show_percentage():
    print("\n--- Attendance Percentage ---")
    for name in students:
        total = len(attendance_history[name])
        present = attendance_history[name].count("Present")
        percent = (present / total * 100) if total > 0 else 0
        print(f"{name} : {percent:.2f}%")
    print()

def show_low_attendance():
    print("\n--- Students With Attendance < 75% ---")
    found = False
    for name in students:
        total = len(attendance_history[name])
        present = attendance_history[name].count("Present")
        percent = (present / total * 100) if total > 0 else 0

        if percent < 75:
            print(f"{name} : {percent:.2f}%")
            found = True

    if not found:
        print("All students have 75% or above attendance!")
    print()

while True:
    print("1. Mark Attendance")
    print("2. Show Attendance")
    print("3. Add Student")
    print("4. Show Attendance Percentage")
    print("5. Show Students Below 75%")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        show_attendance()
    elif choice == "3":
        add_student()
    elif choice == "4":
        show_percentage()
    elif choice == "5":
        show_low_attendance()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")
