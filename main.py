import time


def print_hello_world(text: str = "nothing") -> None:
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


if __name__ == "__main__":
    text = (input("Enter Text:"))
    
    print_hello_world(text)
