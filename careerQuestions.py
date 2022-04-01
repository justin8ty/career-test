# Co-Authored by:
# Names: Anthony Saopa Phiri | Tan Jin Yi
# Student IDs: 20401485 | 20396553


from careerResults import careerOutput1
from careerResults import careerOutput2
from careerResults import careerOutput3
from careerResults import careerOutput4


def creativeInput(startTest):
    while startTest == 1:
        while True:
            print(
                "\nInstructions:\nEnter (1) if you agree. \nEnter (0) if you disagree."
            )
            creativeChoice1 = int(
                input("\nWould you enjoy designing a magazine cover? \nAnswer: ")
            )
            if creativeChoice1 in (0, 1):
                break
        while True:
            creativeChoice2 = int(
                input("\nWould you enjoy taking pictures of nature? \nAnswer: ")
            )
            if creativeChoice2 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        while True:
            creativeChoice3 = int(
                input(
                    "\nDoes illustrating a children's book sounds interesting to you? \nAnswer: "
                )
            )
            if creativeChoice3 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        creativeChoice = creativeChoice1 + creativeChoice2 + creativeChoice3
        return stemInput(startTest, creativeChoice)


def stemInput(startTest, creativeChoice):
    while startTest == 1:
        while True:
            stemChoice1 = int(
                input("\nDo scientific experiments interest you? \nAnswer: ")
            )
            if stemChoice1 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        while True:
            stemChoice2 = int(
                input(
                    "\nDoes researching a new medicine sound attractive to you? \nAnswer: "
                )
            )
            if stemChoice2 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        while True:
            stemChoice3 = int(
                input("\nDo you enjoy analyzing a molecular structure? \nAnswer: ")
            )
            if stemChoice3 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        stemChoice = stemChoice1 + stemChoice2 + stemChoice3
        return laborInput(startTest, creativeChoice, stemChoice)


def laborInput(startTest, creativeChoice, stemChoice):
    while startTest == 1:
        while True:
            laborChoice1 = int(
                input("\nWould you enjoy installing a hardwood floor? \nAnswer: ")
            )
            if laborChoice1 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        while True:
            laborChoice2 = int(
                input(
                    "\nDo you enjoy assembling DIY (DO-IT-YOURSELF) products? \nAnswer: "
                )
            )
            if laborChoice2 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        while True:
            laborChoice3 = int(
                input("\nDo you like to repair an Air Conditioning system? \nAnswer: ")
            )
            if laborChoice3 in (0, 1):
                break
            print("Please enter (1) if you agree, or (0) if you disagree.")
        laborChoice = laborChoice1 + laborChoice2 + laborChoice3

        print(
            "\nYou've finished the test. Below are your final scores for: ",
            "\nCreative Career: ",
            creativeChoice,
            "\nSTEM Career: ",
            stemChoice,
            "\nLabor Career: ",
            laborChoice,
        )
        careerOutput1(creativeChoice, stemChoice, laborChoice)
        careerOutput2(creativeChoice, stemChoice, laborChoice)
        careerOutput3(creativeChoice, stemChoice, laborChoice)
        return careerOutput4(creativeChoice, stemChoice, laborChoice)
