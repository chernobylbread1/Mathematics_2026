#!/usr/bin/env python3
"""
visualize_problem_14.py

Generate a 2D geometric visualization of the composition of rotation matrices in Exercise 14:
- Initial vector: v = [1, 0]
- First rotation: alpha = 30 deg -> R(alpha) v = [cos(30 deg), sin(30 deg)]
- Second rotation: beta = 45 deg -> R(beta) R(alpha) v = R(alpha + beta) v = [cos(75 deg), sin(75 deg)]

Includes curved arcs showing angles alpha and beta, unit circle guide, grid, and legend.
Saves the plot as ex14_rotations.png and automatically inserts the markdown image link into problem_14_solution.md.
"""

import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def plot_rotations():
    # Angles in degrees and radians
    alpha_deg = 30.0
    beta_deg = 45.0
    total_deg = alpha_deg + beta_deg  # 75 deg

    alpha_rad = np.deg2rad(alpha_deg)
    beta_rad = np.deg2rad(beta_deg)
    total_rad = np.deg2rad(total_deg)

    # Initial vector and rotated vectors
    v = np.array([1.0, 0.0])
    v_alpha = np.array([np.cos(alpha_rad), np.sin(alpha_rad)])
    v_total = np.array([np.cos(total_rad), np.sin(total_rad)])

    fig, ax = plt.subplots(figsize=(8, 7.5))

    # Reference axes through origin
    ax.axhline(0, color='black', linewidth=1.0, linestyle='-', zorder=1)
    ax.axvline(0, color='black', linewidth=1.0, linestyle='-', zorder=1)

    # Unit circle arc (first quadrant guide) showing length preservation
    theta = np.linspace(0, np.pi / 2, 100)
    ax.plot(np.cos(theta), np.sin(theta), color='gray', linestyle=':', linewidth=1.2,
            alpha=0.6, label='Unit circle', zorder=2)

    # Curved arcs for angles
    # Arc for alpha (from 0 to 30 deg)
    arc_alpha_radius = 0.42
    arc_alpha = Arc((0, 0), 2 * arc_alpha_radius, 2 * arc_alpha_radius,
                    angle=0, theta1=0, theta2=alpha_deg,
                    color='tab:orange', linewidth=2.0, linestyle='-', zorder=3)
    ax.add_patch(arc_alpha)

    # Arc for beta (from 30 to 75 deg)
    arc_beta_radius = 0.62
    arc_beta = Arc((0, 0), 2 * arc_beta_radius, 2 * arc_beta_radius,
                   angle=0, theta1=alpha_deg, theta2=total_deg,
                   color='tab:purple', linewidth=2.0, linestyle='-', zorder=3)
    ax.add_patch(arc_beta)

    # Angle label text
    # Alpha label at mid-angle (15 deg)
    mid_alpha = np.deg2rad(alpha_deg / 2)
    label_alpha_r = arc_alpha_radius + 0.12
    ax.text(label_alpha_r * np.cos(mid_alpha), label_alpha_r * np.sin(mid_alpha),
            r'$\alpha = 30^\circ$', color='tab:orange', fontsize=11, fontweight='bold',
            ha='left', va='center', zorder=6)

    # Beta label at mid-angle ((30 + 75) / 2 = 52.5 deg)
    mid_beta = np.deg2rad((alpha_deg + total_deg) / 2)
    label_beta_r = arc_beta_radius + 0.12
    ax.text(label_beta_r * np.cos(mid_beta), label_beta_r * np.sin(mid_beta),
            r'$\beta = 45^\circ$', color='tab:purple', fontsize=11, fontweight='bold',
            ha='left', va='center', zorder=6)

    # Vectors as arrows starting from the origin (0, 0)
    q_v = ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
                    color='tab:blue', label=r'$v = [1, 0]$ (Initial)', width=0.009, zorder=4)
    q_v_alpha = ax.quiver(0, 0, v_alpha[0], v_alpha[1], angles='xy', scale_units='xy', scale=1,
                          color='tab:orange', label=r'$R(\alpha)v$ ($\alpha = 30^\circ$)', width=0.009, zorder=4)
    q_v_total = ax.quiver(0, 0, v_total[0], v_total[1], angles='xy', scale_units='xy', scale=1,
                          color='tab:purple', label=r'$R(\beta)R(\alpha)v = R(\alpha+\beta)v$ ($75^\circ$)',
                          width=0.009, zorder=5)

    # Tip labels
    ax.text(v[0] + 0.05, v[1] + 0.05, r'$v\,(1, 0)$', fontsize=10.5,
            ha='left', va='bottom', zorder=6)
    ax.text(v_alpha[0] + 0.05, v_alpha[1] + 0.05, r'$R(\alpha)v$', fontsize=10.5,
            ha='left', va='bottom', zorder=6)
    ax.text(v_total[0] - 0.05, v_total[1] + 0.05, r'$R(\alpha+\beta)v$', fontsize=10.5,
            ha='right', va='bottom', zorder=6)

    # Settings
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlim(-0.25, 1.25)
    ax.set_ylim(-0.25, 1.25)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title(r'Exercise 14: Composition of Rotations $R(\alpha)R(\beta) = R(\alpha+\beta)$', fontsize=12, pad=12)
    ax.legend(loc='lower left', framealpha=0.95, fontsize=10)

    # Save plot in script directory and current working directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_script_path = os.path.join(script_dir, 'ex14_rotations.png')
    plt.savefig(out_script_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f'Saved plot to {out_script_path}')

    cwd_path = os.path.join(os.getcwd(), 'ex14_rotations.png')
    if os.path.abspath(cwd_path) != os.path.abspath(out_script_path):
        shutil.copy2(out_script_path, cwd_path)
        print(f'Also copied plot to {cwd_path}')


def insert_markdown_image_link():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(script_dir, 'problem_14_solution.md')
    img_tag = '![Rotations Plot](ex14_rotations.png)'

    if not os.path.exists(md_path):
        print(f'Markdown file not found: {md_path}')
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if img_tag in content:
        print(f'Image link already present in {md_path}')
        return

    # Insert into the solution section of Exercise 14, right after Step 4 (before "---" preceding "### Final Answer")
    target_anchor = '---'
    solution_marker = '### Solution'

    if solution_marker in content and target_anchor in content:
        parts = content.split('---')
        new_parts = []
        inserted = False
        for part in parts:
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

    # Fallback
    with open(md_path, 'a', encoding='utf-8') as f:
        f.write(f'\n\n{img_tag}\n')
    print(f'Appended image link to {md_path}')


if __name__ == '__main__':
    plot_rotations()
    insert_markdown_image_link()

