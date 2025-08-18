# Prompt for a single task
Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
match Priority:
    case "high":
        message = f"Reminder: Your HIGH priority task '{Task}' needs your focus."
    case "medium":
        message = f"Reminder: Your MEDIUM priority task '{Task}' should be completed soon."
    case "low":
        message = f"Reminder: Your LOW priority task '{Task}' can be done when you have free time."
    case _:
        message = f"Reminder: The task '{Task}' has an UNKNOWN priority."

# Modify reminder if time-bound
if Time_bound == "yes":
    message += " This task requires immediate attention today!"

# Provide customized reminder
print(message)
