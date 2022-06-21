Start = input("Would You Like To Start This Game? Type Yes/No")

if Start == "Yes" or Start == "yes"  or Start == "YES":

    

    colour = input("Enter a Colour :")

    animal = input("Enter an Animal :")

    noun1 = input("Enter a Noun :")

    noun2 = input("Enter a Noun :")

    action = input("Enter an Action in Past Tense :")

    story = "Once upon a time there was a " + colour + " " + animal + " that walked \n out of a " + noun1 + " and then it saw a " + noun2 + " and then it " + action + " ."
    print("\n ===== (>v<) ===== \n")
    print(story)

else:
    print("Goodbye")
