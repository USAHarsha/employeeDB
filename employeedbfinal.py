def create_employee(emp_id, first_name, last_name, dept_name):
    return {
        "emp_id": emp_id,
        "first_name": first_name,
        "last_name": last_name,
        "dept_name": dept_name
    }


def add_employee(employees, emp_id, first_name, last_name, dept_name):
    employees.append(create_employee(emp_id, first_name, last_name, dept_name))

def update_employee(employees, emp_id, first_name, last_name, dept_name):
    for employee in employees:
        if employee["emp_id"] == emp_id:
            employee["first_name"] = first_name
            employee["last_name"] = last_name
            employee["dept_name"] = dept_name
            print("Employee record updated Successfully.")
            return
    print("No Employee found.")

def delete_employee(employees, emp_id):
    for employee in employees:
        if employee["emp_id"] == emp_id:
            employees.remove(employee)
            print("Employee record deleted successfully.")
            return
    print("No Employee found.")

def view_all_employees(employees):
    if employees:
        print("Employee Records:")
        for employee in employees:
            print(f"ID: {employee['emp_id']}, Name: {employee['first_name']} {employee['last_name']}, Department Name: {employee['dept_name']}")
    else:
        print("No employee records found.")

def search_employee_by_name(employees, name):
    success = False
    for employee in employees:
        if name.lower() in employee['first_name'].lower() or name.lower() in employee['last_name'].lower():
            print(f"ID: {employee['emp_id']}, Name: {employee['first_name']} {employee['last_name']}, Department Name: {employee['dept_name']}")
            success = True
    if not success:
        print("Employee not found.")
def main():
    employees = []
    while True:
        print("\n\n\nEmployee Database Application")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View All Employees")
        print("5. Search By Employee name")
        print("6. Exit program")

        selection = input("Enter your selection (1-6): ")
        if selection == '1':
            emp_id = input("Enter employee ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            dept_name = input("Enter department name: ")
            add_employee(employees, emp_id, first_name, last_name, dept_name)
        elif selection == '2':
            emp_id = input("Enter employee ID to update: ")
            first_name = input("Enter updated first name: ")
            last_name = input("Enter updated last name: ")
            dept_name = input("Enter updated department name: ")
            update_employee(employees, emp_id, first_name, last_name, dept_name)
        elif selection == '3':
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(employees, emp_id)
        elif selection == '4':
            view_all_employees(employees)
        elif selection == '5':
            name = input("Enter first or last name to search for an employee: ")
            search_employee_by_name(employees, name)
        elif selection == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()