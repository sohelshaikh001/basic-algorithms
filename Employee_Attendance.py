# Employee Attendance Management System

employees = [
    (101, "Alice Johnson", "HR"),
    (102, "Bob Smith", "IT"),
    (103, "Charlie Brown", "Finance"),
    (104, "David White", "IT"),
    (105, "Eve Black", "Marketing")
]

attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Present"),
    (105, "2025-03-01", "Absent"),
]

def mark_attendance(employee_id, date, status):
    attendance_records.append((employee_id, date, status))
    print(f"Attendance marked for Employee {employee_id} on {date}: {status}")

def search_attendance(employee_id):
    records = [record for record in attendance_records if record[0] == employee_id]
    if records:
        print(f"Attendance records for Employee {employee_id}:")
        for record in records:
            print(f"Date: {record[1]}, Status: {record[2]}")
    else:
        print(f"No records found for Employee {employee_id}.")


# Example Usage
mark_attendance(101, "2025-03-02", "Present")
search_attendance(101)
search_attendance(102)
