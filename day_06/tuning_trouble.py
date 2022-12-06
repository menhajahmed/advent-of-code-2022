#!/usr/bin/env python3

with open("input.txt", encoding="utf-8") as input:
    marker = []
    char = input.read(1)
    while len(marker) < 14:
        try:
            marker = marker[marker.index(char) + 1:]
        except ValueError:
            pass
        marker.append(char)
        char = input.read(1)
    print(input.tell() - 1)
