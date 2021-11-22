from docxtpl import DocxTemplate

from utils import clean_input

doc = DocxTemplate("template.docx")

print("\/\/\/\/======== PROFESSIONAL RESUME BUILDER ========\/\/\/\/\n")
print("\t\t\tPERSONAL INFO\n")
print("Lets Fill in your personal details\n")
profile = {}
resume_role         = clean_input(input("\trole> "), True)
first_name          = clean_input(input("\tfirst_name> "), True)
last_name           = clean_input(input("\tlast_name> "), True)
email               = clean_input(input("\temail> "))
phone               = clean_input(input("\tphone> "))
city                = clean_input(input("\tcity e.g Lagos, Nigeria> "), True)
summary             = clean_input(input("\tSummary> "), True)

profile["role"]       = resume_role
profile["first_name"] = first_name
profile["last_name"]  = last_name
profile["phone"]      = phone
profile["email"]      = email
profile["city"]       = city


print("\t\t\tEXPERIENCES\n")
print("Lets Fill in your Work Experiences\n")
experiences = []
more_position = True
while more_position:

    job_role     = clean_input(input("\tJob Title> "), True)
    city         = clean_input(input("\tCity> "), True)
    company      = clean_input(input("\tEmployer/Company> "), True)
    print("When did you start this job?")
    start_date   = clean_input(input("\tHint: jan 2020> "), True)
    
    works_here   = input("\tDo work here currently(y/n)?> ").lower()
    if works_here in ("yes", "y", ""):
        end_date = "Current"
    else:
        print("When did you quit this job?")
        end_date = clean_input(input("\tHint: dec 2020> "), True)
        print("")

    print("\nNice! Now let's describe what you did \n Type 'd' when you are done with the accomplishments")
    tasks = []
    while True:
        task = input("\tHint: Conducted tests of components and systems to evaluate performance and identify concerns.\n\t>")
        if task.lower() in ("done", "do", "d"):
            break
        tasks.append(task)
        

    add_more_position = clean_input(input("\n\tDo you want to add another position(y/n)?> ")).lower()
    if add_more_position in ("no", "n"):
        more_position = False

    experiences.append(
        {
            "job_role":job_role,
            "city": city,
            "company": company,
            "start_date": start_date,
            "end_date": end_date, 
            "tasks": tasks,
        }
    )



print("\t\t\tEDUCATION\n")
print("Lets Fill in your educational history\n")
education = []
edu_history = True
while edu_history:

    course       = clean_input(input("\tCourse> "), True)
    location     = clean_input(input("\tLocation: e.g Akoka,Lagos> "), True)
    institution  = clean_input(input("\tSchool/Institution> "), True)
    print("When did you start?")
    start_date   = clean_input(input("\tHint: jan 2020> "), True)
    
    works_here   = input("\tDo you school here currently(y/n)> ").lower()
    if works_here in ("yes", "y", ""):
        end_date = "Current"
    else:
        print("When did you graduate?")
        end_date = clean_input(input("\tHint: dec 2020> "), True)
        print("")
  

    add_institution = clean_input(input("\n\tDo you want to add another institution(y/n)?> ")).lower()
    if add_institution in ("no", "n"):
        edu_history = False

    education.append(
        {
            "course": course,
            "location": location,
            "institution": institution,
            "start_date": start_date,
            "end_date": end_date, 
        }
    )


print("\t\t\tPROJECTS\n")
print("What projects have you take on\n")
projects = []
more_projects = True
while more_projects:

    title           = clean_input(input("\tProject Title> "), True)
    description     = clean_input(input("\tDescription> "), True)
    github_link     = clean_input(input("\tGithub Link> "))
    tech_stack      = clean_input(input("\tTech Stacks Used.e.g python,docxtpl, xml> "), True)
    live_preview    = clean_input(input("\tLive preview> "))
    

    add_projects = clean_input(input("\n\tDo you want to add another project(y/n)?> ")).lower()
    if add_projects in ("no", "n"):
        more_projects = False


    projects.append(
        {
            "title": title,
            "description": description,
            "link": github_link,
            "stack": tech_stack,
            "preview": live_preview, 
        }
    )



print("\t\t\tTECHNICAL SKILLS\n")
print("\nLets Fill in your technical skills\n\t Type 'd' when you are done with this section.")
technical_skils = []
while True:
        command = input("\tHint: Python, MySQL, PHP, scrum, Agile, AWS, Machine learning.\n\t>")
        if command.lower() == "d" or command.lower() == "done":
            break
        else:
            technical_skils.append(command)

dash = "-" * 113
context = {
    'profile'       :   profile,
    'experiences'   : experiences,
    'education'     : education,
    'tech_skills'   : technical_skils,
    'projects'      : projects,

    'dash'           : dash,
}

doc.render(context)

try:
    doc.save(f"{first_name}{last_name}.docx")
except:
    print("An error occured saving the file")
    remane = input("Remane the file to get past this error> ")
    doc.save(f"{remane}.docx")