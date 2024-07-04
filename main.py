import time


def print_english(text: str) -> None:
    printed_text = ""

    for j in range(len(text)):
        time.sleep(0.1)
        current_char = text[j]
        for i in range(97, 122 + 1):
            time.sleep(0.05)
            letter = chr(i)
            print(printed_text + letter)
            if letter == current_char:
                printed_text += letter
                break
            elif current_char == ' ':
                printed_text += ' '
                break


def print_russian(text: str) -> None:
    printed_text = ""

    for j in range(len(text)):
        time.sleep(0.1)
        current_char = text[j]
        for i in range(1072, 1103 + 1):
            time.sleep(0.05)
            letter = chr(i)
            print(printed_text + letter)
            if letter == current_char:
                printed_text += letter
                break
            elif current_char == ' ':
                printed_text += ' '
                break





if __name__ == "__main__":
    while True:
        print("Choose Language:")
        time.sleep(0.1)
        print("English: E")
        time.sleep(0.1)
        print("Russian: R")
        time.sleep(0.1)
        language = input("E/R: ")
        time.sleep(0.1)
        if language in ["R", "r", "Russian", "Rus", "rus", "russian", "E", "e", "English", "english", "eng", "Eng"]:
            break
        print("WRONG DATA")
        time.sleep(0.1)
    while True:
        text_to_print = (input("Enter Text: "))
        if text_to_print:
            break
        print("ENTER TEXT!")
    if language in ["R", "r", "Russian", "Rus", "rus", "russian"]:
        print_russian(text_to_print)
    elif language in ["E", "e", "English", "english", "eng", "Eng"]:
        print_english(text_to_print)

    

