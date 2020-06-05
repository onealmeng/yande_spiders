import pyperclip
tag = "miyo (user zdsp7735)"
tag = tag.strip()
tags = tag.replace(" ", "_")
print(tags)
pyperclip.copy(tags)
