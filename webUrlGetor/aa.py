import pyperclip
tag = "ogami ren"
tag = tag.strip()
tags = tag.replace(" ", "_")
print(tags)
pyperclip.copy(tags)
