from docxtpl import DocxTemplate



doc = DocxTemplate("resume_template.docx")



print("\/\/\/\\/======== Professioanl Resume Builder ========\/\/\/\/")
print("PERSONAL INFO\n")
first_name          = input("first_name> ").strip()
last_name           = input("last_name> ").strip()
email               = input("email> ").strip()
phone               = input("phone> ").strip()



print("\nLets Fill in your Work Experiences\n")

more_position = True
while more_position:

    job_title   = input("Job Title> ").strip().capitalize()
    city        = input("City> ").strip().capitalize()
    employer    = input("Employer> ").strip().capitalize()
    print("When did you start this job")
    start_date  = input("Hint: jan 2020> ").strip()
    
    works_here = input("Do work here currently(y/n)> ").lower().strip()
    if works_here == "yes" or works_here == "y":
        end_date = "Current"
    else:
        print("When did you quit this job")
        end_date = input("Hint: dec 2020> ").strip()
        print("")

    print("Nice! Now let's describe what you did \n\t Type 'd' when you are done with the accomplishments")
    while True:
        task = input("Hint: Conducted tests of components and systems to evaluate performance and identify concerns.\n\t>")
        if task.lower() == "d" or task.lower() == "done":
            break
        experiences.add_tasks(task)


    
    add_more_position = input("Do you want to add another position(y/n)> ").lower().strip()
    if add_more_position == "no" or add_more_position == "n":
        more_position = False



print("\nLets Fill in the languages and tools you use\n\t Type 'd' when you are done with this section.")
lang_and_tools = []
while True:
        command = input("Hint: Conducted tests of components and systems to evaluate performance and identify concerns.\n\t>")
        if command.lower() == "d" or command.lower() == "done":
            break
        else:
            lang_and_tools.append(command)






context = {
    'first_name' : person.firstname,
    'last_name'  : person.lastname,
    'email'      : person.email_address,
    'phone'      : person.phone_number,

    'experiences': experiences.get_experiences(),

    'lang_and_tools' : lang_and_tools,
    
}





doc.render(context)

try:
    doc.save("resume.docx")
except:
    print("An error occured saving the file")
    remane = input("Remane the file to get past this error> ")
    doc.save(f"{remane}.docx")