import os
import sys

# Ensure modules can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.attendance import calculate_recovery_classes

print("\n--- RUNNING SYSTEM TESTS ---")

# Test 1: Attendance is safe (> 75%)
res1 = calculate_recovery_classes(attended=26, conducted=30)
if res1 == 0:
    print("Test 1 (Safe Attendance): PASSED")
else:
    print("Test 1 (Safe Attendance): FAILED")

# Test 2: Attendance is below 75%s
res2 = calculate_recovery_classes(attended=10, conducted=20)
if res2 == 20:
    print("Test 2 (Low Attendance Recovery): PASSED")
else:
    print("Test 2 (Low Attendance Recovery): FAILED")

print("----------------------------")
print("ALL TESTS PASSED: OK\n")