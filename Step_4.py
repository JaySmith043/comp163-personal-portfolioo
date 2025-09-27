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

    study_options = ["Programming", "Math", "English", "History"]

    print("\nChoose a subject to study from the following options:")
    print(study_options)

    subject_choice = input("Your subject: ")

    
    if subject_choice not in study_options:
        print("Invalid subject choice. Please pick from the list exactly as shown.")
    else:
        print(f"You decided to study {subject_choice}.")


        if (subject_choice == "Programming" and current_gpa <= 3.4) and (study_hours >= 20 or stress_level <= 60):
            current_gpa += 0.15
            social_points -= 3
            print("Focused Programming session! Noticeable GPA boost, tiny social tradeoff.")


        elif (subject_choice in ("Math", "English")) and not (stress_level > 70):
            current_gpa += 0.10
            social_points -= 5
            print("Solid study in Math/English. Small GPA gain; less time for friends.")


        elif subject_choice == "History" and (social_points <= 60 or stress_level >= 50):
            social_points += 8
            stress_level -= 5
            print("History deep-dive calms you and reconnects you with classmates.")


        else:
            current_gpa += 0.05
            print("Light review helps a little across the board.")


            print("\nFinal decision: Do you want to attend a study group? (yes/no)")
            group_choice = input("Your choice: ")


            if type(group_choice) is str and group_choice is not None:
                if group_choice.lower() == "yes":
                    study_hours += 3
                    stress_level -= 5
                    print("You joined a study group — productive and supportive!")
                elif group_choice.lower() == "no":
                    social_points += 5
                    print("You skipped the study group — more time for friends.")
                else:

                    if group_choice.lower() != "yes" and group_choice.lower() != "no":
                        print("Unrecognized response. Defaulting to 'no group'.")
                        social_points += 2
            else:

                print("Unexpected input type. No action taken.")


            current_gpa = max(0.0, min(4.0, current_gpa))


            print("\n=== Final Outcome ===")
            if current_gpa >= 3.5:
                if stress_level <= 50:
                    print("Ending 1: Academic Excellence! High GPA with healthy balance.")
                else:
                    print("Ending 2: Burnout Scholar. Strong GPA but stress is high.")
            elif current_gpa >= 2.0:
                if social_points >= 60:
                    print("Ending 3: Social Star! Solid grades and strong friendships.")
                else:
                    print("Ending 4: Average Achiever. Passing, but room to grow.")
            else:
                print("Ending 5: Academic Probation. Time to rethink your strategy next term.")

            
            print("\n=== Final Statistics ===")
            print(f"GPA: {current_gpa:.2f}")
            print(f"Study Hours: {study_hours}")
            print(f"Social Points: {social_points}")
            print(f"Stress Level: {stress_level}/100")