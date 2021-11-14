#from docxtpl import DocxTemplate

from utils import input_processor

#doc = DocxTemplate("resume_template.docx")



print("\/\/\/\\/======== Professioanl Resume Builder ========\/\/\/\/\n")
print("\t\t\tPERSONAL INFO\n")
print("Lets Fill in your personal details\n")
personal_info = {}
#resume_role         = input_processor(input("role> "), True)
#first_name          = input_processor(input("first_name> "), True)
#last_name           = input_processor(input("last_name> "), True)
#email               = input_processor(input("email> "))
#phone               = input_processor(input("phone> "))

#personal_info["role"]           = resume_role
#personal_info["first_name"]     = first_name
#personal_info["last_name"]      = last_name
#personal_info["phone"]          = phone
#personal_info["email"]          = email

#print(personal_info)

print("\t\t\tEXPERIENCES\n")
print("Lets Fill in your Work Experiences\n")
experiences = []
more_position = True
while more_position:

    job_role    = input_processor(input("Job Title> "), True)
    city        = input_processor(input("City> "), True)
    company    = input_processor(input("Employer/Company> "), True)
    print("When did you start this job?")
    start_date  = input_processor(input("Hint: jan 2020> "), True)
    
    works_here  = input("Do work here currently(y/n)> ").lower()
    if works_here in ("yes", "y", ""):
        end_date = "Current"
    else:
        print("When did you quit this job")
        end_date = input("Hint: dec 2020> ")
        print("")

    print("Nice! Now let's describe what you did \n\t Type 'd' when you are done with the accomplishments")
    tasks = []
    while True:
        task = input("Hint: Conducted tests of components and systems to evaluate performance and identify concerns.\n\t>")
        if task.lower() in ("done", "do", "d"):
            break
        tasks.append(task)
        

    add_more_position = input("Do you want to add another position(y/n)> ").lower().strip()
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

print(experiences)