def task():
    tasks = []
    print("WELCOME TO TO-DO LIST APPLICATION")

    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter the name of task {i}: ")
        tasks.append(task_name)

    print(f"Todays's tasks Are\n{tasks}")

    while True:
        operation = int(input("Enter 1- ADD\n2-Update\n3-Delete\n4-View\n5-Exit\nstop/"))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully.")

        elif operation == 2:
            updated_task = input("Enter the task you want to update: ")
            if updated_task in tasks:
                new_task = input("Enter the new task name: ")
                index = tasks.index(updated_task)
                tasks[index] = new_task
                print(f"Task '{updated_task}' updated to '{new_task}'.")
            else:
                print(f"Task '{updated_task}' not found in the list.")

        elif operation == 3:
            delete_task = input("Enter the task you want to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)
                print(f"Task '{delete_task}' deleted successfully.")
            else:
                print(f"Task '{delete_task}' not found in the list.")

        elif operation == 4:
            print(f"Current tasks: {tasks}")
        
        elif operation == 5:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")
        

if __name__ == "__main__":
    task()