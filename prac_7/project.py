from project_management import Project
projects = []
in_file = open("project.csv", "r")
in_file.readline()
for line in in_file:
    line = line.strip().split(f"\t")
    name = line[0]
    start_date = line[1]
    priority = line[2]
    estimated_cost = line[3]
    completion_percentage = line[4]
    project = Project(name, start_date, int(priority), float(estimated_cost), int(completion_percentage))
    projects.append(project)
in_file.close()
CHOICES = f"- (L)oad projects \n (S)ave projects \n (D)isplay projectsn \n (F)ilter projects by date \n (A)dd new project (U)pdate project \n (Q)uit"
print(CHOICES)
choice = input(">>>  ").upper()
while choice != "Q":
    if choice == "D":
        for project in projects:
            if project.completion_percentage != 100:
                print("Imcomplete projects")
                print(project)
            else:
                print("Completed projects:")
                print(project)
    elif choice == "U":
        for i in (0, len(projects), 1):
            for project in projects:
                    print(f"{i} {project}")
        project_choice = input(int("Project choice: "))
        print(projects[project_choice])
        new_percentage = input(int("New Percentage: "))
        new_priority = input(int("New Priority: "))
    elif choice == "A":
        print("Let's add a new project")
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = input(int("Priority: "))
        estimated_cost = input(float("Cost estimate: $"))
        completion_percentage = input(int("Percent complete: "))
        project = Project(name, start_date, int(priority), float(estimated_cost), int(completion_percentage))
        projects.append(project)
        out_file = open("project.csv", "a")
        print(f"{name}\t{start_date}\t{priority}\t{estimated_cost}\t{completion_percentage}", file=out_file)
        out_file.close()
    elif choice == "F":
        filter_date = input("Show projects that start after date(dd/mm/yy): ")
        projects.sort()
        for project in projects:
            if project.start_date >= filter_date:
                print(project)
    else:
        print("try again")
    choice = input(">>>  ").upper()
print("Thank you for using custom-built project management software.")