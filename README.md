# Student Productivity & Academic Manager

A modular Python command-line application designed to help university students track assignment deadlines, monitor attendance against the mandatory 75% threshold, and structure daily study sessions.

## Key Modules
- **Assignment Manager:** Organize assignments, set priorities, and automatically flag overdue submissions.
- **Attendance Manager:** Compute current attendance percentages and calculate remediation classes required using:
  $$\text{Remediation Classes} = \lceil \frac{0.75 \times C - A}{0.25} \rceil$$
- **Study Planner:** Schedule topic-level study blocks and evaluate daily revision goals.
- **Executive Dashboard:** Consolidated real-time summary across all coursework metrics.

## Project Structure
```text
Student_Productivity_Manager/
├── data/
│   ├── assignments.json
│   ├── attendance.json
│   └── study_plan.json
├── modules/
│   ├── __init__.py
│   ├── assignments.py
│   ├── attendance.py
│   ├── dashboard.py
│   ├── study_planner.py
│   └── utilities.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── main.py
└── └── README.md
```

## How to Run

1. Run the main application:
   ```bash
   python main.py
   ```

2. Run automated test cases:
   ```bash
   python tests/test_app.py
   ```

## Author Information
- **Student Name:** Abhinav Sharma
- **Registration No:** 26BCE10005
- **Course:** Python Programming
- **Institution:** Vellore Institute of Technology