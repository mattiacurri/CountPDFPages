#!/usr/bin/python
import pypdf
import os
import sys

from rich.console import Console
from rich.theme import Theme

from tabulate import tabulate

# add style
custom_theme = Theme({
    "good" : "bold gold3",
    "bad": "bold red",
    "title": "bold green",
    "black": "black",
    "highlight": "bold blue",
})
console = Console(theme=custom_theme)

n = len(sys.argv)
sumDir = [0] * n
directory = [0] * n

for i in range(1, n):
    print()
    console.print(f"Path number {i}: [good]{sys.argv[i]}[/good]", style="title")
    directory[i] = sys.argv[i]
    table_data = []

    if os.path.exists(directory[i]):
        sum_pages = 0
        for filename in os.listdir(directory[i]):
            f = os.path.join(directory[i], filename)
            if f.endswith('.pdf'):
                file = open(f, 'rb')
                readpdf = pypdf.PdfReader(file)
                try:
                    num_pages = len(readpdf.pages)  # Calculate num_pages once
                    sum_pages += num_pages
                    table_data.append([f.replace(directory[i] + "\\", ""), num_pages])
                except pypdf.errors.FileNotDecryptedError:
                    table_data.append([f.replace(directory[i] + "\\", ""), "Encrypted; ignored"])
                    continue
    else:
        console.print(f"Argument number {i} not found", style="bad")
        continue
    table_data.append(["\033[1mTotal pages:\033[0m", sum_pages])
    trimmed_table_data = [[os.path.basename(row[0]), row[1]] for row in table_data]
    print(tabulate(trimmed_table_data, headers=["\033[1mFile\033[0m", "\033[1mNum pages\033[0m"], tablefmt="fancy_grid"))