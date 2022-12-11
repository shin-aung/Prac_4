names_and_emails = dict()
user_email = input("Email: ")
while user_email != "":
    emails = user_email.split("@")
    question = input(f"Is your name {emails[0].title()}? (Y/n) ").upper()
    if "N" in question:
        name_of_user = input("Name: ")
    else:
        name_of_user = emails[0]
    names_and_emails[name_of_user] = user_email
    user_email = input("Email: ")
for name_and_email in names_and_emails:
    print(name_and_email, "  ", "(", names_and_emails[name_and_email], ")")