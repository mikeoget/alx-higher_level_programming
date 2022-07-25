
#!/usr/bin/python3
"""
a reading function
"""


def read_file(filename=""):
    """reads files"""
    with open(filename, mode="r", encoding="utf-8") as mefile:
        print(mefile.read(), end="")
