tasks = []


def AddTask(newTask):
    tasks.append(newTask)


def RemoveTask(task):
    removed = False
    while task in tasks:
        tasks.remove(task)
        removed = True

    if removed:
        print("Task Removed Successfully")
    else:
        print("No Such Task in the list")



def ViewAllTasks():
    print(f"Following are all the tasks added: ")
    i = 1
    for task in tasks:
        print(f"Task {i}: {task}")
        i += 1


AddTask("Finish assignment 3")
AddTask("Submit assignment 3")
AddTask("Submit output screenshots")

ViewAllTasks()

RemoveTask("Do the dishes")
RemoveTask("Finish assignment 3")

ViewAllTasks()