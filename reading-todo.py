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

def finish_reading(service)
    if not task[service]["completed"]:
        tasks[service]["completed"] = True
        tasks[service]["endtime"] = time.time()
        if tasks[service]["start_time"] is not None
            time_spend = tasks[service]["end time"] - task[service]["start_time"]
            task[service]["total_time"] += time_spend
        task[service]["start_time"] = None
        print(f"{service} wurde als erledigt markiert.")
    else:
        print(f"{service} wurde bereits als erledigt markiert. ")


def reset_programm():
    for service in tasks:
        task[service]["completed"] = False
        task[service]["start_time"] = None
        task[service]["end_time"] = None
        task[service]["total_time"] = 0.0

