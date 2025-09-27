# [jedewittsmith]_assignment_3.py
# COMP 163: Assignment 4 - College Life Adventure Game


student_name = "Jadyn"
current_gpa = 3.9
study_hours = 25
social_points = 50
stress_level = 80


print("=== Welcome to the College Life Adventure Game! ===")
print(f"Student: {student_name}")
print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}/100")


print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa >= 2.0:
        study_hours -= 5
        stress_level -= 10
        print("You chose a Light course load. Less stress and more free time!")
    else:
        stress_level += 5
        print("Even with a Light load, your GPA may cause stress.")
elif choice == "B":
    if current_gpa >= 3.0:
        study_hours += 5
        stress_level += 10
        print("You chose a Standard course load. Balanced but slightly stressful.")
    else:
        stress_level += 20
        print("Standard load feels tough with your current GPA.")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 10
        stress_level += 15
        print("You chose a Heavy course load. You can handle it with your high GPA!")
    else:
        study_hours += 10
        stress_level += 30
        print("Heavy load is overwhelming without a stronger GPA!")
else:

    print("Invalid choice. Please select A, B, or C.")