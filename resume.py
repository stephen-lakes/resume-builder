from docxtpl import DocxTemplate

from utils import input_processor, capitalize_sentence

doc = DocxTemplate("resume_template.docx")

print("\/\/\/\/======== Professioanl Resume Builder ========\/\/\/\/\n")
print("\t\t\tPERSONAL INFO\n")
print("Lets Fill in your personal details\n")
personal_info = {}
resume_role         = capitalize_sentence(input_processor(input("\trole> "), True))
first_name          = input_processor(input("\tfirst_name> "), True)
last_name           = input_processor(input("\tlast_name> "), True)
email               = input_processor(input("\temail> "))
phone               = input_processor(input("\tphone> "))
city                = input_processor(input("\tcity> "))

personal_info["role"]       = resume_role
personal_info["first_name"] = first_name
personal_info["last_name"]  = last_name
personal_info["phone"]      = phone
personal_info["email"]      = email

'''

print("\t\t\tEXPERIENCES\n")
print("Lets Fill in your Work Experiences\n")
experiences = []
more_position = True
while more_position:

    job_role     = input_processor(input("\tJob Title> "), True)
    city         = input_processor(input("\tCity> "), True)
    company      = input_processor(input("\tEmployer/Company> "), True)
    print("When did you start this job?")
    start_date   = input_processor(input("\tHint: jan 2020> "), True)
    
    works_here   = input("\tDo work here currently(y/n)> ").lower()
    if works_here in ("yes", "y", ""):
        end_date = "Current"
    else:
        print("When did you quit this job")
        end_date = input("\tHint: dec 2020> ")
        print("")

    print("\nNice! Now let's describe what you did \n Type 'd' when you are done with the accomplishments")
    tasks = []
    while True:
        task = input("\tHint: Conducted tests of components and systems to evaluate performance and identify concerns.\n\t>")
        if task.lower() in ("done", "do", "d"):
            break
        tasks.append(task)
        

    add_more_position = input_processor(input("\tDo you want to add another position(y/n)> ")).lower()
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
'''

print("\t\t\tEDUCATION\n")
print("Lets Fill in your educational history\n")
education = []
edu_history = True
while edu_history:

    course       = input_processor(input("\tCourse> "), True)
    location     = input_processor(input("\tLocation> "), True)
    institution  = capitalize_sentence(input_processor(input("\tSchool/Institution> "), True))
    print("When did you start?")
    start_date   = input_processor(input("\tHint: jan 2020> "), True)
    
    works_here   = input("\tDo you school here currently(y/n)> ").lower()
    if works_here in ("yes", "y", ""):
        end_date = "Current"
    else:
        print("When did you graduate")
        end_date = input("\tHint: dec 2020> ")
        print("")
  

    add_institution = input_processor(input("\tDo you want to add another institution(y/n)> ")).lower()
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

print(education)



print("\t\t\tTECHNICAL SKILLS\n")
print("\nLets Fill in your technical skills\n\t Type 'd' when you are done with this section.")
technical_skils = []
while True:
        command = input("\tHint: Python, MySQL, PHP, scrum, Agile, AWS, Machine learning.\n\t>")
        if command.lower() == "d" or command.lower() == "done":
            break
        else:
            technical_skils.append(command)


context = {
    'role'          : resume_role,
    'first_name'    : first_name,
    'last_name'     : last_name,
    'email'         : email,
    'phone'         : phone,
    'city'          : city,
    #'experiences'   : experiences,
    'education'     : education,
    'tech_skills'   : technical_skils,
}





doc.render(context)

try:
    doc.save("resume.docx")
except:
    print("An error occured saving the file")
    remane = input("Remane the file to get past this error> ")
    doc.save(f"{remane}.docx")