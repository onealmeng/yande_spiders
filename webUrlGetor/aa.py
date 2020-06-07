import pyperclip
tag = "renka (cloudsaikou)"
tag = tag.strip()
tags = tag.replace(" ", "_")
print(tags)
pyperclip.copy(tags)
