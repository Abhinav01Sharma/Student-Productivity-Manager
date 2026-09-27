import sys
from modules.assignments import run_assignments
from modules.attendance import run_attendance
from modules.study_planner import run_study_planner
from modules.dashboard import show_dashboard

def main():
    while True:
        print("\n" + "="*35)
        print("    STUDENT PRODUCTIVITY MANAGER")
        print("="*35)
        print("1. Assignment Manager")
        print("2. Attendance Manager")
        print("3. Study Planner")
        print("4. Dashboard")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            run_assignments()
        elif choice == "2":
            run_attendance()
        elif choice == "3":
            run_study_planner()
        elif choice == "4":
            show_dashboard()
        elif choice == "5":
            print("\nGoodbye! Exiting application...")
            sys.exit(0)
        else:
            print("Invalid selection! Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()