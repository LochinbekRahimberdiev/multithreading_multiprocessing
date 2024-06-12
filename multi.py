import threading
import time
import threading
import time
def thread_task(thread_number):
    time.sleep(thread_number)
    print(f"Thread {thread_number} finished")

threads = []
for i in range(8):
    thread = threading.Thread(target=thread_task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished.")


def thread_task(thread_number):
    time.sleep(thread_number)
    print(f"Thread {thread_number} finished")

threads = []
for i in range(8):
    thread = threading.Thread(target=thread_task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished.")

