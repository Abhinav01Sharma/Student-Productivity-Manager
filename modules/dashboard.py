from datetime import datetime
from modules.utilities import read_json_file
from modules.assignments import check_if_overdue

def show_dashboard():
    assignments = read_json_file("assignments.json")
    attendance = read_json_file("attendance.json")
    study_plan = read_json_file("study_plan.json")

    print("\n=============================================")
    print("         ACADEMIC DASHBOARD OVERVIEW")
    print("=============================================")

    # 1. Assignment Stats
    pending_cnt = 0
    completed_cnt = 0
    overdue_cnt = 0

    for a in assignments:
        if a["status"].lower() == "completed":
            completed_cnt += 1
        else:
            pending_cnt += 1
            if check_if_overdue(a["deadline"], a["status"]):
                overdue_cnt += 1

    print("\n[ASSIGNMENT SUMMARY]")
    print("   * Pending   : " + str(pending_cnt))
    print("   * Completed : " + str(completed_cnt))
    print("   * Overdue   : " + str(overdue_cnt))

    # 2. Attendance Stats
    print("\n[ATTENDANCE SUMMARY]")
    if not attendance:
        print("   * No attendance logged.")
    else:
        for att in attendance:
            cond = att["conducted"]
            done = att["attended"]
            pct = 0.0
            if cond > 0:
                pct = round((done / cond) * 100.0, 1)

            if pct >= 75.0:
                print("   * " + att["subject"] + ":  " + str(pct) + "%  [SAFE]")
            else:
                print("   * " + att["subject"] + ":  " + str(pct) + "%  [WARNING (<75%)]")

    # 3. Today's Study Stats
    today_str = datetime.now().strftime("%d-%m-%Y")
    total_tasks = 0
    target_time = 0.0
    finished_time = 0.0

    for s in study_plan:
        if s["date"] == today_str:
            total_tasks += 1
            target_time += s["hours"]
            if s["status"].lower() == "completed":
                finished_time += s["hours"]

    print("\n[TODAY'S STUDY TARGETS (" + today_str + ")]")
    print("   * Total Tasks : " + str(total_tasks))
    print("   * Target Time : " + str(target_time) + " hrs")
    print("   * Finished    : " + str(finished_time) + " hrs")
    print("=============================================")
    input("\nPress Enter to return to main menu...")   