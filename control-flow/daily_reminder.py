task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bounded = input("Is it time-bounded? (yes/no):").lower()

if time_bounded:
    match priority:
        case "high":
            print(f"Reminder:'{task}' is a {priority} priority task that requires immediate attention today!")
        case "medium":
            print(f"Reminder:'{task}' is a {priority} priority task that requires immediate attention today!")
        case "low":
            print(f"Reminder:'{task}' is a {priority} priority task that requires immediate attention today!")
else:
    match priority:
        case "high":
            print(f"Note:'{task}' is a {priority} priority task. Consider completing it when you have free time.")
        case "medium":
            print(f"Note:'{task}' is a {priority} priority task. Consider completing it when you have free time.")
        case "low":
            print(f"Note:'{task}' is a {priority} priority task. Consider completing it when you have free time.")