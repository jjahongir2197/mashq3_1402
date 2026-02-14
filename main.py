class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.done = False

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline):
        self.tasks.append(Task(title, deadline))

    def mark_done(self, index):
        self.tasks[index].done = True

    def show_tasks(self):
        for i, t in enumerate(self.tasks):
            status = "✔" if t.done else "❌"
            print(f"{i+1}. {t.title} | {t.deadline} | {status}")

def run():
    todo = Todo()

    while True:
        print("\n1. Task qo‘shish\n2. Bajarildi\n3. Tasklar\n4. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            todo.add_task(input("Nomi: "), input("Deadline: "))
        elif c == "2":
            todo.show_tasks()
            i = int(input("Tanlang: ")) - 1
            todo.mark_done(i)
        elif c == "3":
            todo.show_tasks()
        elif c == "4":
            break

run()
