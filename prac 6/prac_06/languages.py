from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
name_1 = "Python"
name_2 = "Ruby"
name_3 = "Visual Basic"
print(f"The dynamically typed languages are \n{python.dynamic(name_1,True)}\n{ruby.dynamic(name_2,True)}\n{visual_basic.dynamic(name_3,False)}")