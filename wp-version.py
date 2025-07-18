import requests
userInput = input("Enter wordpress website: ")
if userInput != "":
    text = requests.get(f"{userInput.replace(" ","")}/feed")
    generator = text.text
    splitText = generator.split()

    genStart = generator.find("<generator>")
    genEnd = generator.find("</generator>")

    if genStart == -1 and genEnd == -1:
        print("Given website does not seems to be powered by Wordpress")
    else:
        version = generator[genStart:genEnd]
        print(version[version.find("v=")+ 2:])

else:
    print("Invalid input")