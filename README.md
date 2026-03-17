import datetime
import time
import json
import os

# Configuration
STREAK_FILE = "streak_data.json"

def load_data():
    if os.path.exists(STREAK_FILE):
        with open(STREAK_FILE, 'r') as f:
            return json.load(f)
    return {"streak_count": 0, "last_update": None}

def save_data(count, last_date):
    with open(STREAK_FILE, 'w') as f:
        json.dump({"streak_count": count, "last_update": str(last_date)}, f)

def autonomous_streak_manager():
    print("System Initialized: Automating Human Task...")
    
    while True:
        data = load_data()
        streak = data["streak_count"]
        last_update_str = data["last_update"]
        
        today = datetime.date.today()
        
        # Check if the task was already done today
        if last_update_str != str(today):
            # --- START HUMAN-LIKE TASK HERE ---
            # Example: Sending a status log or checking a sensor
            print(f"[{datetime.datetime.now()}] Performing daily automated task...")
            
            # Update Streak Logic
            streak += 1
            save_data(streak, today)
            
            print(f"Task Completed Successfully. Current Streak: {streak} days.")
            # --- END HUMAN-LIKE TASK ---
        else:
            print(f"Task already completed for {today}. Sleeping...")

        # Wait for 1 hour before checking again to save CPU resources
        time.sleep(3600) 

if __name__ == "__main__":
    autonomous_streak_manager()
