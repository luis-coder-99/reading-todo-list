def check_finish_reading(tasks):
    media_service = int(input("Type the number of the read newspapaer: "))
    if media_service in daily_media.keys() and not tasks[media_service]["completed"]:
        spend_time = float(input("Enter the time you spend in (minutes): "))
        if not tasks[media_service]["completed"]:
            tasks[media_service]["completed"] = True
            tasks[media_service]["total_time"] += spend_time
            print(f"Finishedt reading. Spend time on it: {spend_time:.2f} Min")
    else:
        #
        print("Wrong input")
    return tasks

def reset_programm(tasks):
    for task in tasks:
        tasks[task]["completed"] = False
        tasks[task]["total_time"] = 0.0
    return tasks

def add_newspaper(tasks):
    new_magazine = input("Type the name of the new magazine: ")
    new_number = max(daily_media.keys()) + 1
    daily_media[new_number] = new_magazine
    tasks[new_number] = {"completed": False, "total_time": 0.0}
    print(f"New Magazine '{new_magazine}' added")
    return tasks


def calculate_average_time_for_all(tasks):
    completed_tasks = [task["total_time"] for task in tasks.values() if task["completed"]]

    if completed_tasks:
        total_time_completed = sum(task["total_time"] for task in completed_tasks)
        return total_time_completed / len(completed_tasks)
    else:
        return 0.0

def calculate_average_time_for_some(tasks):
    completed_tasks = [task["total_time"] for task in tasks.values() if task["completed"]]
    for completed_task in completed_tasks:
        print(f"{completed_task}")
    
    user_selected_tasks = input("Select tasks:").split(",")
    for user_selected_task in user_selected_tasks:
        if user_selected_task in daily_media.keys() and user_selected_task in completed_tasks:
            current_task = completed_tasks[int(user_selected_task)-1]
            return current_task["total_time"] / len(user_selected_tasks)
        else:
            print("Try again")
    
def calculate_average_time_for_one(tasks):
    completed_tasks = [task["total_time"] for task in tasks.values() if task["completed"]]
    for completed_task in completed_tasks:
        print(f"{completed_task}")

    user_selected_task = int(input("Select task:"))
    if user_selected_task in daily_media.keys() and user_selected_task in completed_tasks:
        current_task = completed_tasks[int(user_selected_task)-1]
        return current_task["total_time"]
    else:
        print("Try again")

# Media I consume daily
daily_media = {
    1: "FAZ",
    2: "Tagesspiegel",
    3: "Handelsblatt",
    4: "Wirtschaftswoche",
    5: "Manager Magazin"
}

# Second Dictionary is there to save the time and the status of the daily media
model_tasks = {service: {"completed": False, "total_time": 0.0} for service in daily_media.keys()}


while True:
    print("Options")
    print("Type 'list' to see the magazines you reading daily")
    print("Type 'completed' to define a magazine as completed")
    print("Type 'average_1' to see what the average time was you spendend on all the magazines")
    print("Type 'average_2' to see what the average time was you spendend on specific the magazines")
    print("Type 'average_3' to see what the average time was you spendend on one the magazines")
    print("Type 'reset' to reset the whole program")
    print("Type 'quit' to exit the program")
    print("Type 'add' to add a new magazine")

    user_input = input("Input: ")


    if user_input == "quit":
        break
    elif user_input == "list":
        print("List of daily News Magazines you reead")
        for service, info in daily_media.items():
            status = "Completed" if model_tasks[service]["completed"] else "Not completed"
            total_time = model_tasks[service]["total_time"]
            print(f"{service}: ({info}) {status} - Total time {total_time:.2f} minutes")
    elif user_input == "average_1":
        completed_tasks = [task for task in model_tasks.values() if task["completed"]]
        average_time = calculate_average_time_for_all(model_tasks)
        print("Average time for all completed tasks: {:.2f} minutes".format(average_time))
    elif user_input == "average_2":
        completed_tasks = [task for task in model_tasks.values() if task["completed"]]
        average_time = calculate_average_time_for_some(model_tasks)
        print("Average time for specific completed tasks: {:.2f} minutes".format(average_time))
    elif user_input == "average_3":
        completed_tasks = [task for task in model_tasks.values() if task["completed"]]
        average_time = calculate_average_time_for_one(model_tasks)
        print("Average time for one completed tasks: {:.2f} minutes".format(average_time))
    elif user_input == "completed":
        model_tasks = check_finish_reading(model_tasks)
    elif user_input == "reset":
        model_tasks = reset_programm(model_tasks)
        print("The Programm willl be complettly reseted")
    elif user_input == "add":
        model_tasks = add_newspaper(model_tasks)
    else:
        ("Wrong Input")