leet_dict = {
        "a":"4",
        "b":"I3",
        "c":"[",
        "d":")",
        "e":"3",
        "f":"|=",
        "g":"&",
        "h":"#",
        "i":"1",
        "j":",_|",
        "k":">|",
        "l":"1",
        "m":"/\\/\\",
        "n":"^/",
        "ñ":"ñ",
        "o":"0",
        "p":"|*",
        "q":"(_,)",
        "r":"I2",
        "s":"5",
        "t":"7",
        "u":"(_)",
        "v":"\\/",
        "w":"\\/\\/",
        "x":"><",
        "y":"j",
        "z":"2",
        "1":"L",
        "2":"R",
        "3":"E",
        "4":"A",
        "5":"S",
        "6":"b",
        "7":"T",
        "8":"B",
        "9":"g",
        "0":"o"
    }

def transform(text):
    for letter in text.lower():
        if letter in leet_dict:
            text = text.replace(letter, leet_dict[letter])
    print(text)

if __name__ == "__main__":
    transform(input("Introduzca un texto para encriptar"))