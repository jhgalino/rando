# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytodotxt
import argparse
import random
import time
import sys

parser = argparse.ArgumentParser()
_ = parser.add_argument("todotxt", help="location of todo.txt file")
_ = parser.add_argument("-i", "--ignore", help="names of projects to ignore", nargs="*")
args = parser.parse_args()
if not args.ignore:
    args.ignore = []

todotxt = pytodotxt.TodoTxt(args.todotxt)
todotxt.parse()

# contains mapping of number of tickets per letter from a to z
TICKETS_BY_LETTER: dict[str, int] = dict(
    zip(
        [chr(i).upper() for i in range(ord("a"), ord("z") + 1)],
        [2**x for x in range(28, 2, -1)],
    )
)

# associate tickets with each task
total_tickets = 0
for task in todotxt.tasks:
    if task.is_completed:
        continue

    if task.priority is not None:
        task.ticket = TICKETS_BY_LETTER[task.priority]
        total_tickets += TICKETS_BY_LETTER[task.priority]
    else:
        task.ticket = 2**2
        total_tickets += 2**2

random.seed = time.time()
picked_ticket = random.randint(0, total_tickets)

# check if a task with priority is picked. if not, then we proceed
# with picking an unprioritized task from the projects.
counter = 0
for task in todotxt.tasks:
    if task.is_completed:
        continue

    counter += task.ticket
    if counter >= picked_ticket and task.priority is not None:
        print(task)
        sys.exit()


# get the set of all projects not being ignored.
# a task can have multiple projects, thus we need to iterate over all tasks in
# the todotxt file to get all projects
projects = set(
    project
    for task in todotxt.tasks
    for project in task.projects
    if project not in args.ignore
)

# # create a dictionary with each non-ignored project as key and a list of tasks
# # associated with it as the value
tasks_per_project = {
    project: [
        task
        for task in todotxt.tasks
        if project in task.projects and not task.is_completed
    ]
    for project in projects
}

# # get only projects with tasks
tasks_per_project = {
    project: tasks for project, tasks in tasks_per_project.items() if len(tasks) != 0
}

if len(tasks_per_project) == 0:
    raise Exception("All tasks are currently completed. No task can be given.")

chosen_project = random.choice(list(tasks_per_project.keys()))
tasks = tasks_per_project[chosen_project]

random.seed = time.time()

print(random.choice(tasks))
