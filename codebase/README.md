# Property Investment Comprehensive Assessment System

A Python-based system for evaluating property investment value by integrating 5 key metrics to provide comprehensive and accurate decision support for investors.

---

## Core Features

### Five-Dimension Assessment Metrics

| Dimension | Metric | Description | Weight |
|-----------|--------|-------------|--------|
| Demand | Population Growth | Directly drives housing demand, foundation for long-term price growth | 25% |
| Return | Rental Yield | Measures cash flow; high rental areas can support holding costs | 25% |
| Supply | New Dwelling Supply Ratio | High new supply suppresses future prices | 20% |
| Stability | Vacancy Rate | Indicates rental market tightness; low vacancy = high demand | 15% |
| Affordability | Mortgage Stress | High debt pressure makes market vulnerable to rate hikes | 15% |

### Scoring System

- **0-100 Scale**: Quantify each metric and overall performance
- **5-Tier Rating**: S (Excellent), A (Good), B (Above Average), C (Average), D (Below Average)
- **Weighted Calculation**: Customize weights based on different investment strategies

---

## Installation & Usage

### 1. Requirements

```bash
Python 3.7+
pip install numpy pandas matplotlib seaborn openpyxl
```

### 2. Quick Start

#### Run Analysis (Recommended)

```bash
python my_analysis.py
```

This will show everything in ONE comprehensive dashboard figure.

#### Customize Your Analysis

Edit `my_analysis.py` and modify:
- **SECTION 1**: Your property data (population growth, rental yield, etc.)
- **SECTION 2**: Weight strategy (default/conservative/aggressive/custom)
- **SECTION 3**: Enable multi-area comparison (optional)

Then run again:
```bash
python my_analysis.py
```

#### Code Usage

```python
from property_investment_scorer import PropertyInvestmentScorer
from property_visualizer import PropertyVisualizer

# Create scorer
scorer = PropertyInvestmentScorer()
visualizer = PropertyVisualizer()

# Input area data
area_data = {
    'population_growth': 2.5,    # Population growth rate 2.5%
    'rental_yield': 5.5,          # Rental yield 5.5%
    'supply_ratio': 6.0,          # New supply ratio 6%
    'vacancy_rate': 2.0,          # Vacancy rate 2%
    'mortgage_stress': 28.0       # Mortgage stress 28%
}

# Calculate composite score
result = scorer.calculate_composite_score(area_data)

# Print report
scorer.print_report(result, "Target Area")

# Generate comprehensive dashboard (all-in-one visualization)
# Includes: radar chart, bar chart, gauge, and pie chart
visualizer.plot_composite_dashboard(result, "Target Area")
```

#### Multi-Area Comparison

```python
# Prepare data for multiple areas
areas_data = {
    'Area A': {
        'population_growth': 2.8,
        'rental_yield': 4.2,
        'supply_ratio': 5.5,
        'vacancy_rate': 1.8,
        'mortgage_stress': 32.0
    },
    'Area B': {
        'population_growth': 3.2,
        'rental_yield': 5.8,
        'supply_ratio': 4.5,
        'vacancy_rate': 1.5,
        'mortgage_stress': 26.0
    }
}

# Batch comparison
comparison_df = scorer.compare_areas(areas_data)
print(comparison_df)

# Visualize comparison
visualizer.plot_comparison(comparison_df)
```

#### Custom Investment Strategy

```python
# Conservative investor: Emphasizes cash flow and stability
conservative_weights = {
    'population_growth': 0.15,
    'rental_yield': 0.35,       # Higher rental return weight
    'supply_ratio': 0.15,
    'vacancy_rate': 0.20,       # Higher stability weight
    'mortgage_stress': 0.15
}

scorer_conservative = PropertyInvestmentScorer(conservative_weights)
result = scorer_conservative.calculate_composite_score(area_data)
```

```python
# Aggressive investor: Emphasizes growth potential
aggressive_weights = {
    'population_growth': 0.40,  # Much higher growth weight
    'rental_yield': 0.15,
    'supply_ratio': 0.25,
    'vacancy_rate': 0.10,
    'mortgage_stress': 0.10
}

scorer_aggressive = PropertyInvestmentScorer(aggressive_weights)
result = scorer_aggressive.calculate_composite_score(area_data)
```

---

## Scoring Standards Explained

### 1. Population Growth

| Growth Rate | Score Range | Rating |
|------------|-------------|--------|
| ≥3.0% | 100 | Excellent |
| 2.0-3.0% | 85-100 | Very Good |
| 1.0-2.0% | 65-85 | Good |
| 0-1.0% | 40-65 | Average |
| <0% | 0-40 | Poor |

**Interpretation**: Population growth directly drives housing demand. High-growth areas typically have increasing job opportunities and strong long-term price appreciation potential.

### 2. Rental Yield

| Yield | Score Range | Rating |
|-------|-------------|--------|
| ≥7.0% | 100 | Excellent |
| 5.0-7.0% | 85-100 | Very Good |
| 3.0-5.0% | 60-85 | Good |
| 1.0-3.0% | 30-60 | Average |
| <1.0% | 0-30 | Poor |

**Interpretation**: Rental yield measures cash flow returns. High yields can cover holding costs and reduce investment risk.

### 3. New Dwelling Supply Ratio (Inverse Indicator)

| Ratio | Score Range | Rating |
|-------|-------------|--------|
| ≤3.0% | 100 | Balanced |
| 3.0-5.0% | 85-100 | Moderate Supply |
| 5.0-8.0% | 60-85 | High Supply |
| 8.0-12.0% | 30-60 | Oversupply |
| >12.0% | 0-30 | Severe Oversupply |

**Interpretation**: Excessive new supply dilutes demand and suppresses price growth. Low-supply areas have better appreciation potential.

### 4. Vacancy Rate (Inverse Indicator)

| Vacancy Rate | Score Range | Rating |
|--------------|-------------|--------|
| ≤1.5% | 100 | Extremely Tight |
| 1.5-2.5% | 85-100 | Supply Shortage |
| 2.5-4.0% | 60-85 | Balanced |
| 4.0-6.0% | 30-60 | Oversupply |
| >6.0% | 0-30 | Severe Oversupply |

**Interpretation**: Low vacancy indicates tight rental market, rental price pressure, and stable investment returns.

### 5. Mortgage Stress (Inverse Indicator)

| Stress Ratio | Score Range | Rating |
|-------------|-------------|--------|
| ≤15% | 100 | Very Low |
| 15-25% | 85-100 | Low |
| 25-35% | 60-85 | Moderate |
| 35-45% | 30-60 | High |
| >45% | 0-30 | Very High |

**Interpretation**: High mortgage stress areas are more vulnerable during rate hike cycles, prone to sell-offs affecting price stability.

---

## Visualization Features

### Composite Dashboard (Recommended - All-in-One)
A comprehensive 2x2 dashboard displaying everything you need in a single figure:
- **Top Left**: Radar chart showing 5-dimension assessment
- **Top Right**: Bar chart with dimension scores (color-coded)
- **Bottom Left**: Gauge chart displaying composite score
- **Bottom Right**: Pie chart showing each dimension's contribution

This is the recommended visualization as it provides complete insights without needing to close multiple windows.

### Individual Charts (Optional)
If needed, you can also generate individual charts:
- `plot_radar_chart()`: Standalone radar chart
- `plot_bar_chart()`: Standalone bar chart with scores and weights
- `plot_comparison()`: Multi-area comparison with heatmap

---

## Advanced Features

### 1. Sensitivity Analysis

Understand which metrics have the greatest impact on composite scores:

```python
# Test ±20% change in each metric's effect on composite score
# See example_sensitivity_analysis() in example_usage.py
```

### 2. Export Reports

```python
# Export Excel report
comparison_df.to_excel("property_investment_report.xlsx", index=False)
```

### 3. Batch Analysis

```python
# Analyze multiple areas simultaneously with automatic sorting
comparison_df = scorer.compare_areas(areas_data)
```

---

## File Descriptions

| File | Description |
|------|-------------|
| `property_investment_scorer.py` | Core scoring engine |
| `property_visualizer.py` | Data visualization module |
| `my_analysis.py` | **Main analysis file - Edit and run this! 主分析文件 - 编辑并运行!** |
| `quick_test.py` | Quick test script to verify installation |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation |

---

## Use Cases

### 1. Individual Investors
- Quickly assess target area investment value
- Compare multiple candidate areas
- Adjust weights based on personal risk tolerance

### 2. Real Estate Agents
- Provide data-backed professional advice to clients
- Generate visual reports to enhance persuasiveness

### 3. Investment Institutions
- Batch screen investment targets
- Establish standardized assessment processes
- Track changes in area investment values

---

## How to Use

### Step 1: Test Installation

```bash
python quick_test.py
```

### Step 2: Customize Your Analysis

Open `my_analysis.py` in any text editor and modify:

**SECTION 1 - Your Property Data:**
```python
my_property = {
    'population_growth': 2.5,    # Change this
    'rental_yield': 5.5,          # Change this
    'supply_ratio': 6.0,          # Change this
    'vacancy_rate': 2.0,          # Change this
    'mortgage_stress': 28.0       # Change this
}
```

**SECTION 2 - Choose Weight Strategy (Optional):**
- Default (Balanced) - Already active
- Conservative - Uncomment lines 41-48
- Aggressive - Uncomment lines 52-59
- Custom - Uncomment lines 63-70 and modify

**SECTION 3 - Compare Multiple Areas (Optional):**
- Set `compare_multiple_areas = True`
- Add your areas data

### Step 3: Run Analysis

```bash
python my_analysis.py
```

---

## Notes

### Data Source Recommendations
- **Population Growth**: Government statistics bureaus, urban planning departments
- **Rental Yield**: Real estate agencies, rental platform data
- **New Supply**: Building permit data, developer reports
- **Vacancy Rate**: Rental market reports, property management data
- **Mortgage Stress**: Financial institutions, economic research reports

### Usage Limitations
1. Scoring system based on historical experience, not investment advice
2. Should be combined with local policies and economic environment
3. Regularly update data to reflect market changes
4. Weight settings should match personal risk tolerance

### Improvement Suggestions
- Can adjust scoring standards for different countries/regions
- Can add more metrics (e.g., schools, transportation, employment)
- Can introduce time series analysis for trend forecasting

---

## Technical Architecture

```
Property Investment Assessment System
├── Data Input Layer
│   └── Raw data for 5 core metrics
├── Scoring Layer
│   ├── Single metric scoring functions (0-100)
│   └── Weighted composite scoring
├── Analysis Layer
│   ├── Single area analysis
│   ├── Multi-area comparison
│   └── Sensitivity analysis
└── Output Layer
    ├── Text reports
    ├── Data tables
    └── Visualization charts
```

---

## FAQ

**Q1: How to interpret composite scores?**
- 85+: Excellent area, high investment value
- 75-85: Good area, worth attention
- 65-75: Above average, needs further analysis
- 50-65: Average level, careful assessment needed
- <50: Poor performance, consider other areas

**Q2: How to set weights?**
- **Conservative**: Increase rental yield and vacancy rate weights, focus on cash flow and stability
- **Aggressive**: Increase population growth and supply ratio weights, pursue long-term appreciation
- **Balanced**: Use default weights, balance all factors

**Q3: How to handle missing data?**
- Try to obtain complete data
- If data missing, can estimate using area average or neighboring area data
- Mark data sources and quality for transparency

**Q4: How often to update data?**
- Population growth: Annual update
- Rental yield: Quarterly or semi-annual update
- New supply: Quarterly update
- Vacancy rate: Monthly or quarterly update
- Mortgage stress: Quarterly update

---

## Version History

### v1.0 (2025)
- Implemented 5-dimension metric scoring system
- Support single area analysis and multi-area comparison
- Provide radar charts, bar charts, dashboards and other visualizations
- Support custom weight strategies
- Added sensitivity analysis feature
