#!/usr/bin/env python3
"""
visualize_problem_09.py

Generate a 2D geometric visualization of the matrix transformations in Exercise 9:
- Original vector: x = [1, 2]
- Nonuniform scaling: S = [[2, 0], [0, 1]] -> Sx = [2, 2]
- 90 deg counterclockwise rotation: R = [[0, -1], [1, 0]] -> Rx = [-2, 1]
- Composition Path 1 (Scale then Rotate): RSx = [-2, 2]
- Composition Path 2 (Rotate then Scale): SRx = [-4, 1]

Saves the plot as ex9_transformations.png and automatically inserts the markdown
image link ![Transformations Plot](ex9_transformations.png) into problem_09_solution.md.
"""

import os
import shutil
import numpy as np
import matplotlib.pyplot as plt


def plot_transformations():
    # Matrices
    S = np.array([[2, 0], [0, 1]])
    R = np.array([[0, -1], [1, 0]])

    # Vectors
    x = np.array([1, 2])
    Sx = S @ x       # [2, 2]
    RSx = R @ Sx     # [-2, 2]
    Rx = R @ x       # [-2, 1]
    SRx = S @ Rx     # [-4, 1]

    fig, ax = plt.subplots(figsize=(9, 6.5))

    # Reference coordinate axes
    ax.axhline(0, color='black', linewidth=1.0, linestyle='-', zorder=1)
    ax.axvline(0, color='black', linewidth=1.0, linestyle='-', zorder=1)

    # Transition helper lines showing the two paths
    # Path 1: x -> Sx (horizontal stretch by factor of 2)
    ax.annotate('', xy=(Sx[0], Sx[1]), xytext=(x[0], x[1]),
                arrowprops=dict(arrowstyle='->', color='tab:cyan', lw=1.5, ls=':'), zorder=2)
    # Path 1: Sx -> RSx (90 deg counterclockwise rotation arc)
    ax.annotate('', xy=(RSx[0], RSx[1]), xytext=(Sx[0], Sx[1]),
                arrowprops=dict(arrowstyle='->', color='tab:purple', lw=1.5, ls=':',
                                connectionstyle='arc3,rad=0.25'), zorder=2)

    # Path 2: x -> Rx (90 deg counterclockwise rotation arc)
    ax.annotate('', xy=(Rx[0], Rx[1]), xytext=(x[0], x[1]),
                arrowprops=dict(arrowstyle='->', color='tab:orange', lw=1.5, ls='--',
                                connectionstyle='arc3,rad=-0.2'), zorder=2)
    # Path 2: Rx -> SRx (horizontal stretch by factor of 2)
    ax.annotate('', xy=(SRx[0], SRx[1]), xytext=(Rx[0], Rx[1]),
                arrowprops=dict(arrowstyle='->', color='tab:red', lw=1.5, ls='--'), zorder=2)

    # Vectors as arrows starting from the origin (0, 0)
    q_x = ax.quiver(0, 0, x[0], x[1], angles='xy', scale_units='xy', scale=1,
                    color='tab:blue', label=r'$x = (1, 2)$ [Original]', width=0.009, zorder=4)
    q_Sx = ax.quiver(0, 0, Sx[0], Sx[1], angles='xy', scale_units='xy', scale=1,
                     color='tab:cyan', label=r'$Sx = (2, 2)$ [Scaled]', width=0.008, zorder=4)
    q_RSx = ax.quiver(0, 0, RSx[0], RSx[1], angles='xy', scale_units='xy', scale=1,
                      color='tab:purple', label=r'$RSx = (-2, 2)$ [Scale $\to$ Rotate]', width=0.008, zorder=5)
    q_Rx = ax.quiver(0, 0, Rx[0], Rx[1], angles='xy', scale_units='xy', scale=1,
                     color='tab:orange', label=r'$Rx = (-2, 1)$ [Rotated]', width=0.008, zorder=4)
    q_SRx = ax.quiver(0, 0, SRx[0], SRx[1], angles='xy', scale_units='xy', scale=1,
                      color='tab:red', label=r'$SRx = (-4, 1)$ [Rotate $\to$ Scale]', width=0.008, zorder=5)

    # Tip labels carefully offset to avoid any collisions
    ax.text(x[0] + 0.15, x[1] + 0.12, r'$x\,(1, 2)$', fontsize=10.5, ha='left', va='bottom', zorder=6)
    ax.text(Sx[0] + 0.15, Sx[1] + 0.12, r'$Sx\,(2, 2)$', fontsize=10.5, ha='left', va='bottom', zorder=6)
    ax.text(RSx[0] - 0.15, RSx[1] + 0.15, r'$RSx\,(-2, 2)$', fontsize=10.5, ha='right', va='bottom', zorder=6)
    ax.text(Rx[0] - 0.15, Rx[1] + 0.18, r'$Rx\,(-2, 1)$', fontsize=10.5, ha='right', va='bottom', zorder=6)
    ax.text(SRx[0] - 0.15, SRx[1] + 0.15, r'$SRx\,(-4, 1)$', fontsize=10.5, ha='right', va='bottom', zorder=6)

    # Plot settings
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlim(-5.2, 3.2)
    ax.set_ylim(-1.0, 3.2)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title(r'Exercise 9: Matrix Transformations $RSx \neq SRx$', fontsize=13, pad=12)

    # Legend placed in lower-left (Quadrant 3 is empty, completely preventing overlaps)
    ax.legend([q_x, q_Sx, q_RSx, q_Rx, q_SRx],
              [r'$x = (1, 2)$ [Original]',
               r'$Sx = (2, 2)$ [Scaled]',
               r'$RSx = (-2, 2)$ [Scale $\to$ Rotate]',
               r'$Rx = (-2, 1)$ [Rotated]',
               r'$SRx = (-4, 1)$ [Rotate $\to$ Scale]'],
              loc='lower left', framealpha=0.95, fontsize=9.5)

    # Save image file in script directory and current working directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_script_path = os.path.join(script_dir, 'ex9_transformations.png')
    plt.savefig(out_script_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved plot to {out_script_path}')

    cwd_path = os.path.join(os.getcwd(), 'ex9_transformations.png')
    if os.path.abspath(cwd_path) != os.path.abspath(out_script_path):
        shutil.copy2(out_script_path, cwd_path)
        print(f'Also copied plot to {cwd_path}')


def insert_markdown_image_link():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(script_dir, 'problem_09_solution.md')
    img_tag = '![Transformations Plot](ex9_transformations.png)'

    if not os.path.exists(md_path):
        print(f'Markdown file not found: {md_path}')
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if img_tag in content:
        print(f'Image link already present in {md_path}')
        return

    # Insert into the solution section of Exercise 9, before "---" preceding "### Final Answer"
    target_anchor = '---'
    solution_marker = '### Solution'

    if solution_marker in content and target_anchor in content:
        parts = content.split('---')
        new_parts = []
        inserted = False
        for i, part in enumerate(parts):
            if '### Final Answer' in part and not inserted:
                prev = new_parts[-1].rstrip()
                new_parts[-1] = f'{prev}\n\n{img_tag}\n\n'
                inserted = True
            new_parts.append(part)

        if inserted:
            new_content = '---'.join(new_parts)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Inserted image link into solution section of {md_path}')
            return

    # Fallback: append before EOF
    with open(md_path, 'a', encoding='utf-8') as f:
        f.write(f'\n\n{img_tag}\n')
    print(f'Appended image link to {md_path}')


if __name__ == '__main__':
    plot_transformations()
    insert_markdown_image_link()
