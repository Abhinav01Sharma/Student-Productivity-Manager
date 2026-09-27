from datetime import datetime
from modules.utilities import read_json_file, write_json_file, ask_float, ask_int

STUDY_FILE = "study_plan.json"

def show_all_study_sessions():
    sessions = read_json_file(STUDY_FILE)
    if not sessions:
        print("\nNo study plans found.")
        return

    print("\n-------------------------------------------------------------")
    print("ID   Date         Subject     Topic                Hours  Status")
    print("-------------------------------------------------------------")
    for s in sessions:
        id_str = str(s["id"]).ljust(4)
        date_str = s["date"].ljust(12)
        sub_str = s["subject"][:10].ljust(11)
        topic_str = s["topic"][:19].ljust(20)
        hrs_str = (str(s["hours"]) + "h").ljust(6)
        print(id_str + date_str + sub_str + topic_str + hrs_str + s["status"])
    print("-------------------------------------------------------------")

def add_study_session():
    sessions = read_json_file(STUDY_FILE)
    print("\n--- Plan a Study Session ---")
    sub = input("Subject: ").strip()
    topic = input("Topic name: ").strip()
    
    while True:
        date_str = input("Date (DD-MM-YYYY) or press Enter for today: ").strip()
        if date_str == "":
            date_str = datetime.now().strftime("%d-%m-%Y")
            break
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            break
        except:
            print("Please enter date as DD-MM-YYYY.")

    hours = ask_float("Planned Study Hours: ")

    new_id = 1
    if len(sessions) > 0:
        new_id = sessions[-1]["id"] + 1

    sessions.append({
        "id": new_id,
        "subject": sub,
        "topic": topic,
        "date": date_str,
        "hours": hours,
        "status": "Incomplete"
    })

    write_json_file(STUDY_FILE, sessions)
    print("Study session added successfully!")

def mark_session_completed():
    sessions = read_json_file(STUDY_FILE)
    if not sessions:
        print("\nNo study sessions logged.")
        return

    show_all_study_sessions()
    sid = ask_int("\nEnter Session ID to mark completed: ")
    
    found = False
    for s in sessions:
        if s["id"] == sid:
            s["status"] = "Completed"
            found = True
            break

    if found:
        write_json_file(STUDY_FILE, sessions)
        print("Session marked as Completed!")
    else:
        print("Session ID not found.")

def run_study_planner():
    while True:
        print("\n==============================")
        print("        STUDY PLANNER")
        print("==============================")
        print("1. View All Study Sessions")
        print("2. Add Study Session")
        print("3. Mark Session Completed")
        print("4. Back to Main Menu")

        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            show_all_study_sessions()
        elif choice == "2":
            add_study_session()
        elif choice == "3":
            mark_session_completed()
        elif choice == "4":
            break
        else:
            print("Invalid input, please try again.") 