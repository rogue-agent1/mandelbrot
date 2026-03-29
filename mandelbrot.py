#!/usr/bin/env python3
"""mandelbrot - Mandelbrot set ASCII renderer."""
import sys, argparse, json

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2: return i
    return max_iter

def render(xmin, xmax, ymin, ymax, width, height, max_iter):
    chars = " .,-~:;=!*#$@"
    lines = []
    for row in range(height):
        y = ymin + (ymax - ymin) * row / height
        line = ""
        for col in range(width):
            x = xmin + (xmax - xmin) * col / width
            n = mandelbrot(complex(x, y), max_iter)
            line += chars[n % len(chars)] if n < max_iter else " "
        lines.append(line)
    return "
".join(lines)

def main():
    p = argparse.ArgumentParser(description="Mandelbrot renderer")
    p.add_argument("--width", type=int, default=80)
    p.add_argument("--height", type=int, default=30)
    p.add_argument("--max-iter", type=int, default=50)
    p.add_argument("--xmin", type=float, default=-2.5)
    p.add_argument("--xmax", type=float, default=1.0)
    p.add_argument("--ymin", type=float, default=-1.0)
    p.add_argument("--ymax", type=float, default=1.0)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if args.json:
        data = []
        for row in range(args.height):
            y = args.ymin + (args.ymax-args.ymin)*row/args.height
            r = []
            for col in range(args.width):
                x = args.xmin + (args.xmax-args.xmin)*col/args.width
                r.append(mandelbrot(complex(x,y), args.max_iter))
            data.append(r)
        print(json.dumps({"width": args.width, "height": args.height, "max_iter": args.max_iter, "data": data}))
    else:
        print(render(args.xmin, args.xmax, args.ymin, args.ymax, args.width, args.height, args.max_iter))

if __name__ == "__main__": main()
