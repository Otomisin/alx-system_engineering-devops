import requests

employee_id = "1"

# Make API requests to retrieve user information and to-do list
user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
user = user_response.json()
todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
todos = todos_response.json()

# Count completed tasks and print them out
completed_tasks = [t for t in todos if t["completed"]]
print(f"Employee {user['name']} is done with {len(completed_tasks)}/{len(todos)} tasks:")
for task in completed_tasks:
    print(f"\t {task['title']}")
