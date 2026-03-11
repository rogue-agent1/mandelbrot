#!/usr/bin/env python3
"""Mandelbrot set renderer (ASCII)."""
import sys
w=int(sys.argv[1]) if len(sys.argv)>1 else 80
h=int(sys.argv[2]) if len(sys.argv)>2 else 40
max_iter=int(sys.argv[3]) if len(sys.argv)>3 else 50
chars=' .,-:;=!*#$@'
for r in range(h):
    row=''
    for c in range(w):
        x0=3.5*c/w-2.5; y0=2.0*r/h-1.0
        x=y=0; i=0
        while x*x+y*y<=4 and i<max_iter:
            x,y=x*x-y*y+x0,2*x*y+y0; i+=1
        row+=chars[i%len(chars)] if i<max_iter else ' '
    print(row)
