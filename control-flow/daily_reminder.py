# Prompt for a single task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority using match case
match priority:
    case "high":
        message = f"Reminder: Your HIGH priority task '{task}' needs your focus."
    case "medium":
         message = f"Reminder: Your MEDIUM priority task '{task}' should be completed soon."
    case "low":
        message = f"Reminder: Your LOW priority task '{task}' can be done when you have free time."
    case _:
         message = f"Reminder: The task '{task}' has an UNKNOWN priority."

    # Modify reminder if time-bound
if time_bound == "yes":
    message += " This task requires immediate attention today!"

    # Provide customized reminder
    print(message)