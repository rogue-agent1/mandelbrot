#!/usr/bin/env python3
"""Mandelbrot set ASCII/Unicode renderer."""
import sys

CHARS = ' .:-=+*#%@'
BLOCKS = ' ░▒▓█'

def mandelbrot(width=80, height=40, max_iter=100, xmin=-2.5, xmax=1.0, ymin=-1.25, ymax=1.25, style='block'):
    palette = BLOCKS if style == 'block' else CHARS
    for row in range(height):
        line = ''
        for col in range(width):
            x0 = xmin + (xmax - xmin) * col / width
            y0 = ymin + (ymax - ymin) * row / height
            x, y, i = 0.0, 0.0, 0
            while x*x + y*y <= 4 and i < max_iter:
                x, y = x*x - y*y + x0, 2*x*y + y0
                i += 1
            line += palette[min(i * len(palette) // (max_iter + 1), len(palette) - 1)]
        print(line)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('-W', '--width', type=int, default=80)
    p.add_argument('-H', '--height', type=int, default=40)
    p.add_argument('-i', '--iterations', type=int, default=100)
    p.add_argument('--zoom', type=float, default=1.0)
    p.add_argument('--cx', type=float, default=-0.75)
    p.add_argument('--cy', type=float, default=0.0)
    p.add_argument('--style', choices=['block','ascii'], default='block')
    args = p.parse_args()
    r = 1.75 / args.zoom
    mandelbrot(args.width, args.height, args.iterations,
               args.cx-r*1.5, args.cx+r*0.5, args.cy-r, args.cy+r, args.style)
