# -*- coding: utf-8 -*-
import pyperclip


def tag_editor(tag):
    tag = tag.strip()
    tags = tag.replace(" ", "_")
    pyperclip.copy(tags)


if __name__ == '__main__':
    tag = ""
    tag_editor(tag)
