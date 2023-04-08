import subprocess
import time

while True:
    # Execute the command to restart the tor service
    try:
        subprocess.run(['service', 'tor', 'restart'], check=True)
        print("Tor service restarted successfully")
    except subprocess.CalledProcessError:
        print("Failed to restart tor service")
    
    # Wait for 5 minutes before executing the command again
    time.sleep(300)
    
