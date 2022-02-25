import playsound
loop = 1


while loop == 1:
    answer = input("What color is the rain?, purple, blue or brown? ")

    if answer == "purple":
        playsound("C:\Soundfiles\purplerain.mp3")
        loop = 0

    elif answer == "blue":
        playsound("C:\Soundfiles\Beatlerain.mp3")
        loop = 0

    elif answer == "brown":
        playsound("C:\Soundfiles\chocolaterain.mp3")
    loop = 0

else:
    print("Say something valid")