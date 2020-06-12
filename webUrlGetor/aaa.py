# -*- coding: utf-8 -*-
import pyperclip


def tag_editor(tag):
    tag = tag.strip()
    tags = tag.replace(" ", "_")
    pyperclip.copy(tags)


if __name__ == '__main__':
    tag = "kaede (003591163)"
    tag_editor(tag)
