# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytodotxt, argparse, random

parser = argparse.ArgumentParser()
parser.add_argument("todotxt", help="location of todo.txt file")
parser.add_argument("-i", "--ignore", help="projects to ignore", nargs="*")
args = parser.parse_args()
if not args.ignore:
	args.ignore = []

todotxt = pytodotxt.TodoTxt(args.todotxt)
todotxt.parse()

# get the set of all projects not being ignored.
# a task can have multiple projects, thus we need to iterate over all tasks in
# the todotxt file to get all projects
projects = set(
    project
    for task in todotxt.tasks
    for project in task.projects
    if project not in args.ignore
)

# create a dictionary with each non-ignored project as key and a list of tasks
# associated with it as the value
tasks_per_project = {
    project: [
        task
        for task in todotxt.tasks
        if project in task.projects and not task.is_completed
    ]
    for project in projects
}

# get only projects with non-completed tasks
tasks_per_project = {
    project: tasks for project, tasks in tasks_per_project.items() if len(tasks) != 0
}

if len(tasks_per_project) == 0:
	raise Exception("All tasks are currently completed. No task can be given.")

chosen_project = random.choice(list(projects))
tasks = tasks_per_project[chosen_project]

print(random.choice(tasks))
