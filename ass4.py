def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid input"
    elif marks >= 0 and marks <= 30:
        return "D"
    elif marks >= 31 and marks <= 50:
        return "C"
    elif marks >= 51 and marks <= 70:
        return "B"
    elif marks >= 71 and marks <= 100:
        return "A"

while True:
    try:
        marks = int(input("Enter your marks (0-100): "))
        grade = calculate_grade(marks)
        if grade != "Invalid input":
            print(f"Your grade is: {grade}")
        else:
            print("Invalid input. Unrecognized marks/avg.")
    except ValueError:
        print("Invalid input. Unrecognized marks/avg")
    another = input("Do you want check marks again? (yes/no): ").lower()
    if another != "yes":
        break