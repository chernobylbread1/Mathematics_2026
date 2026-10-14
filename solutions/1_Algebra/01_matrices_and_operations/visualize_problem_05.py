#!/usr/bin/env python3
"""
visualize_problem_05.py

Generate a 2D plot visualizing Exercise 5 from the markdown solution:
- columns c1 and c2
- scaled columns 4c1 and 2c2
- resulting vector Ax = 4*c1 + 2*c2

The script saves the plot as `problem_05_plot.png` in the same directory as the script.

Run:
    python3 visualize_problem_05.py

Requires: matplotlib, numpy
Install: pip install matplotlib numpy
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def plot_vectors():
    # original column vectors
    c1 = np.array([2, 1])
    c2 = np.array([-1, 3])

    # scaled columns
    v1 = 4 * c1  # 4c1 = (8,4)
    v2 = 2 * c2  # 2c2 = (-2,6)

    # resulting vector
    Ax = v1 + v2  # (6,10)

    # setup plot
    fig, ax = plt.subplots(figsize=(6, 6))

    # draw arrows from origin
    ax.quiver(0, 0, c1[0], c1[1], angles='xy', scale_units='xy', scale=1, color='tab:blue', label='c1 = (2,1)')
    ax.quiver(0, 0, c2[0], c2[1], angles='xy', scale_units='xy', scale=1, color='tab:orange', label='c2 = (-1,3)')
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='tab:green', label='4c1 = (8,4)')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='tab:red', label='2c2 = (-2,6)')
    ax.quiver(0, 0, Ax[0], Ax[1], angles='xy', scale_units='xy', scale=1, color='tab:purple', label='Ax = (6,10)', linewidth=2)

    # annotate vector tips
    vectors = [(c1, 'c1'), (c2, 'c2'), (v1, '4c1'), (v2, '2c2'), (Ax, 'Ax')]
    for vec, name in vectors:
        ax.text(vec[0] + 0.15, vec[1] + 0.15, f"{name} {tuple(vec)}", fontsize=9)

    # set axis limits with margin
    xs = [0, c1[0], c2[0], v1[0], v2[0], Ax[0]]
    ys = [0, c1[1], c2[1], v1[1], v2[1], Ax[1]]
    xmin, xmax = min(xs) - 1, max(xs) + 1
    ymin, ymax = min(ys) - 1, max(ys) + 1
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.set_aspect('equal', 'box')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Exercise 5: columns, scaled columns, and Ax')
    ax.legend(loc='upper left')

    # save to same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, 'problem_05_plot.png')
    plt.savefig(out_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved plot to {out_path}')


if __name__ == '__main__':
    plot_vectors()
