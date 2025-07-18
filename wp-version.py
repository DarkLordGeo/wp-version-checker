import requests
userInput = input("Enter wordpress website: ")
if userInput:
    text = requests.get(f"{userInput.replace(" ","")}/feed")
    generator = text.text
    splitText = generator.split()
    genStart = generator.find("<generator>")
    genEnd = generator.find("</generator>")
    version = generator[genStart:genEnd]
    print(version[version.find("v=")+ 2:])


