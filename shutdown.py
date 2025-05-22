import time
import sys

def fake_shutdown():
    user_input = input("Do you want to shut down the system? (yes/no): ").strip().lower()

    if user_input == "yes":
        print("Shutting down...")
        time.sleep(2)
        print("Closing background processes...")
        time.sleep(2)
        print("Saving system state...")
        time.sleep(2)
        print("System will shut down now.")
        time.sleep(3)
        print("...")
        time.sleep(2)
    
    elif user_input == "no":
        print("Shutdown aborted. System will continue running.")
    
    else:
        print("Sorry, invalid input.")

# Run the fake shutdown
fake_shutdown()
