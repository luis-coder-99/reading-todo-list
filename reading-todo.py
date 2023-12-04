### Checks if reading is finished
def check_finish_reading(tasks):
    media_service = int(input("Type the number of the read newspaper: "))
    if media_service in daily_media.keys() and not tasks[media_service]["completed"]:
        spend_time = float(input("Enter the time you spend in (minutes): "))
        if not tasks[media_service]["completed"]:
            tasks[media_service]["completed"] = True
            tasks[media_service]["total_time"] += spend_time
            print(f"Finished reading. Spend time on it: {spend_time:.2f} Min")
    else:
        #
        print("Wrong input")
    return tasks
### Is resetting all programms

def reset_programm(tasks):
    for task_key in tasks.keys():
        tasks[task_key]["completed"] = False
        tasks[task_key]["total_time"] = 0.0
    return tasks
### Is adding new Newspapers

def add_newspaper(tasks):
    new_magazine = input("Type the name of the new magazine: ")
    new_number = max(daily_media.keys()) + 1
    daily_media[new_number] = new_magazine
    tasks[new_number] = {"completed": False, "total_time": 0.0}
    print(f"New Magazine '{new_magazine}' added")
    return tasks
### Calculating the average time for all

def calculate_average_time_for_all(tasks):
    times = []
    for task in tasks.values():
        if task["completed"]:
            times.append(task["total_time"])
    if not times:
        return 0.0

    total_time = sum(times)
    average_time = total_time / len(times)
    return average_time

def calculate_average_time_for_some(daily_media, tasks):
    completed_tasks = {}
    for service, task_value in tasks.items():
        if task_value["completed"]:
            completed_tasks[service] = task_value
    
    for completed_key, completed_task in completed_tasks.items():
        print(f"{daily_media[completed_key]} {completed_task['total_time']}")
    
    user_selected_services = input("Select service name:").split(",")
    total_time_selected_tasks = 0.0
    for user_selected_service in user_selected_services:
        print(user_selected_service)
        user_selected_service_key = None
        for daily_media_key, daily_media_value in daily_media.items():  
            if user_selected_service == daily_media_value:
                user_selected_service_key = daily_media_key

        if user_selected_service_key and completed_tasks[user_selected_service_key]:
            current_task = completed_tasks[user_selected_service_key]
            total_time_selected_tasks += current_task["total_time"]
        else:
            print("Try again")
    return total_time_selected_tasks / len(user_selected_services)
   
# Dictionary of the Media I consume daily
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
    print("Type 'average_2' to see what the average time was you spendend on on or more of the magazines")
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
        average_time = calculate_average_time_for_all(model_tasks)
        print("Average time for all completed tasks: {:.2f} minutes".format(average_time))
    elif user_input == "average_2":
            average_time = calculate_average_time_for_some(daily_media, model_tasks)
            print("Average time for specific completed tasks: {:.2f} minutes".format(average_time))
    elif user_input == "completed":
        model_tasks = check_finish_reading(model_tasks)
    elif user_input == "reset":
        model_tasks = reset_programm(model_tasks)
        print("The Programm will be completly reseted")
    elif user_input == "add":
        model_tasks = add_newspaper(model_tasks)
    else:
        print("Wrong Input")