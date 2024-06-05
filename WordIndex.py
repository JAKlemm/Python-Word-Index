f = open("Kennedy", "r")

wordIndex = {}
lineNumber = 0

for line in f:
    lineNumber = lineNumber + 1
    words = line.split()

    for index in range(0, len(words)):
        if words[index] in wordIndex:
            if lineNumber not in wordIndex[words[index]]:
                wordIndex[words[index]].append(lineNumber)
        else:
            wordIndex[words[index]] = [lineNumber]
f.close()

output = open('index.txt', 'w+')

for key in sorted(wordIndex.keys()):
    output.write("%s:" % (key))
    for value in wordIndex[key]:
        output.write(" %d" % (value))
    output.write("\n")

output.close()