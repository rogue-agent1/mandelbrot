#!/usr/bin/env python3
"""Mandelbrot Set - Render the fractal in ASCII with zoom support."""
import sys

def mandelbrot(c, max_iter=100):
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2: return i
    return max_iter

def render(x_min=-2.5, x_max=1.0, y_min=-1.25, y_max=1.25, width=80, height=30, max_iter=100):
    chars = " .`-~:;=!*#$@"
    lines = []
    for row in range(height):
        y = y_min + (y_max - y_min) * row / height
        line = ""
        for col in range(width):
            x = x_min + (x_max - x_min) * col / width
            n = mandelbrot(complex(x, y), max_iter)
            if n == max_iter: line += " "
            else: line += chars[n % len(chars)]
        lines.append(line)
    return "\n".join(lines)

def main():
    presets = {
        "full": (-2.5, 1.0, -1.25, 1.25),
        "seahorse": (-0.75, -0.73, 0.1, 0.12),
        "spiral": (-0.77, -0.74, 0.08, 0.11),
        "mini": (-0.17, -0.13, 1.02, 1.06),
    }
    name = sys.argv[1] if len(sys.argv) > 1 else "full"
    coords = presets.get(name, presets["full"])
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    print(f"=== Mandelbrot Set ({name}) ===\n")
    print(render(*coords, width=70, height=25, max_iter=iters))

if __name__ == "__main__":
    main()
