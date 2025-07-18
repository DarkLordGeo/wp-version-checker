import requests
# import re
userInput = input("Enter wordpress website: ")
if userInput:
    text = requests.get(f"{userInput.replace(" ","")}/feed")
    generator = text.text
    # generatorSrc = re.findall("<generator>",generator)
    splitText = generator.split()
    genStart = generator.find("<generator>")
    genEnd = generator.find("</generator>")
    version = generator[genStart:genEnd]
    print(version[version.find("v=")+ 2:])


