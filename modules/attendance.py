import math
from modules.utilities import read_json_file, write_json_file, ask_int

ATTENDANCE_FILE = "attendance.json"

# Formula to check how many future classes to attend to reach 75%
def calculate_recovery_classes(attended, conducted):
    if conducted == 0:
        return 0
    curr_pct = (attended / conducted) * 100.0
    if curr_pct >= 75.0:
        return 0
    # Formula: (attended + x) / (conducted + x) >= 0.75
    # x >= (0.75 * conducted - attended) / 0.25
    needed = (0.75 * conducted - attended) / 0.25
    return math.ceil(needed)

def view_attendance_report():
    records = read_json_file(ATTENDANCE_FILE)
    if not records:
        print("\nNo attendance records found.")
        return

    print("\n-----------------------------------------------------------------")
    print("Subject           Conducted   Attended   Percentage  Status")
    print("-----------------------------------------------------------------")
    for r in records:
        cond = r["conducted"]
        att = r["attended"]
        pct = 0.0
        if cond > 0:
            pct = round((att / cond) * 100.0, 2)

        status = "SAFE"
        if pct < 75.0:
            extra = calculate_recovery_classes(att, cond)
            status = "WARNING [Need +" + str(extra) + " classes]"

        sub_col = r["subject"][:16].ljust(17)
        cond_col = str(cond).ljust(11)
        att_col = str(att).ljust(10)
        pct_col = (str(pct) + "%").ljust(11)
        print(sub_col + cond_col + att_col + pct_col + status)
    print("-----------------------------------------------------------------")

def add_or_update_attendance():
    records = read_json_file(ATTENDANCE_FILE)
    print("\n--- Add / Update Attendance ---")
    sub_name = input("Subject Name: ").strip()
    if not sub_name:
        print("Subject name cannot be blank!")
        return

    cond = ask_int("Total Classes Conducted: ")
    while True:
        att = ask_int("Classes Attended: ")
        if att <= cond:
            break
        print("Error: Attended (" + str(att) + ") cannot exceed conducted (" + str(cond) + ")!")

    # Check if subject already exists
    updated = False
    for r in records:
        if r["subject"].lower() == sub_name.lower():
            r["conducted"] = cond
            r["attended"] = att
            updated = True
            break

    if not updated:
        records.append({
            "subject": sub_name,
            "conducted": cond,
            "attended": att
        })

    write_json_file(ATTENDANCE_FILE, records)
    print("Attendance for '" + sub_name + "' saved successfully.")

def run_attendance():
    while True:
        print("\n==============================")
        print("     ATTENDANCE MANAGER")
        print("==============================")
        print("1. View Attendance Status")
        print("2. Add / Update Attendance")
        print("3. Back to Main Menu")

        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            view_attendance_report()
        elif choice == "2":
            add_or_update_attendance()
        elif choice == "3":
            break
        else:
            print("Invalid option, try again.")