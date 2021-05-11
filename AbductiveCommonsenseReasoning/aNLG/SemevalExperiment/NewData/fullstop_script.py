lines = []
with open("enthymeme_new_data.source", "r") as f:
    for line in f.readlines():
        context = line.split("#")
        if (context[0].strip()[-1] != "."):
            line.replace(context[0].strip()[-1], context[0].strip()[-1] + ".")
        lines.append(line)


print(lines)

with open("enthymeme_new_data_fullstop.source", "w") as f:
    for line in lines:
        f.write(line)