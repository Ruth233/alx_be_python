# Prompt for a single task
Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
match Priority:
    case "high":
        reminder = f"Your HIGH priority task '{Task}' needs your focus."
    case "medium":
        reminder = f"Your MEDIUM priority task '{Task}' should be completed soon."
    case "low":
        reminder = f"Your LOW priority task '{Task}' can be done when you have free time."
    case _:
        reminder = f"The task '{Task}' has an UNKNOWN priority."

# Modify reminder if time-bound
if Time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Provide customized reminder (must literally begin with Reminder:)
print(f"Reminder: {reminder}")
