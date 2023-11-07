import time 
### media i consume daily
daily_media = {
    1: "FAZ",
    2: "Tagesspiegel",
    3: "Handelsblatt",
    4: "Wirtschaftswoche",
    5: "Manager Magazin"
}
#### Second Dictionary to save the time and status of the first
task = {service: {"completed": False, "start_time": None, "end_time": None, "total_time": 0.0} for service in daily_media.values()}

def finish_reading(service, spend_time):
    if not task[service]["completed"]:
        tasks[service]["completed"] = True
        tasks[service]["endtime"] = time.time()
        if tasks[service]["start_time"] is not None
            time_spend = tasks[service]["end time"] - task[service]["start_time"]
            task[service]["total_time"] += spend_time
        task[service]["start_time"] = None
        print(f"{service} wurde als erledigt markiert.")



def reset_programm():
    for service in tasks:
        task[service]["completed"] = False
        task[service]["start_time"] = None
        task[service]["end_time"] = None
        task[service]["total_time"] = 0.0


def calculate_average_time():
    completed_task = [task for task in task.values() if task["completed"]]
    if completed_tasks:
        total_time_completed = sum(task["total_time"] for task in completed_task)
        return total_time_completed / len(completed_task)
    else:
        return 0.0

while true:
    print("Optionen:")
    print("Geben Sie 'List' ein, um alle Nachrichtendienste anzuzeigen")
    print("Geben Sie 'erledigt' ein, um ein Nachrichtendiesnt als erledit zu makieren")
    print("Geben Sie 'average' ein, um die durchschnittliche Zeit anzuzeigen")
    print("Geben Sie 'reset' ein, um das Programm zurückzusetzen")
    print("Geben Sie 'quit' ein, um das Programm zu beenden")

    user_input = input(": ")

