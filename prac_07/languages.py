from prac_07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    print(ruby)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(python)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(visual_basic)

    languages = [ruby, python, visual_basic]
    print(languages)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.typing == "Dynamic":
            print("{}".format(language.name))

main()