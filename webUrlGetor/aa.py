import pyperclip
tag = "mashiro (rikuya)"
tag = tag.strip()
tags = tag.replace(" ", "_")
print(tags)
pyperclip.copy(tags)
