#Count word frequencies in a text file

text = open("words.txt", "r")
d = dict()
for line in text:
    line = line.strip().lower()  
    words = line.split(" ")
    for word in words:
        d[word] = d[word] + 1 if word in d else 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])