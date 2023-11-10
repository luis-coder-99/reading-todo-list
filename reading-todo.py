import time

#Media I consume daily
daily_media = {
    1: "FAZ",
    2: "Tagesspiegel",
    3: "Handelsblatt",
    4: "Wirtschaftswoche",
    5: "Manager Magazin"
}

# Second Dictionary to save time and status
tasks = {service: {"completed": False, "total_time": 0.0} for service in daily_media.values()}

#Functions
def finish_reading(service, spend_time):
    if not tasks[service]["completed"]:
        tasks[service]["completed"] = True
        tasks[service]["total_time"] += spend_time
        print(f"{service} wurde als erledigt makiert. Verbrachte Zeit: {spend_time:.2f} Sekunden")

def reset_programm():
    for service in tasks:
        tasks[service]["completed"] = False

def calculate_average_time():
    completed_tasks = [task for task in tasks.values() if task["completed"]]
    if completed_tasks:
        total_time_completed = sum(task["total_time"] for task in completed_tasks)
        return total_time_completed / len(completed_tasks)
    else:
        return 0.0

while True:
    print("Options:")
    print("Type 'List' to see all newspapers I daily read")
    print("Type 'completed' to mark a news service as completed")
    print("Type 'average' to see the average time")
    print("Type 'reset' to reset the program")
    print("Type 'quit' to exit the program")

    user_input = input("Input: ")

    if user_input == "quit":
        break
    elif user_input == "List":
        print("List of daily newspapers I read:")
        for service, info in daily_media.items():
            status = "Completed" if tasks[info]["completed"] else "Not completed"
            total_time = tasks[info]["total_time"]
            print(f"{service}: {info} - {status} - Total time {total_time:.2f} seconds")
    elif user_input == "average":
        average_time = calculate_average_time()
        print(f"Average time for completed tasks: {average_time:.2f} seconds")
    elif user_input == "completed":
        service = int(input("Enter the number of the read news magazine: "))
        if service in daily_media.values() and not tasks[service]["completed"]:
            spend_time = float(input("Enter the time spent (in seconds): "))
            finish_reading(service, spend_time)

        
