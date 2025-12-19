# Predicting last-mile delivery route deviations using machine learning

A machine learning system for classifying delivery routes based on whether or not the driver will deviate from the proposed optimal route and predicting route quality scores using deep learning models. This work has been published in a peer-reviewed journal.

## Project Overview

This project analyzes real-world delivery route data to:
- **Classify routes** based on their characteristics and execution patterns
- **Predict quality scores** for routes using LSTM, CNN and Attention-based neural networks
- Regression and classification models quantify and predict route deviations
- Route deviation metrics to measure the similarity of routes.
- Models use sequential route structure, route attributes, and driver information.
- Exploring tacit driver knowledge for efficient route planning.
- Publicly available dataset supports further research.
- Future opportunities: identify optimization opportunities for planned routes

This work has been published in the peer-reviewed journal "Expert Systems with Applications". Please cite this work when using the code or methods.

[FULL PAPER HERE](https://doi.org/10.1016/j.eswa.2025.129921)

[Anonymized dataset](https://data.mendeley.com/datasets/kkwgfvmtxn/1)

**Please note**: Project notebooks used the full available company dataset. All sensitive company information is hidden and not available to view in output cells.


**Citation Information:**
```


Anna Konovalenko, Lars Magnus Hvattum, Kim Aleksander Hammer Iversen,
Predicting last-mile delivery route deviations using machine learning,
Expert Systems with Applications,
Volume 298, Part D,
2026,
129921,
ISSN 0957-4174,
https://doi.org/10.1016/j.eswa.2025.129921.
(https://www.sciencedirect.com/science/article/pii/S0957417425035365)

```


The system processes actual delivery data from logistics operations, comparing planned routes with routes executed by drivers to quantify delivery efficiency and identify improvement areas.
<img width="592" height="294" alt="Screenshot 2025-12-19 at 12 22 56" src="https://github.com/user-attachments/assets/43bb39f8-3c74-4e34-a2ad-471fe2aaa48e" />

## Key Features

- **Multiple Classification Models**: Baseline, K-Fold, and larger architecture variants
- **Advanced Regression Models**:
  - LSTM-based score prediction
  - Attention-based score prediction
  - Larger filtered architectures
  - K-Fold cross-validated models
- **Geospatial Analysis**: Distance calculations and route optimization metrics
- **Route Quality Scoring**: Levenshtein distance-based route deviation measurement
- **Interactive Visualizations**: HTML-based route comparisons and mapping

## Project Structure

```
RealDataClassificator/
├── src/                              # Source code modules
│   ├── __init__.py
│   ├── route_analysis.py            # Route comparison and quality metrics
│   ├── geospatial.py                # Distance calculations and geospatial utilities
│   ├── models/                      # Model architectures
│   ├── data/                        # Data loading and preprocessing
│   └── evaluation.py                # Model evaluation metrics
│
├── notebooks/                        # Jupyter notebooks organized by workflow stage
│   ├── exploratory/
│   │   └── main.ipynb               # Initial data exploration
│   │
│   ├── modeling/                    # ⭐ Final model implementations (tracked in git)
│   │   ├── classification_v2_final.ipynb    # Final classification model
│   │   ├── regression_final.ipynb           # Final regression model
│   │   ├── classification_v1.ipynb
│   │   └── classification_v0.ipynb
│   │
│   └── utils/                       # Utility notebooks
│       ├── basic_functions.ipynb
│       └── maps.ipynb
│
├── src/                             # Source code modules (tracked in git)
│   ├── __init__.py
│   ├── route_analysis.py
│   ├── geospatial.py
│   ├── models/
│   ├── data/
│   └── evaluation.py
│
├── config/                          # Configuration files (tracked in git)
│   └── config.yaml
│
├── requirements.txt                 # Python dependencies
├── setup.py                         # Package installation
├── .gitignore                       # Git ignore patterns
└── README.md                        # This file
```


## Installation & Setup

### Prerequisites
- Python 3.7+
```
Install dependencies:
pip install -r requirements.txt
```

## Model Descriptions

### Final Models (Production)

#### Classification v2 Final (`classification_v2_final.ipynb`)
**Task:** Binary classification - predicts if a route will be executed correctly or deviate

**Architectures:**
- Bidirectional LSTM
- Multi Head Attention
- CNN (Convolutional)
- GRU (Gated Recurrent Unit)

**Features:**
- 4 neural network models with cross-validation
- Route quality scoring based on planned vs. actual execution
- Benchmarking and baseline comparison
- Geographic features (country detection)
- Evaluation: Accuracy, Precision, Recall, F1, ROC-AUC

#### Regression Final (`regression_final.ipynb`)
**Task:** Continuous value regression - predicts route quality scores

**Architectures:**
- Standard RNN
- CNN (Convolutional)
- Attention-based model

**Features:**
- 3 neural network models with K-Fold cross-validation
- Predicts quality scores (0-1 range)
- Evaluation: MSE, RMSE, MAE, R² score
- Enhanced training (512 batch size, 100 epochs, 0.001 learning rate)
- Model performance comparison

## Data Format

Input data should include:

- `driver_id` - Driver identifier
- `planned_route_location` - List of planned stops
- `actual_route_unique` - List of actual stops visited
- `arriving_time` - Arrival times at each stop
- `distance_route` - Planned distances between stops
- `distance_actual_route` - Actual distances between stops
- `stop_earliest` - Earliest time window for stops
- `stop_latest` - Latest time window for stops
- `day_of_week` - Day of delivery
- `date` - Delivery date
- `country_flag` - Country/region
- Additional features as needed


**Last Updated:** December 19, 2024
