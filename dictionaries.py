#numbers to words
def number_converter():
    phone = input("Phone: ")
    numbers = {
        "0":"zero",
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine"
    }
    output = ""
    for ch in phone:
        output += numbers.get(ch, "!") + " "
    print(output)


#emoji converter
def emoji_converter():
    message= input("> ")
    words = message.split(" ")
    emojis = {
        ":)":"😀",
        ":(":"🙁"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)

number_converter()
emoji_converter()