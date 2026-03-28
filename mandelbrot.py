#!/usr/bin/env python3
"""mandelbrot - ASCII Mandelbrot set renderer."""
import sys
def mandelbrot(width=80,height=24,max_iter=100,xmin=-2.5,xmax=1.0,ymin=-1.0,ymax=1.0):
    chars=" .:-=+*#%@"
    lines=[]
    for row in range(height):
        line=""
        for col in range(width):
            x0=xmin+(xmax-xmin)*col/width;y0=ymin+(ymax-ymin)*row/height
            x=y=0;i=0
            while x*x+y*y<=4 and i<max_iter:x,y=x*x-y*y+x0,2*x*y+y0;i+=1
            line+=chars[min(i*len(chars)//max_iter,len(chars)-1)]
        lines.append(line)
    return lines
if __name__=="__main__":
    w=int(sys.argv[1]) if len(sys.argv)>1 else 80
    h=int(sys.argv[2]) if len(sys.argv)>2 else 30
    for line in mandelbrot(w,h):print(line)
