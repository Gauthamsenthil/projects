import time
import sys

def fake_shutdown():
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
    sys.exit()

# Run the fake shutdown
fake_shutdown()
