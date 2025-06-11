import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle

def draw_block(ax, x, y, width, height, color, text):
    """Draws a rectangular block with text."""
    rect = Rectangle((x, y), width, height, color=color, ec="black")
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=10)

def draw_arrow(ax, x_start, y_start, x_end, y_end):
    """Draws an arrow between two points."""
    ax.arrow(x_start, y_start, x_end - x_start, y_end - y_start,
             length_includes_head=True, head_width=0.2, head_length=0.3,
             fc="black", ec="black")

def draw_image():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")  # Turn off axes

    # Draw AXI Masters
    draw_block(ax, 1.5, 5.2, 1.5, 0.6, "orange", "AXI Master 1")
    draw_block(ax, 4.0, 5.2, 1.5, 0.6, "orange", "AXI Master 2")
    draw_block(ax, 6.5, 5.2, 1.5, 0.6, "orange", "AXI Master N")

    # Draw AXI Monitors (above Interconnect)
    draw_block(ax, 1.5, 4.4, 1.5, 0.6, "skyblue", "AXI Monitor 1")
    draw_block(ax, 4.0, 4.4, 1.5, 0.6, "skyblue", "AXI Monitor 2")
    draw_block(ax, 6.5, 4.4, 1.5, 0.6, "skyblue", "AXI Monitor N")

    # Draw Interconnect
    draw_block(ax, 2.25, 3.3, 4.5, 0.8, "mediumpurple", "Interconnect")

    # Draw AXI Slaves (below Interconnect)
    draw_block(ax, 1.5, 2.2, 1.5, 0.6, "yellowgreen", "AXI Slave1")
    draw_block(ax, 4.0, 2.2, 1.5, 0.6,"yellowgreen","AXI Slave2")
