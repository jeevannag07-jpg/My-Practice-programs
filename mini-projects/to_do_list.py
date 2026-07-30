tasks=[]
while True:
    print("........TO DO LIST........")
    print("1.add task")
    print("2. remove atask")
    print("3.view task")
    print("4.exit")


    choice=int(input("enter your choice:"))


    #add task
    if choice==1:
        task=input("enter a task")
        tasks.append(task)
        print("y0our task has been added succesfully")

    #VIEW TASK
    elif choice==2:
        if len(tasks==0):
            print("sorry there are no tasks ")
        else:
            print("your tasks are")
            for i in len(tasks):
                print(i+1,".",tasks[i])

    elif choice==3:
        if len(tasks)==0:
            print("there ae no tasks to remove")
        else:
            print("your tasks")
            for i in len(tasks):
                print(i+1,".",tasks[i])
                remove_index=input("enter your tasks to be removed")
                if remove_index>0 and remove_index<len(tasks):
                    removed_task=tasks.pop(remove_index-1)
                    print(removed_task,"removed succesfully")
                else:
                 print("invalid number") 
    elif choice==4:
        print("exiting the list...")
        break
    else:
        print("INVALID CHOICE")