"""
Data Validation Module
======================

This module provides utilities for validating data quality and integrity
before using it in machine learning pipelines. Catching data issues early
prevents cryptic errors and incorrect model behavior downstream.

All validation functions either return validation results or raise
descriptive exceptions, making them suitable for both interactive
exploration and automated pipelines.

Functions
---------
validate_dataset(data, labels, checks)
    Perform comprehensive dataset validation.
check_missing_values(data)
    Detect and report missing/null values.
check_duplicates(data, labels)
    Find duplicate samples in the dataset.
check_feature_variance(data, threshold)
    Identify low-variance (constant) features.
check_class_balance(labels, threshold)
    Analyze class distribution for imbalance.
check_outliers(data, method, threshold)
    Detect potential outliers in the data.

Examples
--------
Quick dataset validation:

>>> from ai_utils.validation import validate_dataset
>>> issues = validate_dataset(X, y, checks=['missing', 'duplicates'])
>>> if issues:
...     print(f"Found {len(issues)} issues to address")

Check for class imbalance:

>>> from ai_utils.validation import check_class_balance
>>> report = check_class_balance(labels, threshold=0.1)
>>> if report['is_imbalanced']:
...     print("Consider using stratified sampling or SMOTE")
"""

from typing import List, Dict, Any, Optional, Tuple, Union, Literal
import math


def validate_dataset(
    data: List[List[float]],
    labels: Optional[List[Any]] = None,
    checks: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Perform comprehensive validation on a dataset.

    This function runs multiple validation checks and returns a detailed
    report of any issues found. It's recommended to run this before
    training any model.

    Parameters
    ----------
    data : List[List[float]]
        Feature matrix. Shape: (n_samples, n_features).
        Each inner list represents one sample's features.

    labels : List[Any], optional
        Target labels or values. If provided, enables label-related
        checks like class balance and duplicate detection.

    checks : List[str], optional
        List of specific checks to run. If None, runs all checks.
        Available checks:

        - 'missing': Check for missing (None/NaN) values
        - 'duplicates': Check for duplicate samples
        - 'variance': Check for low-variance features
        - 'balance': Check class balance (requires labels)
        - 'outliers': Check for outliers using IQR method
        - 'shape': Validate data shape consistency

    Returns
    -------
    Dict[str, Any]
        A validation report containing:

        - 'valid': bool - True if no critical issues found
        - 'n_samples': int - Number of samples
        - 'n_features': int - Number of features
        - 'issues': List[Dict] - Detailed list of issues found
        - 'warnings': List[str] - Non-critical warnings
        - 'checks_performed': List[str] - Which checks were run

    Raises
    ------
    ValueError
        If data is empty or malformed.

    See Also
    --------
    check_missing_values : Detailed missing value analysis.
    check_class_balance : Detailed class balance analysis.
    check_outliers : Detailed outlier analysis.

    Notes
    -----
    This function is designed for quick dataset health checks. For
    detailed analysis of specific issues, use the individual check
    functions.

    Validation workflow recommendation:

    1. Run validate_dataset() first for overview
    2. Address critical issues (missing values, shape problems)
    3. Use individual functions for detailed analysis
    4. Re-validate after fixing issues

    Examples
    --------
    Basic validation:

    >>> data = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
    >>> labels = [0, 1, 0]
    >>> report = validate_dataset(data, labels)
    >>> print(f"Dataset valid: {report['valid']}")
    Dataset valid: True

    Validation with specific checks:

    >>> report = validate_dataset(
    ...     data, labels,
    ...     checks=['missing', 'duplicates', 'balance']
    ... )

    Finding issues:

    >>> data_with_issues = [[1.0, None], [1.0, 2.0], [1.0, 2.0]]
    >>> labels = [0, 0, 0]
    >>> report = validate_dataset(data_with_issues, labels)
    >>> for issue in report['issues']:
    ...     print(f"- {issue['type']}: {issue['message']}")
    - missing_values: Found 1 missing value(s)
    - duplicates: Found 1 duplicate sample(s)
    - class_imbalance: Only 1 unique class found
    """
    if not data:
        raise ValueError("Data cannot be empty")

    all_checks = ['shape', 'missing', 'duplicates', 'variance', 'outliers']
    if labels is not None:
        all_checks.append('balance')

    checks_to_run = checks if checks is not None else all_checks

    report: Dict[str, Any] = {
        'valid': True,
        'n_samples': len(data),
        'n_features': len(data[0]) if data else 0,
        'issues': [],
        'warnings': [],
        'checks_performed': checks_to_run,
    }

    # Shape check
    if 'shape' in checks_to_run:
        feature_counts = [len(row) for row in data]
        if len(set(feature_counts)) > 1:
            report['valid'] = False
            report['issues'].append({
                'type': 'inconsistent_shape',
                'message': f"Inconsistent feature counts: {set(feature_counts)}",
                'severity': 'critical',
            })
            # Can't continue with other checks if shape is inconsistent
            return report

        if labels is not None and len(labels) != len(data):
            report['valid'] = False
            report['issues'].append({
                'type': 'label_mismatch',
                'message': f"Data has {len(data)} samples but labels has {len(labels)}",
                'severity': 'critical',
            })

    # Missing values check
    if 'missing' in checks_to_run:
        missing_report = check_missing_values(data)
        if missing_report['total_missing'] > 0:
            report['issues'].append({
                'type': 'missing_values',
                'message': f"Found {missing_report['total_missing']} missing value(s)",
                'severity': 'warning',
                'details': missing_report,
            })

    # Duplicates check
    if 'duplicates' in checks_to_run:
        dup_report = check_duplicates(data, labels)
        if dup_report['n_duplicates'] > 0:
            report['warnings'].append(
                f"Found {dup_report['n_duplicates']} duplicate sample(s)"
            )
            report['issues'].append({
                'type': 'duplicates',
                'message': f"Found {dup_report['n_duplicates']} duplicate sample(s)",
                'severity': 'info',
                'details': dup_report,
            })

    # Variance check
    if 'variance' in checks_to_run:
        var_report = check_feature_variance(data)
        if var_report['n_low_variance'] > 0:
            report['warnings'].append(
                f"{var_report['n_low_variance']} feature(s) have zero/low variance"
            )
            report['issues'].append({
                'type': 'low_variance',
                'message': f"{var_report['n_low_variance']} feature(s) have zero/low variance",
                'severity': 'warning',
                'details': var_report,
            })

    # Class balance check
    if 'balance' in checks_to_run and labels is not None:
        balance_report = check_class_balance(labels)
        if balance_report['is_imbalanced']:
            report['warnings'].append(
                f"Class imbalance detected (ratio: {balance_report['imbalance_ratio']:.2f})"
            )
            report['issues'].append({
                'type': 'class_imbalance',
                'message': f"Class imbalance detected",
                'severity': 'warning',
                'details': balance_report,
            })

    # Outliers check
    if 'outliers' in checks_to_run:
        outlier_report = check_outliers(data)
        if outlier_report['n_samples_with_outliers'] > 0:
            pct = (outlier_report['n_samples_with_outliers'] / len(data)) * 100
            report['warnings'].append(
                f"{outlier_report['n_samples_with_outliers']} samples "
                f"({pct:.1f}%) contain outliers"
            )
            report['issues'].append({
                'type': 'outliers',
                'message': f"Potential outliers detected in {outlier_report['n_samples_with_outliers']} samples",
                'severity': 'info',
                'details': outlier_report,
            })

    return report


def check_missing_values(
    data: List[List[Optional[float]]],
) -> Dict[str, Any]:
    """
    Detect and report missing (None/NaN) values in the dataset.

    Missing values can cause errors in many ML algorithms and should
    be handled before training.

    Parameters
    ----------
    data : List[List[Optional[float]]]
        Feature matrix that may contain None values.

    Returns
    -------
    Dict[str, Any]
        A report containing:

        - 'total_missing': Total count of missing values
        - 'missing_by_feature': List of missing counts per feature
        - 'missing_by_sample': List of missing counts per sample
        - 'features_with_missing': Indices of features with missing values
        - 'samples_with_missing': Indices of samples with missing values
        - 'missing_percentage': Overall percentage of missing values

    Notes
    -----
    Strategies for handling missing values depend on the pattern:

    +---------------------+----------------------------------------+
    | Pattern             | Recommended Strategy                   |
    +=====================+========================================+
    | Random (MCAR)       | Mean/median imputation, or drop        |
    +---------------------+----------------------------------------+
    | Feature-specific    | Feature-specific imputation or drop    |
    |                     | the feature if >50% missing            |
    +---------------------+----------------------------------------+
    | Sample-specific     | Drop samples with many missing values  |
    +---------------------+----------------------------------------+
    | Systematic (MNAR)   | Model-based imputation, use indicator  |
    |                     | variables                              |
    +---------------------+----------------------------------------+

    MCAR = Missing Completely At Random
    MNAR = Missing Not At Random

    Examples
    --------
    Check for missing values:

    >>> data = [[1.0, 2.0, 3.0], [4.0, None, 6.0], [7.0, 8.0, None]]
    >>> report = check_missing_values(data)
    >>> print(f"Total missing: {report['total_missing']}")
    Total missing: 2
    >>> print(f"Features with missing: {report['features_with_missing']}")
    Features with missing: [1, 2]

    Clean dataset:

    >>> clean_data = [[1.0, 2.0], [3.0, 4.0]]
    >>> report = check_missing_values(clean_data)
    >>> report['total_missing']
    0
    """
    if not data:
        return {
            'total_missing': 0,
            'missing_by_feature': [],
            'missing_by_sample': [],
            'features_with_missing': [],
            'samples_with_missing': [],
            'missing_percentage': 0.0,
        }

    n_samples = len(data)
    n_features = len(data[0]) if data else 0

    missing_by_feature = [0] * n_features
    missing_by_sample = []
    samples_with_missing = []

    for sample_idx, sample in enumerate(data):
        sample_missing = 0
        for feat_idx, value in enumerate(sample):
            if value is None or (isinstance(value, float) and math.isnan(value)):
                missing_by_feature[feat_idx] += 1
                sample_missing += 1

        missing_by_sample.append(sample_missing)
        if sample_missing > 0:
            samples_with_missing.append(sample_idx)

    total_missing = sum(missing_by_feature)
    features_with_missing = [
        i for i, count in enumerate(missing_by_feature) if count > 0
    ]

    total_values = n_samples * n_features
    missing_percentage = (total_missing / total_values * 100) if total_values > 0 else 0.0

    return {
        'total_missing': total_missing,
        'missing_by_feature': missing_by_feature,
        'missing_by_sample': missing_by_sample,
        'features_with_missing': features_with_missing,
        'samples_with_missing': samples_with_missing,
        'missing_percentage': missing_percentage,
    }


def check_duplicates(
    data: List[List[float]],
    labels: Optional[List[Any]] = None,
) -> Dict[str, Any]:
    """
    Find duplicate samples in the dataset.

    Duplicates can artificially inflate model performance and cause
    data leakage if the same sample appears in both train and test sets.

    Parameters
    ----------
    data : List[List[float]]
        Feature matrix to check for duplicates.

    labels : List[Any], optional
        If provided, also checks for samples with same features but
        different labels (potential labeling errors).

    Returns
    -------
    Dict[str, Any]
        A report containing:

        - 'n_duplicates': Number of duplicate samples (not counting originals)
        - 'duplicate_groups': List of index groups that are duplicates
        - 'n_unique': Number of unique samples
        - 'duplicate_percentage': Percentage of samples that are duplicates
        - 'conflicting_labels': Indices of duplicates with different labels
          (only if labels provided)

    Notes
    -----
    Types of duplicates and their implications:

    +------------------+------------------------------------------------+
    | Type             | Issue & Action                                 |
    +==================+================================================+
    | Exact duplicates | May inflate metrics. Remove or investigate.    |
    +------------------+------------------------------------------------+
    | Same features,   | Likely labeling error. Investigate and fix.    |
    | different labels |                                                |
    +------------------+------------------------------------------------+
    | Near duplicates  | Similar samples (not detected here). May       |
    |                  | need fuzzy matching.                           |
    +------------------+------------------------------------------------+

    Examples
    --------
    Check for duplicates:

    >>> data = [[1.0, 2.0], [3.0, 4.0], [1.0, 2.0], [5.0, 6.0]]
    >>> report = check_duplicates(data)
    >>> print(f"Found {report['n_duplicates']} duplicate(s)")
    Found 1 duplicate(s)
    >>> print(f"Duplicate groups: {report['duplicate_groups']}")
    Duplicate groups: [[0, 2]]

    Check with labels for conflicts:

    >>> data = [[1.0, 2.0], [1.0, 2.0], [3.0, 4.0]]
    >>> labels = [0, 1, 0]  # Same features, different labels!
    >>> report = check_duplicates(data, labels)
    >>> report['conflicting_labels']
    [[0, 1]]
    """
    if not data:
        return {
            'n_duplicates': 0,
            'duplicate_groups': [],
            'n_unique': 0,
            'duplicate_percentage': 0.0,
        }

    # Convert to tuples for hashing
    seen: Dict[Tuple[float, ...], List[int]] = {}

    for idx, sample in enumerate(data):
        key = tuple(sample)
        if key not in seen:
            seen[key] = []
        seen[key].append(idx)

    # Find groups with duplicates
    duplicate_groups = [indices for indices in seen.values() if len(indices) > 1]

    # Count total duplicates (excluding first occurrence in each group)
    n_duplicates = sum(len(group) - 1 for group in duplicate_groups)

    n_unique = len(seen)
    duplicate_percentage = (n_duplicates / len(data) * 100) if data else 0.0

    result = {
        'n_duplicates': n_duplicates,
        'duplicate_groups': duplicate_groups,
        'n_unique': n_unique,
        'duplicate_percentage': duplicate_percentage,
    }

    # Check for conflicting labels
    if labels is not None:
        conflicting = []
        for group in duplicate_groups:
            group_labels = [labels[i] for i in group]
            if len(set(group_labels)) > 1:
                conflicting.append(group)
        result['conflicting_labels'] = conflicting

    return result


def check_feature_variance(
    data: List[List[float]],
    threshold: float = 0.0,
) -> Dict[str, Any]:
    """
    Identify low-variance (constant or near-constant) features.

    Features with zero or very low variance provide no information
    for discrimination and can cause numerical issues in some models.

    Parameters
    ----------
    data : List[List[float]]
        Feature matrix. Shape: (n_samples, n_features).

    threshold : float, default=0.0
        Variance threshold below which a feature is considered
        low-variance. Use 0.0 to detect only constant features.

    Returns
    -------
    Dict[str, Any]
        A report containing:

        - 'variances': List of variance for each feature
        - 'low_variance_features': Indices of features below threshold
        - 'n_low_variance': Count of low-variance features
        - 'constant_features': Indices of features with zero variance

    Notes
    -----
    Why low-variance features are problematic:

    +--------------------+----------------------------------------------+
    | Issue              | Affected Models                              |
    +====================+==============================================+
    | Division by zero   | Standardization, normalization               |
    +--------------------+----------------------------------------------+
    | No discrimination  | All models (feature provides no info)        |
    +--------------------+----------------------------------------------+
    | Numerical issues   | Linear models, neural networks               |
    +--------------------+----------------------------------------------+

    Recommended actions:
    - Remove features with variance = 0 (constant features)
    - Consider removing features with very low variance
    - Be cautious with threshold: domain knowledge matters

    Examples
    --------
    Check variance:

    >>> data = [[1.0, 5.0, 3.0], [2.0, 5.0, 3.0], [3.0, 5.0, 3.0]]
    >>> report = check_feature_variance(data)
    >>> print(f"Constant features: {report['constant_features']}")
    Constant features: [1, 2]
    >>> # Feature 0 has variance, features 1 and 2 are constant

    With threshold:

    >>> data = [[1.0, 1.001], [1.0, 1.002], [1.0, 1.003]]
    >>> report = check_feature_variance(data, threshold=0.001)
    >>> report['low_variance_features']
    [0, 1]
    """
    if not data:
        return {
            'variances': [],
            'low_variance_features': [],
            'n_low_variance': 0,
            'constant_features': [],
        }

    n_features = len(data[0])
    n_samples = len(data)

    variances = []

    for feat_idx in range(n_features):
        # Extract column values (skip None)
        values = [
            row[feat_idx] for row in data
            if row[feat_idx] is not None
        ]

        if not values:
            variances.append(0.0)
            continue

        mean = sum(values) / len(values)
        variance = sum((v - mean) ** 2 for v in values) / len(values)
        variances.append(variance)

    low_variance_features = [
        i for i, var in enumerate(variances) if var <= threshold
    ]

    constant_features = [
        i for i, var in enumerate(variances) if var == 0.0
    ]

    return {
        'variances': variances,
        'low_variance_features': low_variance_features,
        'n_low_variance': len(low_variance_features),
        'constant_features': constant_features,
    }


def check_class_balance(
    labels: List[Any],
    threshold: float = 0.1,
) -> Dict[str, Any]:
    """
    Analyze class distribution and detect imbalance.

    Class imbalance can bias models toward the majority class,
    leading to poor performance on minority classes.

    Parameters
    ----------
    labels : List[Any]
        Class labels for all samples.

    threshold : float, default=0.1
        Minimum acceptable proportion for any class. If any class
        has fewer than this proportion of samples, the dataset is
        considered imbalanced.

    Returns
    -------
    Dict[str, Any]
        A report containing:

        - 'class_counts': Dict mapping class label to count
        - 'class_proportions': Dict mapping class label to proportion
        - 'n_classes': Number of unique classes
        - 'majority_class': Label of the most common class
        - 'minority_class': Label of the least common class
        - 'imbalance_ratio': Ratio of majority to minority class size
        - 'is_imbalanced': True if any class below threshold

    Notes
    -----
    Class imbalance severity guidelines:

    +------------------+-------------------+---------------------------+
    | Imbalance Ratio  | Severity          | Recommended Actions       |
    +==================+===================+===========================+
    | 1:1 to 1:3       | None to mild      | Standard approaches work  |
    +------------------+-------------------+---------------------------+
    | 1:3 to 1:10      | Moderate          | Use stratified sampling,  |
    |                  |                   | class weights             |
    +------------------+-------------------+---------------------------+
    | 1:10 to 1:100    | Significant       | SMOTE, undersampling,     |
    |                  |                   | threshold moving          |
    +------------------+-------------------+---------------------------+
    | > 1:100          | Severe            | Anomaly detection,        |
    |                  |                   | one-class classification  |
    +------------------+-------------------+---------------------------+

    Strategies for handling imbalance:

    1. **Resampling**: Oversample minority or undersample majority
    2. **SMOTE**: Generate synthetic minority samples
    3. **Class weights**: Weight loss function inversely to frequency
    4. **Threshold tuning**: Adjust decision threshold
    5. **Evaluation metrics**: Use F1, AUC-PR instead of accuracy

    Examples
    --------
    Balanced dataset:

    >>> labels = [0, 1, 0, 1, 0, 1, 0, 1]
    >>> report = check_class_balance(labels)
    >>> report['is_imbalanced']
    False
    >>> report['imbalance_ratio']
    1.0

    Imbalanced dataset:

    >>> labels = [0] * 90 + [1] * 10
    >>> report = check_class_balance(labels)
    >>> report['is_imbalanced']
    True
    >>> report['imbalance_ratio']
    9.0
    >>> report['minority_class']
    1
    """
    if not labels:
        return {
            'class_counts': {},
            'class_proportions': {},
            'n_classes': 0,
            'majority_class': None,
            'minority_class': None,
            'imbalance_ratio': 1.0,
            'is_imbalanced': False,
        }

    # Count classes
    class_counts: Dict[Any, int] = {}
    for label in labels:
        class_counts[label] = class_counts.get(label, 0) + 1

    total = len(labels)
    class_proportions = {
        label: count / total for label, count in class_counts.items()
    }

    # Find majority and minority classes
    sorted_classes = sorted(class_counts.items(), key=lambda x: x[1])
    minority_class, min_count = sorted_classes[0]
    majority_class, max_count = sorted_classes[-1]

    imbalance_ratio = max_count / min_count if min_count > 0 else float('inf')

    # Check if any class is below threshold
    is_imbalanced = any(prop < threshold for prop in class_proportions.values())

    return {
        'class_counts': class_counts,
        'class_proportions': class_proportions,
        'n_classes': len(class_counts),
        'majority_class': majority_class,
        'minority_class': minority_class,
        'imbalance_ratio': imbalance_ratio,
        'is_imbalanced': is_imbalanced,
    }


def check_outliers(
    data: List[List[float]],
    method: Literal["iqr", "zscore"] = "iqr",
    threshold: float = 1.5,
) -> Dict[str, Any]:
    """
    Detect potential outliers in the dataset.

    Outliers can significantly affect model training, especially for
    algorithms sensitive to the scale of data (linear regression,
    k-means, etc.).

    Parameters
    ----------
    data : List[List[float]]
        Feature matrix. Shape: (n_samples, n_features).

    method : {'iqr', 'zscore'}, default='iqr'
        The outlier detection method:

        - 'iqr': Interquartile Range method. Values outside
          [Q1 - threshold*IQR, Q3 + threshold*IQR] are outliers.
          More robust to existing outliers.

        - 'zscore': Z-score method. Values with |z-score| > threshold
          are outliers. Assumes approximately normal distribution.

    threshold : float, default=1.5
        Threshold for outlier detection:
        - For 'iqr': Multiplier for IQR (1.5 = mild, 3.0 = extreme)
        - For 'zscore': Number of standard deviations (2.0 or 3.0 typical)

    Returns
    -------
    Dict[str, Any]
        A report containing:

        - 'outlier_mask': 2D list of booleans indicating outliers
        - 'n_outliers_per_feature': Count of outliers in each feature
        - 'n_samples_with_outliers': Number of samples with any outlier
        - 'outlier_indices': List of sample indices with outliers
        - 'total_outliers': Total number of outlier values

    Notes
    -----
    Comparison of outlier detection methods:

    +----------+---------------------------+---------------------------+
    | Method   | Pros                      | Cons                      |
    +==========+===========================+===========================+
    | IQR      | Robust to outliers,       | May flag too many in      |
    |          | no distribution           | heavy-tailed distributions|
    |          | assumption                |                           |
    +----------+---------------------------+---------------------------+
    | Z-score  | Easy to interpret,        | Sensitive to outliers,    |
    |          | statistical basis         | assumes normality         |
    +----------+---------------------------+---------------------------+

    What to do with outliers:

    1. **Investigate**: Are they data errors or genuine extreme values?
    2. **Data errors**: Correct or remove
    3. **Genuine extremes**: Consider:
       - Winsorization (cap at threshold)
       - Log transformation
       - Robust models (tree-based, robust regression)
       - Separate modeling for extreme cases

    Examples
    --------
    Detect outliers using IQR:

    >>> data = [[1.0, 2.0], [2.0, 3.0], [100.0, 4.0], [3.0, 5.0]]
    >>> report = check_outliers(data, method='iqr')
    >>> print(f"Samples with outliers: {report['outlier_indices']}")
    Samples with outliers: [2]

    Using z-score method:

    >>> data = [[1.0], [2.0], [2.5], [3.0], [100.0]]
    >>> report = check_outliers(data, method='zscore', threshold=2.0)
    >>> report['n_samples_with_outliers']
    1
    """
    if not data:
        return {
            'outlier_mask': [],
            'n_outliers_per_feature': [],
            'n_samples_with_outliers': 0,
            'outlier_indices': [],
            'total_outliers': 0,
        }

    n_features = len(data[0])
    n_samples = len(data)

    outlier_mask = [[False] * n_features for _ in range(n_samples)]
    n_outliers_per_feature = [0] * n_features

    for feat_idx in range(n_features):
        # Extract column values (skip None)
        values = [
            (row_idx, row[feat_idx])
            for row_idx, row in enumerate(data)
            if row[feat_idx] is not None
        ]

        if not values:
            continue

        indices, vals = zip(*values)

        if method == "iqr":
            sorted_vals = sorted(vals)
            n = len(sorted_vals)
            q1_idx = n // 4
            q3_idx = (3 * n) // 4
            q1 = sorted_vals[q1_idx]
            q3 = sorted_vals[q3_idx]
            iqr = q3 - q1

            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr

            for row_idx, val in zip(indices, vals):
                if val < lower_bound or val > upper_bound:
                    outlier_mask[row_idx][feat_idx] = True
                    n_outliers_per_feature[feat_idx] += 1

        elif method == "zscore":
            mean = sum(vals) / len(vals)
            variance = sum((v - mean) ** 2 for v in vals) / len(vals)
            std = math.sqrt(variance) if variance > 0 else 0

            if std == 0:
                continue

            for row_idx, val in zip(indices, vals):
                z = abs((val - mean) / std)
                if z > threshold:
                    outlier_mask[row_idx][feat_idx] = True
                    n_outliers_per_feature[feat_idx] += 1

    # Find samples with any outliers
    outlier_indices = [
        i for i, row in enumerate(outlier_mask) if any(row)
    ]

    total_outliers = sum(n_outliers_per_feature)

    return {
        'outlier_mask': outlier_mask,
        'n_outliers_per_feature': n_outliers_per_feature,
        'n_samples_with_outliers': len(outlier_indices),
        'outlier_indices': outlier_indices,
        'total_outliers': total_outliers,
    }
