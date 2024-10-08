#!/usr/bin/python
import PyPDF2
import os
import sys

from rich.console import Console
from rich.theme import Theme

# add style
custom_theme = Theme({
    "good" : "bold gold3",
    "bad": "bold red",
    "title": "bold green",
    "black": "black",
    "highlight": "bold blue"
})
console = Console(theme=custom_theme)

n = len(sys.argv)
sumDir = [-1] * n
directory = [-1] * n

for i in range(1, n):
    print()
    console.print(f"Path number {i}: [good]{sys.argv[i]}[/good]", style="title")
    sum_pages = 0
    directory[i] = sys.argv[i]

    if os.path.exists(directory[i]):
        for filename in os.listdir(directory[i]):
            f = os.path.join(directory[i], filename)
            if f.endswith('.pdf'):
                file = open(f, 'rb')
                readpdf = PyPDF2.PdfReader(file)
                try:
                    sum_pages += len(readpdf.pages)
                except PyPDF2.errors.FileNotDecryptedError:
                    console.print("[black]File:[/black]", f.replace(directory[i] + "\\", ""), "is encrypted; ignored.", style="bad")
                    continue
                console.print(f"[black]File:[/black] [good]{f.replace(directory[i] + '\\', '')}[/good] Num pages: {len(readpdf.pages)}", style="title")
    else:
        console.print(f"Argument number {i} not found", style="bad")

    console.print(f"Total number of pages: {sum_pages}", style="highlight")