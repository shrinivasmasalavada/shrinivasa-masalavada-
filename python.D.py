# Simple Task Management System

def show_tasks(task_list):
    if not task_list:
        print("\nYour task list is empty!")
    else:
        print("\n--- Your Current Tasks ---")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []
    
    while True:
        print("\n1. Add Task")
        print(2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            new_task = input("Enter the task name: ")
            tasks.append(new_task)
            print("Task added successfully!")
            
        elif choice == '2':
            show_tasks(tasks)
            
        elif choice == '3':
            show_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed task: {removed}")
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Please enter a valid number.")
            
        elif choice == '4':
            print("Exiting the program. Good luck with your Deloitte program!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()