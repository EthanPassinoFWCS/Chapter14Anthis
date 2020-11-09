import os
for filename in os.listdir("/Users/pass512cs15/PycharmProjects/Chapter14Anthis"):
    if "TIY1" in filename:
        with open(filename) as f2:
            content = f2.readlines()
        with open(f"TIY8{filename[4:]}", "w+") as f:
            print(f"Created {f.name} in encoding type {f.encoding}.")
            f.writelines(content)
