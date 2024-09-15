to_do_tasks = []#initializing an empty list


def add_new_Task():
  newly_added_task = input("Please Enter the Task that you want to add to your to-do-List ")
  to_do_tasks.append(newly_added_task)#add the newly addes task to the empty list
  print(f"The new task ' {newly_added_task} ' is added to the list.")


def view_all_listed_tasks():
  if not to_do_tasks:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(to_do_tasks): #iterating through to_do_tasks list
      print(f"Task  {task}")

def deleteTask():
  view_all_listed_tasks() #calling the function
  try:
    to_be_deleted_task = int(input("Enter the # to delete: "))
    if to_be_deleted_task >= 0 and to_be_deleted_task < len(to_do_tasks):
      to_do_tasks.pop(to_be_deleted_task)
      print(f"Task {to_be_deleted_task} is removed successfully.")
    else:
      print(f"Sorry! Task #{to_be_deleted_task} was not found.")
  except:
    print("SORRY!Invalid input.")


if __name__ == "__main__":
  ### Creating a loop for running the app
  print("HEllo there! WELCOME to your to-do List application :)")
  while True:
    print("\n")
    print("Select from the below Options")
    print("******************************************")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List the tasks")
    print("4. Quit from the to-do-app")

    users_input = input("Enter your choice: ")

    if (users_input == "1"):
      add_new_Task()
    elif (users_input == "2"):
      deleteTask()
    elif (users_input == "3"):
      view_all_listed_tasks()
    elif (users_input == "4"):
      break
    else:
      print("Sorry! Invalid Input.TRY AGAIN")

  print("You are out from your to-do-application")#prints after exiting from the application