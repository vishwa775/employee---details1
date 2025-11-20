import sys

if len(sys.argv) != 5:
    print("Usage: python employee.py <emp_id> <emp_name> <emp_salary> <emp_exp>")
    sys.exit()

emp_id = sys.argv[1]
emp_name = sys.argv[2]
emp_salary = sys.argv[3]
emp_exp = sys.argv[4]

print("\n--- Employee Details ---")
print("ID:", emp_id)
print("Name:", emp_name)
print("Salary:", emp_salary)
print("Experience:", emp_exp, "years")