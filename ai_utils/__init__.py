"""
AI Utilities Package
====================

A comprehensive collection of utilities for machine learning and AI workflows.

This package provides commonly-needed functions for:
- Data preprocessing and transformation
- Model evaluation and metrics calculation
- Data validation and quality checks

Modules
-------
preprocessing
    Data cleaning, normalization, and feature engineering utilities.
evaluation
    Model performance metrics and evaluation helpers.
validation
    Data quality checks and input validation.

Quick Start
-----------
>>> from ai_utils import preprocessing, evaluation
>>> # Normalize your data
>>> normalized = preprocessing.normalize(data, method='minmax')
>>> # Evaluate model performance
>>> metrics = evaluation.calculate_metrics(y_true, y_pred)

Version
-------
0.1.0

Author
------
AI Course Contributors

License
-------
MIT License
"""

__version__ = "0.1.0"
__author__ = "AI Course Contributors"

from . import preprocessing
from . import evaluation
from . import validation

__all__ = [
    "preprocessing",
    "evaluation",
    "validation",
    "__version__",
    "__author__",
]
