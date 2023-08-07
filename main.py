import functions
import time

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_task()

        todos.append(todo + '\n')

        functions.write_task(todos)

    elif user_action.startswith('show'):

        todos = functions.get_task()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif    user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_task()

            new_todo = input("Enter a new task: ")
            todos[number] = new_todo + '\n'

            functions.write_task(todos)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_task()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_task(todos)

            message = f"Task {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no task with that number.")
            continue
    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid Command")

print("Bye")

