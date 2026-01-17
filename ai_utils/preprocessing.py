"""
Data Preprocessing Module
=========================

This module provides utilities for preparing and transforming data
for machine learning models. It includes functions for normalization,
handling missing values, encoding categorical variables, and feature
engineering.

All functions are designed to work with both Python lists and NumPy
arrays where applicable, with automatic type detection and conversion.

Functions
---------
normalize(data, method, feature_range)
    Scale numerical data using various normalization methods.
handle_missing_values(data, strategy, fill_value)
    Handle missing or null values in datasets.
encode_categorical(data, method, categories)
    Convert categorical variables to numerical representations.
create_polynomial_features(data, degree, include_bias)
    Generate polynomial and interaction features.
train_test_split(data, labels, test_size, random_seed, stratify)
    Split data into training and testing sets.

Examples
--------
Basic normalization workflow:

>>> from ai_utils.preprocessing import normalize, handle_missing_values
>>> raw_data = [1.0, 2.0, None, 4.0, 5.0]
>>> clean_data = handle_missing_values(raw_data, strategy='mean')
>>> normalized = normalize(clean_data, method='minmax')

Notes
-----
For large datasets, consider using the batch processing capabilities
or integrating with NumPy for better performance.
"""

from typing import List, Union, Optional, Tuple, Any, Literal
import math
import random


def normalize(
    data: List[float],
    method: Literal["minmax", "zscore", "robust"] = "minmax",
    feature_range: Tuple[float, float] = (0, 1),
) -> List[float]:
    """
    Normalize numerical data using the specified method.

    This function scales numerical features to a standard range, which is
    essential for many machine learning algorithms that are sensitive to
    the scale of input features (e.g., gradient descent-based methods,
    distance-based algorithms like KNN).

    Parameters
    ----------
    data : List[float]
        A list of numerical values to normalize. Must contain at least
        two elements for meaningful normalization. NaN values are not
        supported; use `handle_missing_values()` first.

    method : {'minmax', 'zscore', 'robust'}, default='minmax'
        The normalization method to apply:

        - 'minmax': Scales data to [feature_range[0], feature_range[1]].
          Formula: (x - min) / (max - min) * (range_max - range_min) + range_min
          Best for: Data with known bounds, neural networks.

        - 'zscore': Standardizes to zero mean and unit variance.
          Formula: (x - mean) / std
          Best for: Data following Gaussian distribution, linear models.

        - 'robust': Uses median and IQR, resistant to outliers.
          Formula: (x - median) / IQR
          Best for: Data with significant outliers.

    feature_range : Tuple[float, float], default=(0, 1)
        The target range for minmax normalization. Only used when
        method='minmax'. The first value must be less than the second.

    Returns
    -------
    List[float]
        A new list containing the normalized values. The original data
        is not modified.

    Raises
    ------
    ValueError
        If data is empty, contains non-numeric values, or if
        feature_range[0] >= feature_range[1].
    ZeroDivisionError
        If all values in data are identical (zero variance/range).

    See Also
    --------
    handle_missing_values : Clean data before normalization.
    create_polynomial_features : Generate features after normalization.

    Notes
    -----
    - For minmax: Results are bounded within feature_range.
    - For zscore: Results are unbounded; mean=0, std=1.
    - For robust: Results are unbounded; median=0.

    The choice of method depends on your data distribution and model:

    +----------+------------------+-------------------------+
    | Method   | Pros             | Cons                    |
    +==========+==================+=========================+
    | minmax   | Bounded output   | Sensitive to outliers   |
    +----------+------------------+-------------------------+
    | zscore   | Handles outliers | Unbounded output        |
    |          | better           |                         |
    +----------+------------------+-------------------------+
    | robust   | Best for outliers| May not work well with  |
    |          |                  | small datasets          |
    +----------+------------------+-------------------------+

    Examples
    --------
    Basic min-max normalization:

    >>> data = [10.0, 20.0, 30.0, 40.0, 50.0]
    >>> normalize(data, method='minmax')
    [0.0, 0.25, 0.5, 0.75, 1.0]

    Custom range for min-max:

    >>> normalize(data, method='minmax', feature_range=(-1, 1))
    [-1.0, -0.5, 0.0, 0.5, 1.0]

    Z-score standardization:

    >>> result = normalize(data, method='zscore')
    >>> # Mean will be approximately 0, std approximately 1
    >>> abs(sum(result) / len(result)) < 1e-10
    True

    Robust scaling with outliers:

    >>> data_with_outliers = [10.0, 20.0, 30.0, 40.0, 1000.0]
    >>> robust_result = normalize(data_with_outliers, method='robust')
    >>> # Outlier has less impact on other values
    """
    if not data:
        raise ValueError("Input data cannot be empty")

    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numeric")

    if method == "minmax":
        if feature_range[0] >= feature_range[1]:
            raise ValueError(
                f"feature_range[0] ({feature_range[0]}) must be less than "
                f"feature_range[1] ({feature_range[1]})"
            )

        min_val = min(data)
        max_val = max(data)
        range_diff = max_val - min_val

        if range_diff == 0:
            raise ZeroDivisionError(
                "Cannot normalize: all values are identical"
            )

        scale = feature_range[1] - feature_range[0]
        return [
            ((x - min_val) / range_diff) * scale + feature_range[0]
            for x in data
        ]

    elif method == "zscore":
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std = math.sqrt(variance)

        if std == 0:
            raise ZeroDivisionError(
                "Cannot normalize: standard deviation is zero"
            )

        return [(x - mean) / std for x in data]

    elif method == "robust":
        sorted_data = sorted(data)
        n = len(sorted_data)

        # Calculate median
        if n % 2 == 0:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            median = sorted_data[n // 2]

        # Calculate IQR (Interquartile Range)
        q1_idx = n // 4
        q3_idx = (3 * n) // 4
        q1 = sorted_data[q1_idx]
        q3 = sorted_data[q3_idx]
        iqr = q3 - q1

        if iqr == 0:
            raise ZeroDivisionError(
                "Cannot normalize: IQR is zero"
            )

        return [(x - median) / iqr for x in data]

    else:
        raise ValueError(
            f"Unknown method '{method}'. "
            f"Supported methods: 'minmax', 'zscore', 'robust'"
        )


def handle_missing_values(
    data: List[Optional[float]],
    strategy: Literal["mean", "median", "mode", "constant", "drop"] = "mean",
    fill_value: Optional[float] = None,
) -> List[float]:
    """
    Handle missing (None/NaN) values in a dataset.

    Missing data is a common problem in real-world datasets. This function
    provides several strategies for handling missing values, each with
    different trade-offs.

    Parameters
    ----------
    data : List[Optional[float]]
        A list that may contain None values representing missing data.
        Numeric values (int, float) are preserved.

    strategy : {'mean', 'median', 'mode', 'constant', 'drop'}, default='mean'
        The strategy for handling missing values:

        - 'mean': Replace with the arithmetic mean of non-missing values.
          Best for: Normally distributed data without outliers.

        - 'median': Replace with the median of non-missing values.
          Best for: Skewed data or data with outliers.

        - 'mode': Replace with the most frequent value.
          Best for: Categorical-like numeric data with clear modes.

        - 'constant': Replace with a specified fill_value.
          Best for: Domain-specific default values (e.g., 0 for counts).

        - 'drop': Remove all missing values from the result.
          Best for: When missing data is sparse and removal is acceptable.

    fill_value : float, optional
        The value to use when strategy='constant'. Required if strategy
        is 'constant', ignored otherwise.

    Returns
    -------
    List[float]
        A new list with missing values handled according to the strategy.
        The original data is not modified.

    Raises
    ------
    ValueError
        If strategy is 'constant' but fill_value is not provided.
        If all values are missing (nothing to compute mean/median/mode).
        If strategy is not recognized.

    Warnings
    --------
    Using 'mean' or 'median' imputation can reduce variance in your
    dataset and may introduce bias. Consider the implications for your
    specific use case.

    See Also
    --------
    normalize : Normalize data after handling missing values.

    Notes
    -----
    The choice of strategy can significantly impact model performance:

    +----------+-----------------------------+---------------------------+
    | Strategy | When to Use                 | Drawbacks                 |
    +==========+=============================+===========================+
    | mean     | Normal distribution,        | Sensitive to outliers,    |
    |          | few missing values          | reduces variance          |
    +----------+-----------------------------+---------------------------+
    | median   | Skewed data, outliers       | May not preserve          |
    |          | present                     | distribution shape        |
    +----------+-----------------------------+---------------------------+
    | mode     | Categorical-like data       | May introduce bias if     |
    |          |                             | mode is not representative|
    +----------+-----------------------------+---------------------------+
    | constant | Known default value         | Requires domain knowledge |
    +----------+-----------------------------+---------------------------+
    | drop     | Sparse missing data,        | Loses information,        |
    |          | MCAR assumption valid       | changes sample size       |
    +----------+-----------------------------+---------------------------+

    MCAR = Missing Completely At Random

    Examples
    --------
    Mean imputation:

    >>> data = [1.0, 2.0, None, 4.0, 5.0]
    >>> handle_missing_values(data, strategy='mean')
    [1.0, 2.0, 3.0, 4.0, 5.0]

    Median imputation (better for outliers):

    >>> data = [1.0, 2.0, None, 4.0, 100.0]
    >>> handle_missing_values(data, strategy='median')
    [1.0, 2.0, 3.0, 4.0, 100.0]

    Constant fill value:

    >>> data = [1.0, None, 3.0, None]
    >>> handle_missing_values(data, strategy='constant', fill_value=0.0)
    [1.0, 0.0, 3.0, 0.0]

    Drop missing values:

    >>> data = [1.0, None, 3.0, None, 5.0]
    >>> handle_missing_values(data, strategy='drop')
    [1.0, 3.0, 5.0]
    """
    # Separate valid and missing values
    valid_values = [x for x in data if x is not None]

    if not valid_values and strategy != "drop":
        raise ValueError(
            "Cannot compute fill value: all values are missing"
        )

    if strategy == "mean":
        fill = sum(valid_values) / len(valid_values)
        return [x if x is not None else fill for x in data]

    elif strategy == "median":
        sorted_valid = sorted(valid_values)
        n = len(sorted_valid)
        if n % 2 == 0:
            fill = (sorted_valid[n // 2 - 1] + sorted_valid[n // 2]) / 2
        else:
            fill = sorted_valid[n // 2]
        return [x if x is not None else fill for x in data]

    elif strategy == "mode":
        # Count occurrences
        counts: dict[float, int] = {}
        for v in valid_values:
            counts[v] = counts.get(v, 0) + 1
        fill = max(counts, key=lambda k: counts[k])
        return [x if x is not None else fill for x in data]

    elif strategy == "constant":
        if fill_value is None:
            raise ValueError(
                "fill_value must be provided when strategy='constant'"
            )
        return [x if x is not None else fill_value for x in data]

    elif strategy == "drop":
        return valid_values

    else:
        raise ValueError(
            f"Unknown strategy '{strategy}'. "
            f"Supported: 'mean', 'median', 'mode', 'constant', 'drop'"
        )


def encode_categorical(
    data: List[str],
    method: Literal["onehot", "label", "ordinal"] = "label",
    categories: Optional[List[str]] = None,
) -> Union[List[int], List[List[int]]]:
    """
    Encode categorical string variables as numerical values.

    Machine learning models typically require numerical input. This function
    converts categorical (string) data into numerical representations using
    various encoding schemes.

    Parameters
    ----------
    data : List[str]
        A list of categorical string values to encode.

    method : {'onehot', 'label', 'ordinal'}, default='label'
        The encoding method to use:

        - 'label': Assigns a unique integer to each category.
          Result: [0, 1, 2, ...] for each unique category.
          Best for: Tree-based models, ordinal-like categories.

        - 'onehot': Creates binary columns for each category.
          Result: [[1,0,0], [0,1,0], ...] for each sample.
          Best for: Linear models, neural networks, nominal categories.

        - 'ordinal': Uses provided categories list for ordering.
          Result: Integer based on position in categories list.
          Best for: Categories with meaningful order (e.g., low/med/high).

    categories : List[str], optional
        For 'ordinal' encoding, specifies the order of categories from
        lowest to highest. Required if method='ordinal'. For other methods,
        this parameter is ignored.

    Returns
    -------
    Union[List[int], List[List[int]]]
        - For 'label' and 'ordinal': List of integers.
        - For 'onehot': List of binary lists (one-hot vectors).

    Raises
    ------
    ValueError
        If method is 'ordinal' but categories is not provided.
        If data contains values not in the categories list (ordinal).
        If method is not recognized.

    See Also
    --------
    normalize : Normalize encoded values if needed.

    Notes
    -----
    Encoding choice affects model interpretation and performance:

    +----------+------------------+-------------------------+---------------+
    | Method   | Output Shape     | Pros                    | Cons          |
    +==========+==================+=========================+===============+
    | label    | (n,)             | Compact, simple         | Implies false |
    |          |                  |                         | ordering      |
    +----------+------------------+-------------------------+---------------+
    | onehot   | (n, k)           | No ordering implied,    | High dim for  |
    |          | k = # categories | works with linear       | many cats     |
    |          |                  | models                  |               |
    +----------+------------------+-------------------------+---------------+
    | ordinal  | (n,)             | Preserves meaningful    | Requires      |
    |          |                  | order                   | domain        |
    |          |                  |                         | knowledge     |
    +----------+------------------+-------------------------+---------------+

    Examples
    --------
    Label encoding:

    >>> colors = ['red', 'blue', 'green', 'red', 'blue']
    >>> encode_categorical(colors, method='label')
    [0, 1, 2, 0, 1]

    One-hot encoding:

    >>> colors = ['red', 'blue', 'green']
    >>> encode_categorical(colors, method='onehot')
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    Ordinal encoding with explicit order:

    >>> sizes = ['medium', 'small', 'large', 'small']
    >>> categories = ['small', 'medium', 'large']
    >>> encode_categorical(sizes, method='ordinal', categories=categories)
    [1, 0, 2, 0]
    """
    if not data:
        return []

    if method == "label":
        unique_cats = list(dict.fromkeys(data))  # Preserve order
        cat_to_int = {cat: i for i, cat in enumerate(unique_cats)}
        return [cat_to_int[x] for x in data]

    elif method == "onehot":
        unique_cats = list(dict.fromkeys(data))
        cat_to_idx = {cat: i for i, cat in enumerate(unique_cats)}
        n_categories = len(unique_cats)

        result = []
        for x in data:
            one_hot = [0] * n_categories
            one_hot[cat_to_idx[x]] = 1
            result.append(one_hot)
        return result

    elif method == "ordinal":
        if categories is None:
            raise ValueError(
                "categories must be provided for ordinal encoding"
            )

        cat_to_int = {cat: i for i, cat in enumerate(categories)}

        result = []
        for x in data:
            if x not in cat_to_int:
                raise ValueError(
                    f"Value '{x}' not found in categories: {categories}"
                )
            result.append(cat_to_int[x])
        return result

    else:
        raise ValueError(
            f"Unknown method '{method}'. "
            f"Supported: 'label', 'onehot', 'ordinal'"
        )


def create_polynomial_features(
    data: List[List[float]],
    degree: int = 2,
    include_bias: bool = False,
) -> List[List[float]]:
    """
    Generate polynomial and interaction features from input features.

    Polynomial features can help linear models capture non-linear
    relationships. This function generates all polynomial combinations
    of features up to the specified degree.

    Parameters
    ----------
    data : List[List[float]]
        A 2D list where each inner list represents a sample and contains
        the feature values. Shape: (n_samples, n_features).

    degree : int, default=2
        The maximum degree of polynomial features. Must be >= 1.
        - degree=1: Returns original features only (plus bias if enabled)
        - degree=2: Includes squares and pairwise products
        - degree=3: Includes cubes and all 3-way products, etc.

    include_bias : bool, default=False
        If True, includes a bias column (all 1s) as the first feature.
        This is equivalent to adding an intercept term.

    Returns
    -------
    List[List[float]]
        A 2D list with polynomial features. The number of output features
        depends on the input features (n) and degree (d):
        - Without bias: C(n+d, d) - 1 features
        - With bias: C(n+d, d) features
        Where C(a,b) is "a choose b".

    Raises
    ------
    ValueError
        If degree < 1 or if data is empty or malformed.

    Warnings
    --------
    High degrees can lead to:
    - Exponential growth in feature count
    - Overfitting
    - Numerical instability

    Consider using regularization (L1/L2) when using polynomial features.

    See Also
    --------
    normalize : Normalize features after polynomial expansion.

    Notes
    -----
    For 2 features [a, b] and degree=2, the output features are:
    [a, b, a^2, a*b, b^2] (without bias)
    [1, a, b, a^2, a*b, b^2] (with bias)

    Feature count growth:

    +------+------------+---------------------+
    | d    | n=2        | n=5                 |
    +======+============+=====================+
    | 2    | 5 features | 20 features         |
    +------+------------+---------------------+
    | 3    | 9 features | 55 features         |
    +------+------------+---------------------+
    | 4    | 14 features| 125 features        |
    +------+------------+---------------------+

    Examples
    --------
    Basic polynomial expansion:

    >>> data = [[2.0, 3.0]]
    >>> create_polynomial_features(data, degree=2)
    [[2.0, 3.0, 4.0, 6.0, 9.0]]
    # Features: [a, b, a^2, a*b, b^2]

    With bias term:

    >>> create_polynomial_features(data, degree=2, include_bias=True)
    [[1.0, 2.0, 3.0, 4.0, 6.0, 9.0]]
    # Features: [1, a, b, a^2, a*b, b^2]

    Single feature:

    >>> data = [[2.0], [3.0], [4.0]]
    >>> create_polynomial_features(data, degree=3)
    [[2.0, 4.0, 8.0], [3.0, 9.0, 27.0], [4.0, 16.0, 64.0]]
    # Features: [x, x^2, x^3]
    """
    if degree < 1:
        raise ValueError(f"degree must be >= 1, got {degree}")

    if not data:
        raise ValueError("Input data cannot be empty")

    if not all(isinstance(row, list) for row in data):
        raise ValueError("Input must be a 2D list")

    n_features = len(data[0])

    if not all(len(row) == n_features for row in data):
        raise ValueError("All samples must have the same number of features")

    def generate_powers(n_features: int, degree: int) -> List[Tuple[int, ...]]:
        """Generate all power combinations up to degree."""
        if n_features == 0:
            return [()]

        powers = []
        for total_degree in range(1, degree + 1):
            powers.extend(_power_combinations(n_features, total_degree))
        return powers

    def _power_combinations(
        n: int, target_sum: int, current: Tuple[int, ...] = ()
    ) -> List[Tuple[int, ...]]:
        """Recursively generate power combinations summing to target."""
        if len(current) == n:
            if sum(current) == target_sum:
                return [current]
            return []

        results = []
        remaining = n - len(current)
        max_val = target_sum - sum(current)

        for val in range(max_val + 1):
            results.extend(
                _power_combinations(n, target_sum, current + (val,))
            )
        return results

    # Generate all power combinations
    all_powers = generate_powers(n_features, degree)

    # Sort by total degree, then by individual powers
    all_powers.sort(key=lambda p: (sum(p), p))

    result = []
    for sample in data:
        new_features = []

        if include_bias:
            new_features.append(1.0)

        for powers in all_powers:
            feature_val = 1.0
            for feat_idx, power in enumerate(powers):
                feature_val *= sample[feat_idx] ** power
            new_features.append(feature_val)

        result.append(new_features)

    return result


def train_test_split(
    data: List[List[float]],
    labels: List[Any],
    test_size: float = 0.2,
    random_seed: Optional[int] = None,
    stratify: bool = False,
) -> Tuple[List[List[float]], List[List[float]], List[Any], List[Any]]:
    """
    Split data and labels into training and testing sets.

    This function randomly partitions the dataset into two subsets for
    model training and evaluation, ensuring no data leakage between sets.

    Parameters
    ----------
    data : List[List[float]]
        A 2D list of feature vectors. Shape: (n_samples, n_features).
        Each inner list represents one sample.

    labels : List[Any]
        A list of labels/targets corresponding to each sample in data.
        Must have the same length as data.

    test_size : float, default=0.2
        The proportion of data to use for testing. Must be between 0 and 1
        (exclusive). Common values: 0.2 (80/20 split), 0.25 (75/25 split).

    random_seed : int, optional
        Seed for the random number generator to ensure reproducibility.
        If None, results will vary between runs.

    stratify : bool, default=False
        If True, preserves the proportion of each class in both train
        and test sets. Recommended for imbalanced classification problems.

    Returns
    -------
    Tuple[List[List[float]], List[List[float]], List[Any], List[Any]]
        A tuple of four elements:
        - X_train: Training feature vectors
        - X_test: Testing feature vectors
        - y_train: Training labels
        - y_test: Testing labels

    Raises
    ------
    ValueError
        If test_size is not between 0 and 1.
        If data and labels have different lengths.
        If stratify=True and a class has fewer than 2 samples.

    Notes
    -----
    The split is performed randomly. For reproducible results, always
    set a random_seed.

    Stratification ensures that rare classes are represented in both
    sets. Without stratification, rare classes might end up entirely
    in one set.

    +------------+----------------+-------------------------------+
    | test_size  | Train samples  | Test samples                  |
    +============+================+===============================+
    | 0.2        | 80%            | 20%                           |
    +------------+----------------+-------------------------------+
    | 0.25       | 75%            | 25%                           |
    +------------+----------------+-------------------------------+
    | 0.3        | 70%            | 30%                           |
    +------------+----------------+-------------------------------+

    Examples
    --------
    Basic 80/20 split:

    >>> data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    >>> labels = [0, 1, 0, 1, 0]
    >>> X_train, X_test, y_train, y_test = train_test_split(
    ...     data, labels, test_size=0.2, random_seed=42
    ... )
    >>> len(X_train), len(X_test)
    (4, 1)

    Reproducible split with seed:

    >>> X_train1, _, _, _ = train_test_split(data, labels, random_seed=42)
    >>> X_train2, _, _, _ = train_test_split(data, labels, random_seed=42)
    >>> X_train1 == X_train2
    True

    Stratified split for imbalanced data:

    >>> data = [[i] for i in range(100)]
    >>> labels = [0] * 90 + [1] * 10  # 90% class 0, 10% class 1
    >>> _, _, y_train, y_test = train_test_split(
    ...     data, labels, test_size=0.2, stratify=True, random_seed=42
    ... )
    >>> # Both sets maintain ~90/10 class ratio
    """
    if not 0 < test_size < 1:
        raise ValueError(
            f"test_size must be between 0 and 1, got {test_size}"
        )

    if len(data) != len(labels):
        raise ValueError(
            f"data and labels must have same length: "
            f"{len(data)} vs {len(labels)}"
        )

    n_samples = len(data)
    n_test = max(1, int(n_samples * test_size))

    if random_seed is not None:
        random.seed(random_seed)

    indices = list(range(n_samples))

    if stratify:
        # Group indices by label
        label_indices: dict[Any, List[int]] = {}
        for idx, label in enumerate(labels):
            if label not in label_indices:
                label_indices[label] = []
            label_indices[label].append(idx)

        # Check minimum samples per class
        for label, idxs in label_indices.items():
            if len(idxs) < 2:
                raise ValueError(
                    f"Class '{label}' has only {len(idxs)} sample(s). "
                    f"Stratified split requires at least 2 samples per class."
                )

        # Sample proportionally from each class
        test_indices = []
        train_indices = []

        for label, idxs in label_indices.items():
            random.shuffle(idxs)
            n_class_test = max(1, int(len(idxs) * test_size))
            test_indices.extend(idxs[:n_class_test])
            train_indices.extend(idxs[n_class_test:])

    else:
        random.shuffle(indices)
        test_indices = indices[:n_test]
        train_indices = indices[n_test:]

    X_train = [data[i] for i in train_indices]
    X_test = [data[i] for i in test_indices]
    y_train = [labels[i] for i in train_indices]
    y_test = [labels[i] for i in test_indices]

    return X_train, X_test, y_train, y_test
