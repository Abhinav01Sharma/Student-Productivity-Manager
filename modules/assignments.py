from datetime import datetime
from modules.utilities import read_json_file, write_json_file, ask_int

ASSIGNMENT_FILE = "assignments.json"

# Check if a date string in DD-MM-YYYY has already passed
def check_if_overdue(deadline_str, status):
    if status.lower() == "completed":
        return False
    try:
        deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y").date()
        today = datetime.now().date()
        return deadline_date < today
    except:
        return False

def show_all_assignments():
    tasks = read_json_file(ASSIGNMENT_FILE)
    if not tasks:
        print("\nNo assignments added yet.")
        return

    print("\n--------------------------------------------------------------")
    print("ID   Subject       Assignment Name      Deadline    Priority  Status")
    print("--------------------------------------------------------------")
    for t in tasks:
        status_text = t["status"]
        if check_if_overdue(t["deadline"], t["status"]):
            status_text = "OVERDUE"
        
        # Simple spacing using ljust
        id_str = str(t["id"]).ljust(4)
        sub = t["subject"][:12].ljust(13)
        name = t["name"][:19].ljust(20)
        dead = t["deadline"].ljust(11)
        prio = t["priority"].ljust(9)
        print(id_str + sub + name + dead + prio + status_text)
    print("--------------------------------------------------------------")

def add_new_assignment():
    tasks = read_json_file(ASSIGNMENT_FILE)
    print("\n--- Add New Assignment ---")
    name = input("Assignment Title: ").strip()
    if not name:
        print("Title cannot be empty!")
        return

    sub = input("Subject: ").strip()
    
    # Simple date check
    while True:
        dead = input("Deadline (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(dead, "%d-%m-%Y")
            break
        except:
            print("Wrong format! Please use DD-MM-YYYY (e.g. 30-10-2026).")

    print("Choose Priority: 1. High  2. Medium  3. Low")
    p_choice = input("Enter choice (1-3): ").strip()
    prio = "Medium"
    if p_choice == "1":
        prio = "High"
    elif p_choice == "3":
        prio = "Low"

    # Find the next ID
    new_id = 1
    if len(tasks) > 0:
        new_id = tasks[-1]["id"] + 1

    new_task = {
        "id": new_id,
        "name": name,
        "subject": sub,
        "deadline": dead,
        "priority": prio,
        "status": "Pending"
    }
    tasks.append(new_task)
    write_json_file(ASSIGNMENT_FILE, tasks)
    print("Assignment added successfully!")

def mark_assignment_done():
    tasks = read_json_file(ASSIGNMENT_FILE)
    if not tasks:
        print("\nNo assignments to update.")
        return

    show_all_assignments()
    task_id = ask_int("\nEnter the ID of the assignment to mark completed: ")
    
    found = False
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Completed"
            found = True
            break
            
    if found:
        write_json_file(ASSIGNMENT_FILE, tasks)
        print("Assignment marked as completed!")
    else:
        print("ID not found.")

def run_assignments():
    while True:
        print("\n==============================")
        print("     ASSIGNMENT MANAGER")
        print("==============================")
        print("1. View All Assignments")
        print("2. Add Assignment")
        print("3. Mark Assignment as Done")
        print("4. Back to Main Menu")
        
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            show_all_assignments()
        elif choice == "2":
            add_new_assignment()
        elif choice == "3":
            mark_assignment_done()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")