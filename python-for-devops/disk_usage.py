import psutil
def check_disk_usage_threshold():
    disk_threshold = int(input("Enter the disk threshold: "))
    current_disk = psutil.disk_usage('/').percent
    print("current disk usuage %: ", current_disk)
    if current_disk > disk_threshold:
        print("disk Alert email sent!")
    else:
        print("disk is in safe")


check_disk_usage_threshold()