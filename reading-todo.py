import time 
daily_media = {
    1: "FAZ",
    2: "Tagesspiegel",
    3: "Handelsblatt",
    4: "Wirtschaftswoche",
    5: "Manager Magazin"
}
#### Second Dictionary to save the time and status of the first
task = {service: {"completed": False, "start_time": None, "end_time": None, "total_time": 0.0} for service in daily_media.values()}
print(task)