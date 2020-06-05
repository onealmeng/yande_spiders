import pyperclip
tag = "natori youkai"
tag = tag.strip()
tags = tag.replace(" ", "_")
print(tags)
pyperclip.copy(tags)
