"""
Generating HTML codes for ASCII table

2021.10.09
"""
import sys
sys.stdout = open("sample.html", "wt")

for row in range(32):
    print('							<tr class="row100">')
    for col in range(4):
        print(f'								<td class="column100 column{col*4+2}" data-column="column{col*4+2}">{row+32*col}</td>')
        print(f'								<td class="column100 column{col*4+3}" data-column="column{col*4+3}">0x{format(row+32*col, "X").zfill(2)}</td>')
        print(f'								<td class="column100 column{col*4+4}" data-column="column{col*4+4}">{chr(row+32*col)}</td>')
        if col < 3:
            print(f'								<td class="column100 column{col*4+5}" data-column="column{col*4+5}"></td>')
    print('							</tr>')

