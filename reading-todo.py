import time

# Media I consume daily
daily_media = {
    1: "FAZ",
    2: "Tagesspiegel",
    3: "Handelsblatt",
    4: "Wirtschaftswoche",
    5: "Manager Magazin"
}

# Second Dictionary is there to save the time and the status of the daily media
tasks = {service: {"completed": False, "total_time": 0.0} for service in daily_media.keys()}
        
# Functions to
def finish_reading(media_service, spend_time):
    if not tasks[media_service]["completed"]:
        tasks[media_service]["completed"] = True
        tasks[media_service]["total_time"] += spend_time
        print(f"Finishedt reading. Spend time on it: {spend_time:.2f} Min")
              
def check_finish_reading():
    count = 0
    while count <3:
        media_service = int(input("Type the number of the read newspapaer: "))
        if media_service in daily_media.keys() and not tasks[media_service]["completed"]:
            spend_time = float(input("Enter the time you spend in (minutes): "))
            finish_reading(media_service, spend_time)
            count += 1
        else:
            print("Wrong input")

def reset_programm():
    for task in tasks:
        tasks[task]["completed"] = False
        tasks[task]["total_time"] = 0.0

def add_newspaper():
    new_magazine = input("Type the name of the new magazine: ")
    new_number = max(daily_media.keys()) + 1
    daily_media[new_number] = new_magazine
    tasks[new_number] = {"completed": False, "total_time": 0.0}
    print(f"New Magazine '{new_magazine}' added")


def calculate_average_time():
    completed_tasks = [task["total_time"] for task in tasks.values() if task["completed"]]

    if completed_tasks:
        total_time_completed = sum(task["total_time"] for task in completed_tasks)
        return total_time_completed / len(completed_tasks)
    else:
        return 0.0


while True:
    print("Options")
    print("Type 'list' to see the magazines you reading daily")
    print("Type 'completed' to define a magazine as completed")
    print("Type 'average' to see what the average time was you spendend on the magazines")
    print("Type 'reset' to reset the whole program")
    print("Type 'quit' to exit the program")
    print("Type 'add' to add a new magazine")

    user_input = input("Input: ")



    if user_input == "quit":
        break
    elif user_input == "list":
        print("List of daily News Magazines you reead")
        for service, info in daily_media.items():
            status = "Completed" if tasks[service]["completed"] else "Not completed"
            total_time = tasks[service]["total_time"]
            print(f"{service}: ({info}) {status} - Total time {total_time:.2f} minutes")
    elif user_input == "average":
        completed_tasks = [task for task in tasks.values() if task["completed"]]
        average_time = calculate_average_time()
        print("Average time for completed tasks: {:.2f} minutes".format(average_time))
    elif user_input == "completed":
        check_finish_reading()
    elif user_input == "reset":
        reset_programm()
        print("The Programm willl be complettly reseted")
    elif user_input == "add":
        add_newspaper()
    else:
        ("Wrong Input")