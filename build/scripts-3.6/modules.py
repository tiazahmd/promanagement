import psutil

def extract_all():
    pid_list = []
    process_list = []
    user_list = []
    rows = 0
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        pid_list.append(proc.info['pid'])
        process_list.append(proc.info['name'])
        user_list.append(proc.info['username'])
        rows += 1
    return pid_list, process_list, user_list, rows