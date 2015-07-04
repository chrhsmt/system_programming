import re

def verb_post(word):
    if (word.endswith("y")):
        r1 = re.compile(r'^.*[a|i|u|e|o]+y$')
        if (r1.match(word)):
            return word + "ed"
        else:
            return word[0:-1] + "id"
    elif (word.endswith("c")):
        return word + "ked"
    elif (exceptional(word) != None):
        return exceptional(word)
    else:
        return word + "d"

def exceptional(word):
    if (word == "write"):
        return "wrote"
    elif (word == "go"):
        return "went"
    elif (word == "put"):
        return "put"
    else:
        return None

print verb_post("play")
print verb_post("like")
print verb_post("try")
print verb_post("picnic")
print verb_post("write")
print verb_post("go")
print verb_post("put")