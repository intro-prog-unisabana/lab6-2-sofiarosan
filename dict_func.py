# Write your code here!
def employee_print (employee_info):
    print (f"Name: {employee_info.get('Name', 'N/A')} \n Salary: {employee_info.get ('Salary', 'N/A')} \n Role: {employee_info.get('Role', 'N/A')}")

    copia= employee_info.copy()

    copia.pop("Name", None)
    copia.pop("Salary", None)
    copia.pop("Role", None)

    if copia:
        for key, value in copia.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")

