import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def show_graph(subjects, marks):
    # Create bigger figure for spacing
    plt.figure(figsize=(11,6))

    # Assigning colors based on performance
    bar_colors = []
    for mark in marks:
        if mark <= 40:
            bar_colors.append('#ff4d4d')   # red
        elif mark <= 60:
            bar_colors.append('#ffa500')   # orange
        elif mark <= 80:
            bar_colors.append('#3399ff')   # blue
        else:
            bar_colors.append('#33cc33')   # green

    # Plotting bar
    bars = plt.bar(subjects, marks, color=bar_colors, edgecolor='black', width=0.55)

    # Add value labels on top of bars 
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/4,
            height + 1.5,
            f"{height}",
            ha='center',
            fontsize=10,
            fontweight='bold'
        )

    # Labels and title
    plt.xlabel("SUBJECTS", fontsize=12, fontweight = 'bold' , font = 'Times New Roman')
    plt.ylabel("MARKS", fontsize=12, fontweight = 'bold' , font = 'Times New Roman')
    plt.title("STUDENT PERFORMANCE ANALYSIS", fontsize=14, fontweight = 'bold' , font = 'Times New Roman')

    # x-axis label 
    plt.xticks(fontsize=10)

    # Legend
    legend_boxes = [
        mpatches.Patch(color='#ff4d4d', label='Weak (<40)'),
        mpatches.Patch(color='#ffa500', label='Average (40–59)'),
        mpatches.Patch(color='#3399ff', label='Good (60–79)'),
        mpatches.Patch(color='#33cc33', label='Strong (80–100)')
    ]
    plt.legend(handles=legend_boxes)

    # y-axis 
    plt.ylim(0, 100)   # assuming marks are out of 100
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Adjust layout
    plt.tight_layout()

    # Show graph
    plt.show()