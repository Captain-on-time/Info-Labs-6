file_1 = open("text1.txt", "r")
s = file_1.read()
file_1.close()
words = s.split(" ")

Dict = []
for w in words:
    Dict.append((w, words.count(w)))

textDict = dict(Dict)
file_2 = open("textDict.txt", "w")
file_2.write(str(textDict))
file_2.close() 