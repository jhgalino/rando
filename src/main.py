import pytodotxt, argparse, random

parser = argparse.ArgumentParser()
parser.add_argument("todotxt", help="location of todo.txt file")
parser.add_argument("-i", "--ignore", help="projects to ignore", nargs="*")
args = parser.parse_args()

todotxt = pytodotxt.TodoTxt(args.todotxt)
todotxt.parse()

projects = set(
    project
    for task in todotxt.tasks
    for project in task.projects
    if project not in args.ignore
)

num_tasks_in_projects = [
    len(
        [
            task
            for task in todotxt.tasks
            if project in task.projects and not task.is_completed
        ]
    )
    for project in projects
]
print(num_tasks_in_projects)
if all(num == 0 for num in num_tasks_in_projects):
    raise Exception("All tasks are currently ignored.")

tasks_under_project = []
while len(tasks_under_project) == 0:
    chosen_project = random.choice(list(projects))
    tasks_under_project = [
        task
        for task in todotxt.tasks
        if chosen_project in task.projects and not task.is_completed
    ]

print(random.choice(tasks_under_project))
