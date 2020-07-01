#programm by Hamid
#programm to reverse word in a string

string = "class math my to subscribe"

def  reverseString(s):
    wordArray =s.split(" ")
    output = []
    for word in wordArray:
        output.insert(0.word)
    return  " " .join(output)

print(reverseString(string))