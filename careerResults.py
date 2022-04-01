# Q7 - Career Test
#
# This project is developed as according to the specs
# outlined in ENGFF019's Python pair programming assessment.
#
# Co-Authored by:
# Names: Anthony Saopa Phiri | Tan Jin Yi
# Student IDs: 20401485 | 20396553


creativeCareer = ["Graphics Designer, Photographer, or Comedian."]
stemCareer = ["Software Developer, Scientist, or Data Analyst."]
laborCareer = ["Pilot, Carpenter, or Social Worker."]


def careerOutput1(creativeChoice, stemChoice, laborChoice):
    for i in creativeCareer:
        if (creativeChoice + stemChoice + laborChoice > 0) and (
            creativeChoice > stemChoice or creativeChoice > laborChoice
        ):
            print("\nBased on your answers, we think you'd enjoy being a", i)


def careerOutput2(creativeChoice, stemChoice, laborChoice):
    for i in stemCareer:
        if (creativeChoice + stemChoice + laborChoice > 0) and (
            stemChoice > creativeChoice or stemChoice > laborChoice
        ):
            print("\nBased on your answers, we think you'd enjoy being a", i)


def careerOutput3(creativeChoice, stemChoice, laborChoice):
    for i in laborCareer:
        if (creativeChoice + stemChoice + laborChoice > 0) and (
            laborChoice > creativeChoice or laborChoice > stemChoice
        ):
            print("\nBased on your answers, we think you'd enjoy being a", i)


def careerOutput4(creativeChoice, stemChoice, laborChoice):
    if (
        (creativeChoice + stemChoice + laborChoice > 0)
        and (creativeChoice == stemChoice and creativeChoice == laborChoice)
    ) or (creativeChoice + stemChoice + laborChoice == 0):
        print(
            "\nUnfortunately, we do not have suitable careers based on your answers. We will keep improving on the test in the future!"
        )


# This module can be implemented more efficiently using a single function,
# but we decided to follow the required specs.
