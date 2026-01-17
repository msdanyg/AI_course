#!/usr/bin/env python3
"""
ML Pipeline Demo
================

This example demonstrates a complete machine learning workflow using the
ai_utils package. It covers:

1. Data validation
2. Preprocessing
3. Model training (simple example)
4. Evaluation

Run this script to see the utilities in action.

Usage:
    python examples/ml_pipeline_demo.py

Requirements:
    - Python 3.8+
    - No external dependencies (pure Python)
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_utils import preprocessing, evaluation, validation


def create_sample_dataset():
    """Create a sample dataset for demonstration."""
    # Simulated data: features for predicting if a student passes (1) or fails (0)
    # Features: [study_hours, sleep_hours, previous_score]
    data = [
        [5.0, 7.0, 75.0],
        [8.0, 8.0, 85.0],
        [3.0, 5.0, 55.0],
        [7.0, 7.0, 80.0],
        [2.0, 4.0, 45.0],
        [6.0, 6.0, 70.0],
        [9.0, 8.0, 90.0],
        [4.0, 6.0, 60.0],
        [1.0, 3.0, 40.0],
        [8.0, 7.0, 88.0],
        [5.0, None, 68.0],  # Missing value
        [6.0, 7.0, 72.0],
        [7.0, 8.0, 78.0],
        [3.0, 5.0, 50.0],
        [9.0, 9.0, 95.0],
    ]

    # Labels: 1 = pass, 0 = fail
    labels = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1]

    return data, labels


def demonstrate_validation(data, labels):
    """Demonstrate data validation utilities."""
    print("=" * 60)
    print("STEP 1: DATA VALIDATION")
    print("=" * 60)

    # Run comprehensive validation
    report = validation.validate_dataset(data, labels)

    print(f"\nDataset Summary:")
    print(f"  - Samples: {report['n_samples']}")
    print(f"  - Features: {report['n_features']}")
    print(f"  - Valid: {report['valid']}")

    if report['issues']:
        print(f"\nIssues Found ({len(report['issues'])}):")
        for issue in report['issues']:
            print(f"  [{issue['severity'].upper()}] {issue['type']}: {issue['message']}")

    if report['warnings']:
        print(f"\nWarnings:")
        for warning in report['warnings']:
            print(f"  - {warning}")

    # Detailed class balance check
    balance = validation.check_class_balance(labels)
    print(f"\nClass Distribution:")
    for cls, count in balance['class_counts'].items():
        prop = balance['class_proportions'][cls]
        print(f"  Class {cls}: {count} samples ({prop:.1%})")
    print(f"  Imbalance ratio: {balance['imbalance_ratio']:.2f}")

    return report


def demonstrate_preprocessing(data, labels):
    """Demonstrate preprocessing utilities."""
    print("\n" + "=" * 60)
    print("STEP 2: DATA PREPROCESSING")
    print("=" * 60)

    # First, handle missing values for each feature
    print("\n2.1 Handling Missing Values")
    print("-" * 40)

    # Transpose to work with features
    n_features = len(data[0])
    clean_data = []

    for sample in data:
        clean_sample = []
        for i, val in enumerate(sample):
            clean_sample.append(val)
        clean_data.append(clean_sample)

    # Fix missing values column by column
    for feat_idx in range(n_features):
        feature_values = [row[feat_idx] for row in clean_data]
        filled = preprocessing.handle_missing_values(feature_values, strategy='mean')
        for row_idx, val in enumerate(filled):
            clean_data[row_idx][feat_idx] = val

    missing_check = validation.check_missing_values(clean_data)
    print(f"  Missing values after imputation: {missing_check['total_missing']}")

    # Normalize features
    print("\n2.2 Feature Normalization")
    print("-" * 40)

    normalized_data = []
    for sample_idx, sample in enumerate(clean_data):
        normalized_data.append(sample.copy())

    # Normalize each feature independently
    for feat_idx in range(n_features):
        feature_values = [row[feat_idx] for row in clean_data]

        # Demonstrate different normalization methods
        if feat_idx == 0:
            normalized = preprocessing.normalize(feature_values, method='minmax')
            method_name = 'minmax [0,1]'
        elif feat_idx == 1:
            normalized = preprocessing.normalize(feature_values, method='zscore')
            method_name = 'z-score'
        else:
            normalized = preprocessing.normalize(feature_values, method='minmax', feature_range=(-1, 1))
            method_name = 'minmax [-1,1]'

        for row_idx, val in enumerate(normalized):
            normalized_data[row_idx][feat_idx] = val

        print(f"  Feature {feat_idx}: {method_name}")
        print(f"    Before: [{min(feature_values):.1f}, {max(feature_values):.1f}]")
        print(f"    After:  [{min(normalized):.2f}, {max(normalized):.2f}]")

    # Train/test split
    print("\n2.3 Train/Test Split")
    print("-" * 40)

    X_train, X_test, y_train, y_test = preprocessing.train_test_split(
        normalized_data, labels,
        test_size=0.2,
        random_seed=42,
        stratify=True
    )

    print(f"  Training samples: {len(X_train)}")
    print(f"  Test samples: {len(X_test)}")

    # Check stratification
    train_balance = validation.check_class_balance(y_train)
    test_balance = validation.check_class_balance(y_test)
    print(f"  Training class ratio: {train_balance['class_proportions']}")
    print(f"  Test class ratio: {test_balance['class_proportions']}")

    return X_train, X_test, y_train, y_test


def simple_threshold_classifier(X_train, y_train):
    """
    A simple classifier for demonstration.

    Predicts class based on average of normalized features.
    This is intentionally simple to demonstrate the evaluation metrics.
    """
    # Calculate mean feature value for each class
    class_means = {}
    for x, y in zip(X_train, y_train):
        avg = sum(x) / len(x)
        if y not in class_means:
            class_means[y] = []
        class_means[y].append(avg)

    # Calculate threshold as midpoint between class means
    mean_0 = sum(class_means.get(0, [0])) / max(len(class_means.get(0, [1])), 1)
    mean_1 = sum(class_means.get(1, [0])) / max(len(class_means.get(1, [1])), 1)
    threshold = (mean_0 + mean_1) / 2

    def predict(x):
        avg = sum(x) / len(x)
        return 1 if avg > threshold else 0

    return predict


def demonstrate_evaluation(X_train, X_test, y_train, y_test):
    """Demonstrate evaluation utilities."""
    print("\n" + "=" * 60)
    print("STEP 3: MODEL TRAINING & EVALUATION")
    print("=" * 60)

    # Train simple classifier
    print("\n3.1 Training Model")
    print("-" * 40)
    print("  Using simple threshold classifier for demonstration...")

    predict = simple_threshold_classifier(X_train, y_train)

    # Make predictions
    y_pred_train = [predict(x) for x in X_train]
    y_pred_test = [predict(x) for x in X_test]

    # Evaluate on training set
    print("\n3.2 Training Set Performance")
    print("-" * 40)

    train_metrics = evaluation.calculate_metrics(y_train, y_pred_train, task_type='classification')
    print(f"  Accuracy:  {train_metrics['accuracy']:.2%}")
    print(f"  Precision: {train_metrics['precision']:.2%}")
    print(f"  Recall:    {train_metrics['recall']:.2%}")
    print(f"  F1 Score:  {train_metrics['f1']:.2%}")

    # Evaluate on test set
    print("\n3.3 Test Set Performance")
    print("-" * 40)

    test_metrics = evaluation.calculate_metrics(y_test, y_pred_test, task_type='classification')
    print(f"  Accuracy:  {test_metrics['accuracy']:.2%}")
    print(f"  Precision: {test_metrics['precision']:.2%}")
    print(f"  Recall:    {test_metrics['recall']:.2%}")
    print(f"  F1 Score:  {test_metrics['f1']:.2%}")

    # Confusion matrix
    print("\n3.4 Confusion Matrix (Test Set)")
    print("-" * 40)

    matrix, labels_order = evaluation.confusion_matrix(y_test, y_pred_test)
    print(f"  Labels: {labels_order}")
    print("  Matrix:")
    print("           Predicted")
    print("              0    1")
    for i, row in enumerate(matrix):
        print(f"  Actual {labels_order[i]}  [{row[0]:3d}  {row[1]:3d}]")

    # Cross-validation
    print("\n3.5 Cross-Validation")
    print("-" * 40)

    # Combine data for cross-validation
    all_data = X_train + X_test
    all_labels = y_train + y_test

    cv_results = evaluation.cross_validate(
        model_fn=simple_threshold_classifier,
        data=all_data,
        labels=all_labels,
        k_folds=5,
        metric='accuracy',
        random_seed=42
    )

    print(f"  5-Fold CV Results:")
    print(f"    Fold scores: {[f'{s:.2%}' for s in cv_results['scores']]}")
    print(f"    Mean: {cv_results['mean']:.2%} (+/- {cv_results['std']:.2%})")


def demonstrate_encoding():
    """Demonstrate categorical encoding utilities."""
    print("\n" + "=" * 60)
    print("BONUS: CATEGORICAL ENCODING")
    print("=" * 60)

    categories = ['low', 'medium', 'high', 'low', 'high']

    print("\nOriginal categories:", categories)

    # Label encoding
    label_encoded = preprocessing.encode_categorical(categories, method='label')
    print(f"\nLabel encoding: {label_encoded}")

    # One-hot encoding
    onehot_encoded = preprocessing.encode_categorical(categories, method='onehot')
    print(f"\nOne-hot encoding:")
    for cat, vec in zip(categories, onehot_encoded):
        print(f"  {cat}: {vec}")

    # Ordinal encoding with explicit order
    ordinal_encoded = preprocessing.encode_categorical(
        categories,
        method='ordinal',
        categories=['low', 'medium', 'high']
    )
    print(f"\nOrdinal encoding (low=0, medium=1, high=2): {ordinal_encoded}")


def main():
    """Run the complete demonstration."""
    print("\n" + "#" * 60)
    print("# AI UTILITIES - ML PIPELINE DEMONSTRATION")
    print("#" * 60)

    # Create sample data
    data, labels = create_sample_dataset()

    # Step 1: Validation
    demonstrate_validation(data, labels)

    # Step 2: Preprocessing
    X_train, X_test, y_train, y_test = demonstrate_preprocessing(data, labels)

    # Step 3: Evaluation
    demonstrate_evaluation(X_train, X_test, y_train, y_test)

    # Bonus: Encoding
    demonstrate_encoding()

    print("\n" + "#" * 60)
    print("# DEMONSTRATION COMPLETE")
    print("#" * 60)
    print("\nFor more information, see the module docstrings:")
    print("  - ai_utils.preprocessing")
    print("  - ai_utils.evaluation")
    print("  - ai_utils.validation")
    print()


if __name__ == "__main__":
    main()
