fileName = ""
fileObj = open(fileName, "r")
words = fileObj.read().splitlines()
outputs = []
for word in words:
    parts = word.split(".")
    output = parts[1].replace("And since", "")
    outputs.append(output)
fileObj.close()

newFileName = ""
with open(newFileName, 'w') as f:
    for item in outputs:
        f.write("%s\n" % item)
