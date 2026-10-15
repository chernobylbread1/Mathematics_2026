#!/usr/bin/env python3
"""
visualize_problem_05.py

Generate a 2D plot visualizing Exercise 5 from the markdown solution:
- Original column vectors c1 = (2, 1) and c2 = (-1, 3)
- Scaled versions 4c1 = (8, 4) and 2c2 = (-2, 6)
- Resulting vector Ax = 4c1 + 2c2 = (6, 10)

Saves the plot as problem_05_plot.png in the same directory and
automatically appends the markdown image link to problem_05_solution.md if not already present.
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def plot_vectors():
    # Original column vectors
    c1 = np.array([2, 1])
    c2 = np.array([-1, 3])

    # Scaled column vectors
    v1 = 4 * c1  # 4c1 = (8, 4)
    v2 = 2 * c2  # 2c2 = (-2, 6)

    # Resulting vector
    Ax = v1 + v2  # Ax = (6, 10)

    # Setup plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Reference axes at origin
    ax.axhline(0, color='black', linewidth=1.0, linestyle='-', zorder=1)
    ax.axvline(0, color='black', linewidth=1.0, linestyle='-', zorder=1)

    # Parallelogram / addition dashed lines: 4c1 -> Ax and 2c2 -> Ax
    ax.plot([v1[0], Ax[0]], [v1[1], Ax[1]], linestyle='--', color='tab:red', alpha=0.6, linewidth=1.5, zorder=2)
    ax.plot([v2[0], Ax[0]], [v2[1], Ax[1]], linestyle='--', color='tab:green', alpha=0.6, linewidth=1.5, zorder=2)

    # Draw vector arrows starting from the origin (0, 0)
    # Using distinct colors for each vector
    q_c1 = ax.quiver(0, 0, c1[0], c1[1], angles='xy', scale_units='xy', scale=1,
                     color='tab:blue', label=r'$c_1 = (2, 1)$', width=0.009, zorder=4)
    q_c2 = ax.quiver(0, 0, c2[0], c2[1], angles='xy', scale_units='xy', scale=1,
                     color='tab:orange', label=r'$c_2 = (-1, 3)$', width=0.009, zorder=4)
    q_v1 = ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1,
                     color='tab:green', label=r'$4c_1 = (8, 4)$', width=0.007, zorder=3)
    q_v2 = ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1,
                     color='tab:red', label=r'$2c_2 = (-2, 6)$', width=0.007, zorder=3)
    q_Ax = ax.quiver(0, 0, Ax[0], Ax[1], angles='xy', scale_units='xy', scale=1,
                     color='tab:purple', label=r'$Ax = 4c_1 + 2c_2 = (6, 10)$', width=0.008, zorder=5)

    # Annotate vector coordinates clearly
    ax.text(c1[0] + 0.2, c1[1] - 0.35, r'$c_1\ (2, 1)$', fontsize=10, ha='left', va='center', zorder=6)
    ax.text(c2[0] - 0.25, c2[1] + 0.1, r'$c_2\ (-1, 3)$', fontsize=10, ha='right', va='center', zorder=6)
    ax.text(v1[0] + 0.25, v1[1] - 0.2, r'$4c_1\ (8, 4)$', fontsize=10, ha='left', va='center', zorder=6)
    ax.text(v2[0], v2[1] + 0.35, r'$2c_2\ (-2, 6)$', fontsize=10, ha='center', va='bottom', zorder=6)
    ax.text(Ax[0] + 0.2, Ax[1] + 0.25, r'$Ax\ (6, 10)$', fontsize=10, ha='left', va='bottom', zorder=6)

    # Set axis limits with comfortable margins
    ax.set_xlim(-4, 11)
    ax.set_ylim(-1.5, 11.5)

    ax.set_aspect('equal', 'box')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title(r'Exercise 5: Linear Combination of Columns $Ax = 4c_1 + 2c_2$', fontsize=12, pad=12)
    ax.legend([q_c1, q_c2, q_v1, q_v2, q_Ax],
              [r'$c_1 = (2, 1)$', r'$c_2 = (-1, 3)$', r'$4c_1 = (8, 4)$', r'$2c_2 = (-2, 6)$', r'$Ax = (6, 10)$'],
              loc='upper left', framealpha=0.9, fontsize=10)

    # Save PNG in current directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, 'problem_05_plot.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved plot to {out_path}')


def append_markdown_link():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(script_dir, 'problem_05_solution.md')
    img_link = '![Exercise 5 visualization](./problem_05_plot.png)'

    if not os.path.exists(md_path):
        print(f'Markdown file not found at {md_path}')
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'problem_05_plot.png' not in content:
        with open(md_path, 'a', encoding='utf-8') as f:
            if not content.endswith('\n'):
                f.write('\n')
            f.write(f'\n{img_link}\n')
        print(f'Appended image link to {md_path}')
    else:
        print(f'Image link already present in {md_path}')


if __name__ == '__main__':
    plot_vectors()
    append_markdown_link()
