"""
Property Investment Comprehensive Scoring System

Evaluates 5 core metrics:
1. Population Growth - Demand dimension
2. Rental Yield - Return dimension
3. New Dwelling Supply Ratio - Supply dimension
4. Vacancy Rate - Stability dimension
5. Mortgage Stress - Affordability dimension
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from typing import Dict, List, Optional
import warnings

warnings.filterwarnings('ignore')

# Configure font for display
rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
rcParams['axes.unicode_minus'] = False


class PropertyInvestmentScorer:
    """Property Investment Scorer"""

    def __init__(self, custom_weights: Optional[Dict[str, float]] = None):
        """
        Initialize scorer

        Args:
            custom_weights: Custom weight dictionary, e.g. {'population_growth': 0.25, ...}
        """
        # Default weights (can be adjusted based on investment strategy)
        self.default_weights = {
            'population_growth': 0.25,    # Population growth - long-term demand foundation
            'rental_yield': 0.25,          # Rental yield - cash flow
            'supply_ratio': 0.20,          # New dwelling supply ratio - supply pressure
            'vacancy_rate': 0.15,          # Vacancy rate - market tightness
            'mortgage_stress': 0.15        # Mortgage stress - market stability
        }

        self.weights = custom_weights if custom_weights else self.default_weights
        self._validate_weights()

        # Metric names (for display)
        self.metric_names = {
            'population_growth': 'Population Growth',
            'rental_yield': 'Rental Yield',
            'supply_ratio': 'Supply Ratio',
            'vacancy_rate': 'Vacancy Rate',
            'mortgage_stress': 'Mortgage Stress'
        }

        # Metric icons
        self.metric_icons = {
            'population_growth': 'DEMAND',
            'rental_yield': 'RETURN',
            'supply_ratio': 'SUPPLY',
            'vacancy_rate': 'STABLE',
            'mortgage_stress': 'AFFORD'
        }

    def _validate_weights(self):
        """Validate weights sum to 1"""
        total = sum(self.weights.values())
        if not np.isclose(total, 1.0, atol=0.01):
            raise ValueError(f"Weights must sum to 1.0, currently {total:.2f}")

    def score_population_growth(self, growth_rate: float) -> float:
        """
        Score: Population growth rate (higher is better)

        Args:
            growth_rate: Annual population growth rate (%), e.g. 2.5 means 2.5%

        Returns:
            Score 0-100
        """
        if growth_rate >= 3.0:
            return 100
        elif growth_rate >= 2.0:
            return 85 + (growth_rate - 2.0) * 15
        elif growth_rate >= 1.0:
            return 65 + (growth_rate - 1.0) * 20
        elif growth_rate >= 0:
            return 40 + growth_rate * 25
        else:  # Negative growth
            return max(0, 40 + growth_rate * 20)

    def score_rental_yield(self, yield_rate: float) -> float:
        """
        Score: Rental yield (higher is better)

        Args:
            yield_rate: Rental yield (%), e.g. 5.5 means 5.5%

        Returns:
            Score 0-100
        """
        if yield_rate >= 7.0:
            return 100
        elif yield_rate >= 5.0:
            return 85 + (yield_rate - 5.0) * 7.5
        elif yield_rate >= 3.0:
            return 60 + (yield_rate - 3.0) * 12.5
        elif yield_rate >= 1.0:
            return 30 + (yield_rate - 1.0) * 15
        else:
            return max(0, yield_rate * 30)

    def score_supply_ratio(self, supply_ratio: float) -> float:
        """
        Score: New dwelling supply ratio (lower is better, inverse indicator)

        Args:
            supply_ratio: New supply to stock ratio (%), e.g. 8.0 means 8%

        Returns:
            Score 0-100
        """
        if supply_ratio <= 3.0:
            return 100
        elif supply_ratio <= 5.0:
            return 85 + (5.0 - supply_ratio) * 7.5
        elif supply_ratio <= 8.0:
            return 60 + (8.0 - supply_ratio) * 8.33
        elif supply_ratio <= 12.0:
            return 30 + (12.0 - supply_ratio) * 7.5
        else:
            return max(0, 30 - (supply_ratio - 12.0) * 5)

    def score_vacancy_rate(self, vacancy_rate: float) -> float:
        """
        Score: Vacancy rate (lower is better, inverse indicator)

        Args:
            vacancy_rate: Vacancy rate (%), e.g. 2.5 means 2.5%

        Returns:
            Score 0-100
        """
        if vacancy_rate <= 1.5:
            return 100
        elif vacancy_rate <= 2.5:
            return 85 + (2.5 - vacancy_rate) * 15
        elif vacancy_rate <= 4.0:
            return 60 + (4.0 - vacancy_rate) * 16.67
        elif vacancy_rate <= 6.0:
            return 30 + (6.0 - vacancy_rate) * 15
        else:
            return max(0, 30 - (vacancy_rate - 6.0) * 10)

    def score_mortgage_stress(self, stress_ratio: float) -> float:
        """
        Score: Mortgage stress (lower is better, inverse indicator)

        Args:
            stress_ratio: Income used for mortgage repayment (%), e.g. 30.0 means 30%

        Returns:
            Score 0-100
        """
        if stress_ratio <= 15.0:
            return 100
        elif stress_ratio <= 25.0:
            return 85 + (25.0 - stress_ratio) * 1.5
        elif stress_ratio <= 35.0:
            return 60 + (35.0 - stress_ratio) * 2.5
        elif stress_ratio <= 45.0:
            return 30 + (45.0 - stress_ratio) * 3.0
        else:
            return max(0, 30 - (stress_ratio - 45.0) * 3)

    def calculate_scores(self, data: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate all metric scores

        Args:
            data: Dictionary containing all metric raw data
                {
                    'population_growth': 2.5,
                    'rental_yield': 5.5,
                    'supply_ratio': 6.0,
                    'vacancy_rate': 2.0,
                    'mortgage_stress': 28.0
                }

        Returns:
            Dictionary of metric scores
        """
        scores = {
            'population_growth': self.score_population_growth(data['population_growth']),
            'rental_yield': self.score_rental_yield(data['rental_yield']),
            'supply_ratio': self.score_supply_ratio(data['supply_ratio']),
            'vacancy_rate': self.score_vacancy_rate(data['vacancy_rate']),
            'mortgage_stress': self.score_mortgage_stress(data['mortgage_stress'])
        }
        return scores

    def calculate_composite_score(self, data: Dict[str, float]) -> Dict:
        """
        Calculate composite score

        Args:
            data: Dictionary containing all metric raw data

        Returns:
            Dictionary containing detailed score information
        """
        # Calculate individual scores
        scores = self.calculate_scores(data)

        # Calculate weighted composite score
        composite_score = sum(scores[key] * self.weights[key] for key in scores)

        # Generate grade
        grade = self._get_grade(composite_score)

        return {
            'raw_data': data,
            'individual_scores': scores,
            'composite_score': round(composite_score, 2),
            'grade': grade,
            'weights': self.weights
        }

    def _get_grade(self, score: float) -> str:
        """Get grade based on score"""
        if score >= 85:
            return 'S (Excellent)'
        elif score >= 75:
            return 'A (Good)'
        elif score >= 65:
            return 'B (Above Average)'
        elif score >= 50:
            return 'C (Average)'
        else:
            return 'D (Below Average)'

    def print_report(self, result: Dict, area_name: str = "Assessment Area"):
        """
        Print assessment report

        Args:
            result: Result from calculate_composite_score
            area_name: Area name
        """
        print("\n" + "="*60)
        print(f"Property Investment Assessment Report - {area_name}")
        print("="*60)

        print("\n[Raw Data]")
        for key, value in result['raw_data'].items():
            icon = self.metric_icons[key]
            name = self.metric_names[key]
            unit = '%'
            print(f"  [{icon:6s}] {name:20s}: {value:6.2f}{unit}")

        print("\n[Dimension Scores] (0-100 scale)")
        for key, score in result['individual_scores'].items():
            icon = self.metric_icons[key]
            name = self.metric_names[key]
            weight = result['weights'][key]
            bar = '=' * int(score / 5)
            print(f"  [{icon:6s}] {name:20s}: {score:5.1f} (weight {weight*100:4.1f}%) {bar}")

        print("\n[Overall Assessment]")
        print(f"  Composite Score: {result['composite_score']:.2f} / 100")
        print(f"  Investment Grade: {result['grade']}")

        # Give investment recommendation
        self._print_suggestion(result)

        print("="*60 + "\n")

    def _print_suggestion(self, result: Dict):
        """Print investment suggestion"""
        score = result['composite_score']
        scores = result['individual_scores']

        print("\n[Investment Recommendation]")
        if score >= 85:
            print("  [STRONG BUY] Area shows excellent performance with high investment value")
        elif score >= 75:
            print("  [BUY] Area shows good performance, worth serious consideration")
        elif score >= 65:
            print("  [HOLD] Area shows above average performance, further analysis recommended")
        elif score >= 50:
            print("  [CAUTION] Area shows average performance, careful risk assessment needed")
        else:
            print("  [AVOID] Area shows weak performance, consider other locations")

        # Identify weak points
        weak_points = [k for k, v in scores.items() if v < 60]
        if weak_points:
            print(f"\n  [ATTENTION] Areas requiring attention:")
            for key in weak_points:
                name = self.metric_names[key]
                score = scores[key]
                print(f"     - {name}: Low score ({score:.1f})")

    def compare_areas(self, areas_data: Dict[str, Dict[str, float]]) -> pd.DataFrame:
        """
        Batch compare multiple areas

        Args:
            areas_data: Data dictionary for multiple areas
                {
                    'Sydney': {'population_growth': 2.5, ...},
                    'Melbourne': {'population_growth': 2.0, ...}
                }

        Returns:
            Comparison results DataFrame
        """
        results = []
        for area_name, data in areas_data.items():
            result = self.calculate_composite_score(data)
            row = {
                'Area': area_name,
                'Composite Score': result['composite_score'],
                'Grade': result['grade']
            }
            # Add individual scores
            for key, score in result['individual_scores'].items():
                row[self.metric_names[key]] = round(score, 1)
            results.append(row)

        df = pd.DataFrame(results)
        df = df.sort_values('Composite Score', ascending=False)
        return df


def main():
    """Example usage"""
    # Create scorer (using default weights)
    scorer = PropertyInvestmentScorer()

    # Example: Evaluate a single area
    area_data = {
        'population_growth': 2.5,   # Population growth rate 2.5%
        'rental_yield': 5.5,         # Rental yield 5.5%
        'supply_ratio': 6.0,         # New supply ratio 6%
        'vacancy_rate': 2.0,         # Vacancy rate 2%
        'mortgage_stress': 28.0      # Mortgage stress 28%
    }

    result = scorer.calculate_composite_score(area_data)
    scorer.print_report(result, "Example City")


if __name__ == "__main__":
    main()
