import psutil


def check_memory_threshold():
    memory_threshold = int(input("Enter the memory threshold: "))
    current_memory = psutil.virtual_memory().percent
    print("current memory %:",current_memory)
    if current_memory > memory_threshold:
        print("memory Alert email sent!")
    else:
        print("your memory is in safe")
check_memory_threshold()