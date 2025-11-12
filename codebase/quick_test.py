"""
Quick Test Script
Verify the Property Investment Assessment System is working correctly
"""

import sys
import io

# Set UTF-8 encoding for output (fix Windows console display issues)
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from property_investment_scorer import PropertyInvestmentScorer
from property_visualizer import PropertyVisualizer


def quick_test():
    """Quick test of all core functions"""
    print("\n" + "="*60)
    print("[TEST] Property Investment Assessment System - Quick Test")
    print("="*60)

    try:
        # 1. Test scorer
        print("\n[1/4] Testing scorer...")
        scorer = PropertyInvestmentScorer()
        print("[OK] Scorer created successfully")

        # 2. Test single area scoring
        print("\n[2/4] Testing single area scoring...")
        test_data = {
            'population_growth': 2.5,
            'rental_yield': 5.5,
            'supply_ratio': 6.0,
            'vacancy_rate': 2.0,
            'mortgage_stress': 28.0
        }
        result = scorer.calculate_composite_score(test_data)
        print(f"[OK] Calculation successful - Composite Score: {result['composite_score']:.2f} | Grade: {result['grade']}")

        # 3. Test multi-area comparison
        print("\n[3/4] Testing multi-area comparison...")
        areas_data = {
            'Test Area A': {
                'population_growth': 3.0,
                'rental_yield': 6.0,
                'supply_ratio': 5.0,
                'vacancy_rate': 1.5,
                'mortgage_stress': 25.0
            },
            'Test Area B': {
                'population_growth': 2.0,
                'rental_yield': 4.5,
                'supply_ratio': 7.0,
                'vacancy_rate': 2.5,
                'mortgage_stress': 30.0
            }
        }
        comparison_df = scorer.compare_areas(areas_data)
        print("[OK] Multi-area comparison successful")
        print("\nComparison Results:")
        print(comparison_df.to_string(index=False))

        # 4. Test visualization module (without displaying charts)
        print("\n[4/4] Testing visualization module...")
        visualizer = PropertyVisualizer()
        print("[OK] Visualization tool created successfully")

        # 5. Print detailed report
        print("\n" + "="*60)
        print("[REPORT] Test Area A - Detailed Report")
        print("="*60)
        result_a = scorer.calculate_composite_score(areas_data['Test Area A'])
        scorer.print_report(result_a, "Test Area A")

        # Test successful
        print("\n" + "="*60)
        print("[SUCCESS] All tests passed! System is working properly.")
        print("="*60)
        print("\n[TIPS]")
        print("   - Run 'python example_usage.py' to see complete examples")
        print("   - Check 'README.md' for detailed documentation")
        print("   - Modify test_data and areas_data to test your own data")
        print()

        return True

    except ImportError as e:
        print(f"\n[ERROR] Import error: {e}")
        print("\nPlease install dependencies first:")
        print("   pip install -r requirements.txt")
        return False

    except Exception as e:
        print(f"\n[ERROR] Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = quick_test()
    exit(0 if success else 1)
