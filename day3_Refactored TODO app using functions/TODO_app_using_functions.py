tasks=[]

def show_menu():
    print("1. add tasks")
    print("2. view tasks")
    print("3. remove tasks")
    print("4. exit ")
def add_tasks():
    task= input("entr task to add")
    tasks.append(task)
    print ("tasks added")
def view_tasks():
    print("tasks are: \n")
    for i,task in enumerate(tasks):
        print(i+1,task)
def remove_task():
    try:
        index=int(input("enter task number to remove "))
        tasks.pop(index-1)
        print("task removed")
    except:
        print("invalid task number ")

while True:
    show_menu()
    choice= input("enter your choice")

    if choice == '1':
        add_tasks()
    if choice == '2':
        view_tasks()
    elif choice =='3':
        remove_task()
    
    elif choice=='4':
        print("good bye....")
        break
    else:
        print('invalid choice number')