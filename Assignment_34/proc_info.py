import psutil

def process_scanner():
    process_list = list()

    for process in psutil.process_iter():
        process_info = process.as_dict(attrs = ["pid", "name", "username", "status"])
        process_info["cpu_percent"] = process.cpu_percent(None)
        process_info["memory_percent"] = process.memory_percent()

        process_list.append(process_info)

    return process_list
