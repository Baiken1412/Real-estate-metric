"""
Property Investment Data Visualization Module
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from typing import Dict, List
import seaborn as sns

# Configure font display
rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
rcParams['axes.unicode_minus'] = False

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.facecolor'] = 'white'


class PropertyVisualizer:
    """Property Investment Data Visualization Tool"""

    def __init__(self):
        self.metric_names = {
            'population_growth': 'Population Growth',
            'rental_yield': 'Rental Yield',
            'supply_ratio': 'Supply Ratio',
            'vacancy_rate': 'Vacancy Rate',
            'mortgage_stress': 'Mortgage Stress'
        }

        self.colors = {
            'excellent': '#2ecc71',  # Green
            'good': '#3498db',       # Blue
            'medium': '#f39c12',     # Orange
            'poor': '#e74c3c'        # Red
        }

    def plot_radar_chart(self, result: Dict, area_name: str = "Assessment Area", save_path: str = None):
        """
        Plot radar chart

        Args:
            result: Result from calculate_composite_score
            area_name: Area name
            save_path: Save path (optional)
        """
        scores = result['individual_scores']

        # Prepare data
        categories = [self.metric_names[k] for k in scores.keys()]
        values = list(scores.values())

        # Close the radar chart
        values += values[:1]
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]

        # Create figure
        fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection='polar'))

        # Plot radar chart
        ax.plot(angles, values, 'o-', linewidth=2, label=area_name, color='#3498db')
        ax.fill(angles, values, alpha=0.25, color='#3498db')

        # Set ticks and labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=11)
        ax.set_ylim(0, 100)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'], size=9)
        ax.grid(True, linestyle='--', alpha=0.7)

        # Add title and score
        composite_score = result['composite_score']
        grade = result['grade']
        plt.title(f'5-Dimension Property Assessment - {area_name}\nComposite Score: {composite_score:.1f} | Grade: {grade}',
                  size=14, weight='bold', pad=20)

        # Add legend
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"[OK] Radar chart saved to: {save_path}")

        plt.show()

    def plot_bar_chart(self, result: Dict, area_name: str = "Assessment Area", save_path: str = None):
        """
        Plot bar chart

        Args:
            result: Result from calculate_composite_score
            area_name: Area name
            save_path: Save path (optional)
        """
        scores = result['individual_scores']
        weights = result['weights']

        # Prepare data
        categories = [self.metric_names[k] for k in scores.keys()]
        values = list(scores.values())
        weight_values = [weights[k] * 100 for k in scores.keys()]

        # Set colors based on scores
        colors = [self._get_color(v) for v in values]

        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Left plot: Dimension scores
        bars1 = ax1.barh(categories, values, color=colors, alpha=0.8, edgecolor='black')
        ax1.set_xlabel('Score', size=11, weight='bold')
        ax1.set_title(f'Dimension Scores - {area_name}', size=13, weight='bold')
        ax1.set_xlim(0, 100)
        ax1.grid(axis='x', alpha=0.3)

        # Display values on bars
        for i, (bar, value) in enumerate(zip(bars1, values)):
            ax1.text(value + 2, i, f'{value:.1f}', va='center', size=10, weight='bold')

        # Right plot: Weight distribution
        colors_weight = ['#95a5a6'] * len(weight_values)
        bars2 = ax2.barh(categories, weight_values, color=colors_weight, alpha=0.8, edgecolor='black')
        ax2.set_xlabel('Weight (%)', size=11, weight='bold')
        ax2.set_title('Weight Distribution', size=13, weight='bold')
        ax2.set_xlim(0, 30)
        ax2.grid(axis='x', alpha=0.3)

        # Display weights on bars
        for i, (bar, value) in enumerate(zip(bars2, weight_values)):
            ax2.text(value + 0.5, i, f'{value:.1f}%', va='center', size=10, weight='bold')

        # Add overall score
        composite_score = result['composite_score']
        grade = result['grade']
        fig.suptitle(f'Composite Score: {composite_score:.1f} / 100  |  Grade: {grade}',
                     size=15, weight='bold', y=0.98)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"[OK] Bar chart saved to: {save_path}")

        plt.show()

    def plot_comparison(self, comparison_df: pd.DataFrame, save_path: str = None):
        """
        Plot multi-area comparison

        Args:
            comparison_df: DataFrame from compare_areas
            save_path: Save path (optional)
        """
        # Create figure
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))

        # Top plot: Composite score comparison
        areas = comparison_df['Area'].values
        composite_scores = comparison_df['Composite Score'].values
        colors = [self._get_color(score) for score in composite_scores]

        bars = axes[0].barh(areas, composite_scores, color=colors, alpha=0.8, edgecolor='black')
        axes[0].set_xlabel('Composite Score', size=12, weight='bold')
        axes[0].set_title('Area Composite Score Comparison', size=14, weight='bold')
        axes[0].set_xlim(0, 100)
        axes[0].grid(axis='x', alpha=0.3)

        # Display values and grades
        for i, (bar, score, grade) in enumerate(zip(bars, composite_scores, comparison_df['Grade'])):
            axes[0].text(score + 2, i, f'{score:.1f} ({grade})',
                        va='center', size=10, weight='bold')

        # Bottom plot: Dimension heatmap
        metric_columns = ['Population Growth', 'Rental Yield', 'Supply Ratio', 'Vacancy Rate', 'Mortgage Stress']
        heatmap_data = comparison_df[metric_columns].values

        im = axes[1].imshow(heatmap_data, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)
        axes[1].set_xticks(np.arange(len(metric_columns)))
        axes[1].set_yticks(np.arange(len(areas)))
        axes[1].set_xticklabels(metric_columns, size=11)
        axes[1].set_yticklabels(areas, size=10)
        axes[1].set_title('Dimension Score Heatmap', size=14, weight='bold', pad=15)

        # Add value annotations
        for i in range(len(areas)):
            for j in range(len(metric_columns)):
                text = axes[1].text(j, i, f'{heatmap_data[i, j]:.0f}',
                                   ha="center", va="center", color="black", size=9, weight='bold')

        # Add colorbar
        cbar = plt.colorbar(im, ax=axes[1], orientation='horizontal', pad=0.1, shrink=0.8)
        cbar.set_label('Score', size=11, weight='bold')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"[OK] Comparison chart saved to: {save_path}")

        plt.show()

    def plot_composite_dashboard(self, result: Dict, area_name: str = "Assessment Area", save_path: str = None):
        """
        Plot composite dashboard (multiple visualizations)

        Args:
            result: Result from calculate_composite_score
            area_name: Area name
            save_path: Save path (optional)
        """
        scores = result['individual_scores']
        weights = result['weights']
        composite_score = result['composite_score']
        grade = result['grade']

        # Create 2x2 subplots
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

        # 1. Radar chart
        ax1 = fig.add_subplot(gs[0, 0], projection='polar')
        categories = [self.metric_names[k] for k in scores.keys()]
        values = list(scores.values())
        values += values[:1]
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]

        ax1.plot(angles, values, 'o-', linewidth=2.5, color='#3498db')
        ax1.fill(angles, values, alpha=0.25, color='#3498db')
        ax1.set_xticks(angles[:-1])
        ax1.set_xticklabels(categories, size=10)
        ax1.set_ylim(0, 100)
        ax1.set_yticks([20, 40, 60, 80, 100])
        ax1.set_title('5-Dimension Radar Chart', size=12, weight='bold', pad=20)
        ax1.grid(True, linestyle='--', alpha=0.7)

        # 2. Dimension score bar chart
        ax2 = fig.add_subplot(gs[0, 1])
        categories_short = [self.metric_names[k] for k in scores.keys()]
        values_bar = list(scores.values())
        colors_bar = [self._get_color(v) for v in values_bar]

        bars = ax2.barh(categories_short, values_bar, color=colors_bar, alpha=0.8, edgecolor='black')
        ax2.set_xlabel('Score', size=11, weight='bold')
        ax2.set_title('Dimension Scores', size=12, weight='bold')
        ax2.set_xlim(0, 100)
        ax2.grid(axis='x', alpha=0.3)

        for i, (bar, value) in enumerate(zip(bars, values_bar)):
            ax2.text(value + 2, i, f'{value:.1f}', va='center', size=9, weight='bold')

        # 3. Composite score gauge
        ax3 = fig.add_subplot(gs[1, 0])
        self._draw_gauge(ax3, composite_score)
        ax3.set_title('Composite Score', size=12, weight='bold')

        # 4. Contribution analysis (weighted scores)
        ax4 = fig.add_subplot(gs[1, 1])
        weighted_scores = [scores[k] * weights[k] for k in scores.keys()]
        categories_contrib = [self.metric_names[k] for k in scores.keys()]

        wedges, texts, autotexts = ax4.pie(weighted_scores, labels=categories_contrib,
                                            autopct='%1.1f%%', startangle=90,
                                            colors=plt.cm.Set3(range(len(weighted_scores))))
        ax4.set_title('Contribution to Composite Score', size=12, weight='bold')

        # Overall title
        fig.suptitle(f'Property Investment Assessment Dashboard - {area_name}\n'
                     f'Composite Score: {composite_score:.1f} / 100  |  Grade: {grade}',
                     size=16, weight='bold', y=0.98)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"[OK] Dashboard saved to: {save_path}")

        plt.show()

    def _draw_gauge(self, ax, score):
        """Draw gauge chart"""
        # Clear axes
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-0.2, 1.2)
        ax.axis('off')

        # Draw arc background
        theta = np.linspace(0, np.pi, 100)
        r = 1

        # Background sectors (colored segments)
        segments = [
            (0, 50, '#e74c3c'),      # Red 0-50
            (50, 65, '#f39c12'),     # Orange 50-65
            (65, 85, '#3498db'),     # Blue 65-85
            (85, 100, '#2ecc71')     # Green 85-100
        ]

        for start, end, color in segments:
            theta_seg = np.linspace(np.pi * (1 - start/100), np.pi * (1 - end/100), 50)
            x_seg = r * np.cos(theta_seg)
            y_seg = r * np.sin(theta_seg)
            ax.fill_between(x_seg, 0, y_seg, alpha=0.3, color=color)

        # Draw needle
        angle = np.pi * (1 - score / 100)
        ax.plot([0, 0.9 * np.cos(angle)], [0, 0.9 * np.sin(angle)],
               'k-', linewidth=3)
        ax.plot(0, 0, 'ko', markersize=10)

        # Display score
        ax.text(0, -0.15, f'{score:.1f}', ha='center', va='center',
               size=24, weight='bold')

        # Scale labels
        for val in [0, 25, 50, 75, 100]:
            angle = np.pi * (1 - val / 100)
            x = 1.1 * np.cos(angle)
            y = 1.1 * np.sin(angle)
            ax.text(x, y, str(val), ha='center', va='center', size=9)

    def _get_color(self, score: float) -> str:
        """Return color based on score"""
        if score >= 85:
            return self.colors['excellent']
        elif score >= 65:
            return self.colors['good']
        elif score >= 50:
            return self.colors['medium']
        else:
            return self.colors['poor']


def main():
    """Example usage"""
    from property_investment_scorer import PropertyInvestmentScorer

    # Create scorer and visualizer
    scorer = PropertyInvestmentScorer()
    visualizer = PropertyVisualizer()

    # Example data
    area_data = {
        'population_growth': 2.5,
        'rental_yield': 5.5,
        'supply_ratio': 6.0,
        'vacancy_rate': 2.0,
        'mortgage_stress': 28.0
    }

    # Calculate score
    result = scorer.calculate_composite_score(area_data)

    # Generate comprehensive dashboard (all-in-one)
    print("Generating comprehensive dashboard...")
    visualizer.plot_composite_dashboard(result, "Example City A")


if __name__ == "__main__":
    main()
