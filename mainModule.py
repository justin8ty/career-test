# Career Test
#
# This terminal program is developed as according to the specs
# outlined in ENGFF019's Python pair-programming assessment.
#
# Co-Authored by:
# Names: Anthony Saopa Phiri | Tan Jin Yi
# Student IDs: 20401485 | 20396553


from careerQuestions import creativeInput


def nameInput():
    print("Hello, welcome to our Career Test!")
    firstName = input("\nPlease enter your first name: ")
    lastName = input("Please enter your last name: ")
    name = firstName + " " + lastName
    programStart(name)


def programStart(name):
    print("\nHi, " + name)
    while True:
        startTest = int(
            input("\nPlease enter (1) to start the test, or (0) to end your session: ")
        )
        programRestart(startTest, name)
        continue


def programRestart(startTest, name):
    if startTest in (1, 0):
        while True:
            if startTest == 1:
                creativeInput(startTest)
                enterRestart = input(
                    "\nHooray, you have come to the end of our test session! \nPress ENTER to proceed ..."
                )
                programStart(name)
            elif startTest == 0:
                quit()


nameInput()


# Note to Dr. Reginamary:
#
# We did not implement error checking for the name, as some people may prefer to stay anonymous and use nicknames / usernames containing numbers or special characters instead.
#
# the if statement for startTest essentially functions as error checking.


# Special thanks to:
# - https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input
