"""
Property Investment Analysis - Customizable

Instructions:
1. Modify the data in SECTION 1 to input your property data
2. (Optional) Modify weights in SECTION 2 to match your investment strategy
3. Run: python my_analysis.py
"""

from property_investment_scorer import PropertyInvestmentScorer
from property_visualizer import PropertyVisualizer


# ============================================================================
# SECTION 1: PROPERTY DATA
# ============================================================================
# Modify the values below with your property data

my_property = {
    'population_growth': 2.5,    # Population growth rate (%)
    'rental_yield': 5.5,          # Rental yield (%)
    'supply_ratio': 6.0,          # New dwelling supply ratio (%)
    'vacancy_rate': 2.0,          # Vacancy rate (%)
    'mortgage_stress': 28.0       # Mortgage stress (%)
}

# Property name for display
property_name = "My Target Property"


# ============================================================================
# SECTION 2: WEIGHT CONFIGURATION (OPTIONAL)
# ============================================================================
# Choose ONE of the following options by uncommenting it

# Option A: Default Weights (Balanced Strategy)
# Recommended for most investors
use_custom_weights = False
custom_weights = None


# Option B: Conservative Strategy
# Focus on cash flow and stability
# Uncomment the following 3 lines to use:
# use_custom_weights = True
# custom_weights = {
#     'population_growth': 0.15,    # Lower weight on growth
#     'rental_yield': 0.35,          # Higher weight on rental return
#     'supply_ratio': 0.15,
#     'vacancy_rate': 0.20,          # Higher weight on stability
#     'mortgage_stress': 0.15
# }


# Option C: Aggressive Strategy
# Focus on growth potential
# Uncomment the following 3 lines to use:
# use_custom_weights = True
# custom_weights = {
#     'population_growth': 0.40,    # Much higher weight on growth
#     'rental_yield': 0.15,
#     'supply_ratio': 0.25,          # Focus on supply pressure
#     'vacancy_rate': 0.10,
#     'mortgage_stress': 0.10
# }


# Option D: Custom Weights
# Define your own weights (must sum to 1.0)
# Uncomment the following 3 lines to use:
# use_custom_weights = True
# custom_weights = {
#     'population_growth': 0.25,
#     'rental_yield': 0.25,
#     'supply_ratio': 0.20,
#     'vacancy_rate': 0.15,
#     'mortgage_stress': 0.15
# }


# ============================================================================
# SECTION 3: MULTI-AREA COMPARISON (OPTIONAL)
# ============================================================================
# Set to True to compare multiple areas
compare_multiple_areas = False

# If comparing multiple areas, define them here
areas_data = {
    'Property A': {
        'population_growth': 2.8,
        'rental_yield': 5.5,
        'supply_ratio': 5.0,
        'vacancy_rate': 1.8,
        'mortgage_stress': 30.0
    },
    'Property B': {
        'population_growth': 3.2,
        'rental_yield': 6.0,
        'supply_ratio': 4.5,
        'vacancy_rate': 1.5,
        'mortgage_stress': 26.0
    },
    'Property C': {
        'population_growth': 2.0,
        'rental_yield': 4.8,
        'supply_ratio': 7.0,
        'vacancy_rate': 2.5,
        'mortgage_stress': 32.0
    }
}


# ============================================================================
# MAIN PROGRAM - DO NOT MODIFY BELOW
# ============================================================================

def main():
    """Main analysis function"""

    print("\n" + "="*70)
    print("Property Investment Analysis System")
    print("="*70)

    # Create scorer with appropriate weights
    if use_custom_weights and custom_weights:
        print("\n[CONFIG] Using custom weights")
        scorer = PropertyInvestmentScorer(custom_weights)
    else:
        print("\n[CONFIG] Using default balanced weights")
        scorer = PropertyInvestmentScorer()

    # Create visualizer
    visualizer = PropertyVisualizer()

    # Single property analysis
    if not compare_multiple_areas:
        print(f"\n[MODE] Single Property Analysis")
        print(f"[ANALYZING] {property_name}")

        # Calculate score
        result = scorer.calculate_composite_score(my_property)

        # Print detailed report
        scorer.print_report(result, property_name)

        # Show comprehensive dashboard
        print("\n[VISUALIZATION] Generating comprehensive dashboard...")
        print("[TIP] Close the chart window to exit")
        visualizer.plot_composite_dashboard(result, property_name)

    # Multi-area comparison
    else:
        print(f"\n[MODE] Multi-Area Comparison")
        print(f"[ANALYZING] {len(areas_data)} properties")

        # Batch comparison
        comparison_df = scorer.compare_areas(areas_data)

        # Display comparison table
        print("\n" + "="*70)
        print("[COMPARISON RESULTS]")
        print("="*70)
        print(comparison_df.to_string(index=False))

        # Show comparison visualization
        print("\n[VISUALIZATION] Generating comparison chart...")
        print("[TIP] Close the chart window to exit")
        visualizer.plot_comparison(comparison_df)

        # Show detailed report for top ranked property
        print("\n" + "="*70)
        print("[TOP PROPERTY DETAIL]")
        print("="*70)
        top_property = comparison_df.iloc[0]['Area']
        result = scorer.calculate_composite_score(areas_data[top_property])
        scorer.print_report(result, top_property)

    print("\n" + "="*70)
    print("[DONE] Analysis completed")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED] Analysis stopped by user")
    except Exception as e:
        print(f"\n\n[ERROR] An error occurred: {e}")
        import traceback
        traceback.print_exc()
