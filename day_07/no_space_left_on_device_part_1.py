#!/usr/bin/env python3

from collections import defaultdict

class Directory:

    def __init__(self, parent_dir):
        self.parent_dir = parent_dir
        self.subdirs = defaultdict(lambda: Directory(self))
        self.files = {}
        self.size = None

    def mkdir(self, dirname):
        return self.parent_dir if dirname == ".." else self.subdirs[dirname]

    def touch(self, filename, size):
        self.files[filename] = size

    def get_size(self):
        if self.size is None:
            self.size = sum(map(Directory.get_size, self.subdirs.values())) + sum(self.files.values())
        return self.size

    def get_small_subdirs(self):
        return (subdir for subdir in subdirs if subdir.get_size() <= 100000)

with open("input.txt", encoding="utf-8") as input:
    root_dir = Directory(None)
    current_dir = root_dir
    line = input.readline()
    while line:
        command = line[1:].split()
        line = input.readline()
        match command[0]:
            case "cd":
                current_dir = root_dir if command[1] == "/" else current_dir.mkdir(command[1])
            case "ls":
                while line and not line.startswith("$"):
                    listing = line.split()
                    if listing[0] == "dir":
                        current_dir.mkdir(listing[1])
                    else:
                        current_dir.touch(listing[1], int(listing[0]))
                    line = input.readline()
            case _:
                raise ValueError("Unknown command: " + command[0])

    total_size = 0
    dirs = [root_dir]
    while dirs:
        current_dir = dirs.pop()
        if current_dir.get_size() <= 100000:
            total_size += current_dir.get_size()
        dirs.extend(current_dir.subdirs.values())
    print(total_size)
