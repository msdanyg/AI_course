"""
Model Evaluation Module
=======================

This module provides metrics and utilities for evaluating machine learning
model performance. It includes functions for classification metrics,
regression metrics, and cross-validation utilities.

All functions are designed to work with Python lists and return easily
interpretable results. For production use with large datasets, consider
using NumPy-based implementations.

Functions
---------
calculate_metrics(y_true, y_pred, task_type)
    Calculate comprehensive metrics for classification or regression.
accuracy_score(y_true, y_pred)
    Calculate classification accuracy.
precision_recall_f1(y_true, y_pred, average)
    Calculate precision, recall, and F1 score.
confusion_matrix(y_true, y_pred, labels)
    Generate a confusion matrix for classification results.
mean_squared_error(y_true, y_pred, squared)
    Calculate MSE or RMSE for regression.
r2_score(y_true, y_pred)
    Calculate R-squared (coefficient of determination).
cross_validate(model_fn, data, labels, k_folds, metric)
    Perform k-fold cross-validation.

Examples
--------
Classification evaluation:

>>> y_true = [0, 1, 1, 0, 1, 0]
>>> y_pred = [0, 1, 0, 0, 1, 1]
>>> metrics = calculate_metrics(y_true, y_pred, task_type='classification')
>>> print(f"Accuracy: {metrics['accuracy']:.2f}")
Accuracy: 0.67

Regression evaluation:

>>> y_true = [3.0, -0.5, 2.0, 7.0]
>>> y_pred = [2.5, 0.0, 2.0, 8.0]
>>> metrics = calculate_metrics(y_true, y_pred, task_type='regression')
>>> print(f"RMSE: {metrics['rmse']:.2f}")
RMSE: 0.61
"""

from typing import List, Dict, Any, Union, Optional, Callable, Tuple, Literal
import math


def calculate_metrics(
    y_true: List[Any],
    y_pred: List[Any],
    task_type: Literal["classification", "regression"] = "classification",
) -> Dict[str, float]:
    """
    Calculate comprehensive evaluation metrics for model predictions.

    This is a convenience function that computes all relevant metrics
    based on the task type, returning them in a single dictionary.

    Parameters
    ----------
    y_true : List[Any]
        Ground truth (correct) labels or values. For classification,
        these are class labels. For regression, these are continuous values.

    y_pred : List[Any]
        Predicted labels or values from the model. Must have the same
        length as y_true.

    task_type : {'classification', 'regression'}, default='classification'
        The type of machine learning task:

        - 'classification': Computes accuracy, precision, recall, F1.
        - 'regression': Computes MSE, RMSE, MAE, R².

    Returns
    -------
    Dict[str, float]
        A dictionary containing computed metrics:

        For classification:
            - 'accuracy': Overall accuracy (correct / total)
            - 'precision': Weighted precision across classes
            - 'recall': Weighted recall across classes
            - 'f1': Weighted F1 score

        For regression:
            - 'mse': Mean Squared Error
            - 'rmse': Root Mean Squared Error
            - 'mae': Mean Absolute Error
            - 'r2': R-squared (coefficient of determination)

    Raises
    ------
    ValueError
        If y_true and y_pred have different lengths.
        If task_type is not recognized.

    See Also
    --------
    accuracy_score : Calculate accuracy only.
    precision_recall_f1 : Calculate P/R/F1 with averaging options.
    confusion_matrix : Get detailed classification breakdown.
    mean_squared_error : Calculate MSE/RMSE with options.
    r2_score : Calculate R² only.

    Notes
    -----
    Metric interpretation guide:

    **Classification metrics (all range 0-1, higher is better):**

    +-------------+---------------------------------------------------+
    | Metric      | Interpretation                                    |
    +=============+===================================================+
    | Accuracy    | % of correct predictions. Can be misleading with  |
    |             | imbalanced classes.                               |
    +-------------+---------------------------------------------------+
    | Precision   | Of predicted positives, how many were correct?    |
    |             | High when false positives are costly.             |
    +-------------+---------------------------------------------------+
    | Recall      | Of actual positives, how many were found?         |
    |             | High when false negatives are costly.             |
    +-------------+---------------------------------------------------+
    | F1          | Harmonic mean of precision and recall.            |
    |             | Balanced metric when both matter.                 |
    +-------------+---------------------------------------------------+

    **Regression metrics:**

    +-------------+---------------------------------------------------+
    | Metric      | Interpretation                                    |
    +=============+===================================================+
    | MSE         | Average squared error. Penalizes large errors.    |
    |             | Lower is better. Same units as target².           |
    +-------------+---------------------------------------------------+
    | RMSE        | Square root of MSE. Same units as target.         |
    |             | Lower is better. More interpretable than MSE.     |
    +-------------+---------------------------------------------------+
    | MAE         | Average absolute error. Robust to outliers.       |
    |             | Lower is better. Same units as target.            |
    +-------------+---------------------------------------------------+
    | R²          | Proportion of variance explained. Ranges -∞ to 1. |
    |             | 1 = perfect fit, 0 = mean baseline, <0 = worse.   |
    +-------------+---------------------------------------------------+

    Examples
    --------
    Binary classification:

    >>> y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    >>> y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
    >>> metrics = calculate_metrics(y_true, y_pred, 'classification')
    >>> print(f"Accuracy: {metrics['accuracy']:.2%}")
    Accuracy: 75.00%
    >>> print(f"F1 Score: {metrics['f1']:.3f}")
    F1 Score: 0.750

    Multi-class classification:

    >>> y_true = ['cat', 'dog', 'bird', 'cat', 'dog']
    >>> y_pred = ['cat', 'dog', 'cat', 'cat', 'bird']
    >>> metrics = calculate_metrics(y_true, y_pred, 'classification')

    Regression:

    >>> y_true = [100, 150, 200, 250, 300]
    >>> y_pred = [110, 140, 210, 240, 295]
    >>> metrics = calculate_metrics(y_true, y_pred, 'regression')
    >>> print(f"RMSE: ${metrics['rmse']:.2f}")
    RMSE: $8.37
    >>> print(f"R²: {metrics['r2']:.3f}")
    R²: 0.986
    """
    if len(y_true) != len(y_pred):
        raise ValueError(
            f"y_true and y_pred must have same length: "
            f"{len(y_true)} vs {len(y_pred)}"
        )

    if task_type == "classification":
        acc = accuracy_score(y_true, y_pred)
        prec, rec, f1 = precision_recall_f1(y_true, y_pred, average="weighted")

        return {
            "accuracy": acc,
            "precision": prec,
            "recall": rec,
            "f1": f1,
        }

    elif task_type == "regression":
        mse = mean_squared_error(y_true, y_pred, squared=True)
        rmse = mean_squared_error(y_true, y_pred, squared=False)
        mae = _mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)

        return {
            "mse": mse,
            "rmse": rmse,
            "mae": mae,
            "r2": r2,
        }

    else:
        raise ValueError(
            f"Unknown task_type '{task_type}'. "
            f"Supported: 'classification', 'regression'"
        )


def accuracy_score(y_true: List[Any], y_pred: List[Any]) -> float:
    """
    Calculate the accuracy of classification predictions.

    Accuracy is the fraction of predictions that exactly match the
    ground truth labels. It is the simplest classification metric
    but can be misleading with imbalanced classes.

    Parameters
    ----------
    y_true : List[Any]
        Ground truth class labels.

    y_pred : List[Any]
        Predicted class labels. Must have the same length as y_true.

    Returns
    -------
    float
        Accuracy score between 0.0 and 1.0, where 1.0 indicates perfect
        prediction accuracy.

    Raises
    ------
    ValueError
        If y_true and y_pred have different lengths.
        If inputs are empty.

    Warnings
    --------
    Accuracy can be misleading for imbalanced datasets. For example,
    with 95% negative samples, always predicting "negative" achieves
    95% accuracy but is useless. Consider F1 score or balanced accuracy
    for imbalanced problems.

    See Also
    --------
    precision_recall_f1 : Better metrics for imbalanced data.
    confusion_matrix : Detailed breakdown of predictions.

    Notes
    -----
    Formula: accuracy = (TP + TN) / (TP + TN + FP + FN)

    Or simply: accuracy = correct_predictions / total_predictions

    Examples
    --------
    Perfect predictions:

    >>> y_true = [0, 1, 2, 0, 1, 2]
    >>> y_pred = [0, 1, 2, 0, 1, 2]
    >>> accuracy_score(y_true, y_pred)
    1.0

    Some errors:

    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 0, 1, 0]
    >>> accuracy_score(y_true, y_pred)
    0.75

    String labels work too:

    >>> y_true = ['spam', 'ham', 'spam', 'ham']
    >>> y_pred = ['spam', 'spam', 'spam', 'ham']
    >>> accuracy_score(y_true, y_pred)
    0.75
    """
    if len(y_true) != len(y_pred):
        raise ValueError(
            f"y_true and y_pred must have same length: "
            f"{len(y_true)} vs {len(y_pred)}"
        )

    if not y_true:
        raise ValueError("Inputs cannot be empty")

    correct = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
    return correct / len(y_true)


def precision_recall_f1(
    y_true: List[Any],
    y_pred: List[Any],
    average: Literal["binary", "macro", "weighted"] = "binary",
    pos_label: Any = 1,
) -> Tuple[float, float, float]:
    """
    Calculate precision, recall, and F1 score for classification.

    These metrics provide a more nuanced view of classifier performance
    than accuracy alone, especially for imbalanced datasets.

    Parameters
    ----------
    y_true : List[Any]
        Ground truth class labels.

    y_pred : List[Any]
        Predicted class labels.

    average : {'binary', 'macro', 'weighted'}, default='binary'
        The averaging strategy for multi-class classification:

        - 'binary': Calculate metrics for the positive class only.
          Only valid for binary classification with pos_label specified.

        - 'macro': Calculate metrics for each class and average them.
          Treats all classes equally regardless of support.

        - 'weighted': Calculate metrics for each class and compute
          weighted average by class support (number of samples).

    pos_label : Any, default=1
        The class to consider as "positive" for binary averaging.
        Ignored for macro and weighted averaging.

    Returns
    -------
    Tuple[float, float, float]
        A tuple of (precision, recall, f1_score):

        - precision: TP / (TP + FP). What fraction of positive
          predictions were correct?
        - recall: TP / (TP + FN). What fraction of actual positives
          were correctly identified?
        - f1_score: 2 * (precision * recall) / (precision + recall).
          Harmonic mean of precision and recall.

    Raises
    ------
    ValueError
        If inputs have different lengths or are empty.
        If average='binary' but there are more than 2 classes.

    See Also
    --------
    accuracy_score : Overall accuracy (simpler metric).
    confusion_matrix : Full breakdown of predictions.

    Notes
    -----
    Understanding precision and recall:

    +-------------+---------------------------------------------+
    | Metric      | Focus                                       |
    +=============+=============================================+
    | Precision   | Minimize false positives                    |
    |             | "Of things I called positive, how many      |
    |             | were actually positive?"                    |
    +-------------+---------------------------------------------+
    | Recall      | Minimize false negatives                    |
    |             | "Of all actual positives, how many did I    |
    |             | find?"                                      |
    +-------------+---------------------------------------------+
    | F1          | Balance precision and recall                |
    |             | Useful when both matter equally             |
    +-------------+---------------------------------------------+

    When to prioritize each metric:

    - **High precision needed**: Spam filtering (don't mark good email
      as spam), medical screening confirmatory tests.
    - **High recall needed**: Disease screening (don't miss cases),
      fraud detection (don't miss fraud).
    - **F1 balanced**: When false positives and false negatives have
      similar costs.

    Examples
    --------
    Binary classification:

    >>> y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    >>> y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
    >>> prec, rec, f1 = precision_recall_f1(y_true, y_pred, average='binary')
    >>> print(f"Precision: {prec:.2f}, Recall: {rec:.2f}, F1: {f1:.2f}")
    Precision: 0.75, Recall: 0.75, F1: 0.75

    Multi-class with macro averaging:

    >>> y_true = ['cat', 'dog', 'bird', 'cat', 'dog', 'cat']
    >>> y_pred = ['cat', 'dog', 'cat', 'cat', 'bird', 'dog']
    >>> prec, rec, f1 = precision_recall_f1(y_true, y_pred, average='macro')

    Weighted average for imbalanced classes:

    >>> y_true = [0, 0, 0, 0, 0, 1]  # Imbalanced: 5 zeros, 1 one
    >>> y_pred = [0, 0, 0, 0, 1, 1]
    >>> prec, rec, f1 = precision_recall_f1(y_true, y_pred, average='weighted')
    """
    if len(y_true) != len(y_pred):
        raise ValueError(
            f"y_true and y_pred must have same length: "
            f"{len(y_true)} vs {len(y_pred)}"
        )

    if not y_true:
        raise ValueError("Inputs cannot be empty")

    # Get unique labels
    labels = list(set(y_true) | set(y_pred))

    if average == "binary":
        if len(labels) > 2:
            raise ValueError(
                f"average='binary' requires binary classification, "
                f"but found {len(labels)} classes: {labels}"
            )

        # Calculate for positive class
        tp = sum(1 for yt, yp in zip(y_true, y_pred)
                 if yt == pos_label and yp == pos_label)
        fp = sum(1 for yt, yp in zip(y_true, y_pred)
                 if yt != pos_label and yp == pos_label)
        fn = sum(1 for yt, yp in zip(y_true, y_pred)
                 if yt == pos_label and yp != pos_label)

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * precision * recall / (precision + recall)
              if (precision + recall) > 0 else 0.0)

        return precision, recall, f1

    else:  # macro or weighted
        precisions = []
        recalls = []
        f1s = []
        supports = []

        for label in labels:
            tp = sum(1 for yt, yp in zip(y_true, y_pred)
                     if yt == label and yp == label)
            fp = sum(1 for yt, yp in zip(y_true, y_pred)
                     if yt != label and yp == label)
            fn = sum(1 for yt, yp in zip(y_true, y_pred)
                     if yt == label and yp != label)

            prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1_val = (2 * prec * rec / (prec + rec)
                      if (prec + rec) > 0 else 0.0)

            precisions.append(prec)
            recalls.append(rec)
            f1s.append(f1_val)
            supports.append(sum(1 for yt in y_true if yt == label))

        if average == "macro":
            return (
                sum(precisions) / len(precisions),
                sum(recalls) / len(recalls),
                sum(f1s) / len(f1s),
            )
        else:  # weighted
            total_support = sum(supports)
            return (
                sum(p * s for p, s in zip(precisions, supports)) / total_support,
                sum(r * s for r, s in zip(recalls, supports)) / total_support,
                sum(f * s for f, s in zip(f1s, supports)) / total_support,
            )


def confusion_matrix(
    y_true: List[Any],
    y_pred: List[Any],
    labels: Optional[List[Any]] = None,
) -> Tuple[List[List[int]], List[Any]]:
    """
    Compute a confusion matrix for classification results.

    A confusion matrix shows the counts of actual vs predicted labels,
    helping visualize where a classifier makes errors.

    Parameters
    ----------
    y_true : List[Any]
        Ground truth class labels.

    y_pred : List[Any]
        Predicted class labels.

    labels : List[Any], optional
        List of labels to index the matrix. If not provided, labels
        are inferred from the data and sorted. Use this to ensure
        consistent ordering across multiple evaluations.

    Returns
    -------
    Tuple[List[List[int]], List[Any]]
        A tuple containing:

        - matrix: 2D list where matrix[i][j] is the count of samples
          with true label labels[i] predicted as labels[j].
        - labels: The label ordering used for the matrix rows/columns.

    Raises
    ------
    ValueError
        If y_true and y_pred have different lengths.

    See Also
    --------
    accuracy_score : Single accuracy metric.
    precision_recall_f1 : Precision/recall from confusion matrix.

    Notes
    -----
    Reading the confusion matrix:

    For binary classification with labels [Negative, Positive]:

    ::

                      Predicted
                    Neg    Pos
        Actual Neg [ TN    FP ]
               Pos [ FN    TP ]

    Where:
    - TN (True Negative): Correctly predicted negative
    - FP (False Positive): Incorrectly predicted positive (Type I error)
    - FN (False Negative): Incorrectly predicted negative (Type II error)
    - TP (True Positive): Correctly predicted positive

    Derived metrics:
    - Accuracy = (TN + TP) / total
    - Precision = TP / (TP + FP)
    - Recall = TP / (TP + FN)
    - Specificity = TN / (TN + FP)

    Examples
    --------
    Binary classification:

    >>> y_true = [0, 0, 1, 1, 0, 1]
    >>> y_pred = [0, 1, 1, 1, 0, 0]
    >>> matrix, labels = confusion_matrix(y_true, y_pred)
    >>> print(f"Labels: {labels}")
    Labels: [0, 1]
    >>> for row in matrix:
    ...     print(row)
    [2, 1]
    [1, 2]

    Multi-class with specific label order:

    >>> y_true = ['cat', 'dog', 'bird', 'cat']
    >>> y_pred = ['cat', 'bird', 'bird', 'dog']
    >>> matrix, labels = confusion_matrix(
    ...     y_true, y_pred,
    ...     labels=['bird', 'cat', 'dog']
    ... )
    >>> # Row 0 = actual bird, Row 1 = actual cat, Row 2 = actual dog
    >>> # Col 0 = pred bird, Col 1 = pred cat, Col 2 = pred dog
    """
    if len(y_true) != len(y_pred):
        raise ValueError(
            f"y_true and y_pred must have same length: "
            f"{len(y_true)} vs {len(y_pred)}"
        )

    if labels is None:
        labels = sorted(set(y_true) | set(y_pred), key=str)

    label_to_idx = {label: i for i, label in enumerate(labels)}
    n_labels = len(labels)

    # Initialize matrix with zeros
    matrix = [[0] * n_labels for _ in range(n_labels)]

    for yt, yp in zip(y_true, y_pred):
        if yt in label_to_idx and yp in label_to_idx:
            i = label_to_idx[yt]
            j = label_to_idx[yp]
            matrix[i][j] += 1

    return matrix, labels


def mean_squared_error(
    y_true: List[float],
    y_pred: List[float],
    squared: bool = True,
) -> float:
    """
    Calculate Mean Squared Error (MSE) or Root Mean Squared Error (RMSE).

    MSE measures the average squared difference between predicted and
    actual values. RMSE is the square root of MSE, giving error in the
    same units as the target variable.

    Parameters
    ----------
    y_true : List[float]
        Ground truth (actual) values.

    y_pred : List[float]
        Predicted values. Must have the same length as y_true.

    squared : bool, default=True
        If True, returns MSE. If False, returns RMSE (square root of MSE).

    Returns
    -------
    float
        The MSE or RMSE value. Lower values indicate better fit.
        - MSE >= 0, with 0 being perfect prediction.
        - RMSE >= 0, in the same units as the target.

    Raises
    ------
    ValueError
        If y_true and y_pred have different lengths or are empty.

    See Also
    --------
    r2_score : Relative measure of fit quality.
    calculate_metrics : Get all regression metrics at once.

    Notes
    -----
    MSE formula: MSE = (1/n) * Σ(y_true - y_pred)²

    RMSE formula: RMSE = √MSE

    Comparison of MSE vs MAE:

    +--------+--------------------------------+--------------------------------+
    | Metric | Pros                           | Cons                           |
    +========+================================+================================+
    | MSE    | Penalizes large errors more,   | Sensitive to outliers,         |
    |        | differentiable everywhere      | units are squared              |
    +--------+--------------------------------+--------------------------------+
    | RMSE   | Same units as target,          | Still sensitive to outliers    |
    |        | interpretable                  |                                |
    +--------+--------------------------------+--------------------------------+
    | MAE    | Robust to outliers,            | Not differentiable at 0,       |
    |        | same units as target           | treats all errors equally      |
    +--------+--------------------------------+--------------------------------+

    Examples
    --------
    Calculate MSE:

    >>> y_true = [3.0, -0.5, 2.0, 7.0]
    >>> y_pred = [2.5, 0.0, 2.0, 8.0]
    >>> mean_squared_error(y_true, y_pred)
    0.375

    Calculate RMSE (more interpretable):

    >>> mean_squared_error(y_true, y_pred, squared=False)
    0.6123724356957945

    Interpretation: On average, predictions differ from actual values
    by about 0.61 units.
    """
    if len(y_true) != len(y_pred):
        raise ValueError(
            f"y_true and y_pred must have same length: "
            f"{len(y_true)} vs {len(y_pred)}"
        )

    if not y_true:
        raise ValueError("Inputs cannot be empty")

    mse = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)

    if squared:
        return mse
    else:
        return math.sqrt(mse)


def _mean_absolute_error(y_true: List[float], y_pred: List[float]) -> float:
    """
    Calculate Mean Absolute Error (MAE).

    Internal helper function. MAE measures the average absolute
    difference between predicted and actual values.

    Parameters
    ----------
    y_true : List[float]
        Ground truth values.

    y_pred : List[float]
        Predicted values.

    Returns
    -------
    float
        The MAE value.
    """
    return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / len(y_true)


def r2_score(y_true: List[float], y_pred: List[float]) -> float:
    """
    Calculate the R-squared (coefficient of determination) score.

    R² measures how well predictions approximate the actual values
    compared to a baseline model that always predicts the mean.

    Parameters
    ----------
    y_true : List[float]
        Ground truth (actual) values.

    y_pred : List[float]
        Predicted values. Must have the same length as y_true.

    Returns
    -------
    float
        The R² score, typically between 0 and 1:

        - R² = 1.0: Perfect predictions.
        - R² = 0.0: Model performs same as predicting the mean.
        - R² < 0.0: Model is worse than predicting the mean.

    Raises
    ------
    ValueError
        If y_true and y_pred have different lengths or are empty.

    See Also
    --------
    mean_squared_error : Absolute measure of prediction error.
    calculate_metrics : Get all regression metrics at once.

    Notes
    -----
    Formula: R² = 1 - (SS_res / SS_tot)

    Where:
    - SS_res = Σ(y_true - y_pred)² (residual sum of squares)
    - SS_tot = Σ(y_true - y_mean)² (total sum of squares)

    Interpretation guide:

    +-------------+--------------------------------------------------+
    | R² Value    | Interpretation                                   |
    +=============+==================================================+
    | 0.9 - 1.0   | Excellent fit                                    |
    +-------------+--------------------------------------------------+
    | 0.7 - 0.9   | Good fit                                         |
    +-------------+--------------------------------------------------+
    | 0.5 - 0.7   | Moderate fit                                     |
    +-------------+--------------------------------------------------+
    | 0.3 - 0.5   | Weak fit                                         |
    +-------------+--------------------------------------------------+
    | < 0.3       | Poor fit (model may not be appropriate)          |
    +-------------+--------------------------------------------------+
    | < 0         | Model is worse than mean baseline                |
    +-------------+--------------------------------------------------+

    Cautions:
    - R² can increase by adding any predictor, even random noise.
    - Use adjusted R² when comparing models with different numbers
      of predictors.
    - High R² doesn't prove causation or model correctness.

    Examples
    --------
    Good fit:

    >>> y_true = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> y_pred = [1.1, 2.0, 2.9, 4.1, 5.0]
    >>> r2_score(y_true, y_pred)
    0.99

    Perfect fit:

    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [1.0, 2.0, 3.0]
    >>> r2_score(y_true, y_pred)
    1.0

    Poor fit (worse than mean):

    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [3.0, 2.0, 1.0]  # Reversed predictions
    >>> r2_score(y_true, y_pred)
    -3.0
    """
    if len(y_true) != len(y_pred):
        raise ValueError(
            f"y_true and y_pred must have same length: "
            f"{len(y_true)} vs {len(y_pred)}"
        )

    if not y_true:
        raise ValueError("Inputs cannot be empty")

    # Calculate mean of y_true
    y_mean = sum(y_true) / len(y_true)

    # Total sum of squares
    ss_tot = sum((yt - y_mean) ** 2 for yt in y_true)

    # Residual sum of squares
    ss_res = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))

    # Handle case where all y_true values are identical
    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0

    return 1 - (ss_res / ss_tot)


def cross_validate(
    model_fn: Callable[[List[List[float]], List[Any]], Callable[[List[float]], Any]],
    data: List[List[float]],
    labels: List[Any],
    k_folds: int = 5,
    metric: Literal["accuracy", "mse", "r2"] = "accuracy",
    random_seed: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Perform k-fold cross-validation on a model.

    Cross-validation provides a more robust estimate of model performance
    by training and evaluating the model on multiple different train/test
    splits of the data.

    Parameters
    ----------
    model_fn : Callable
        A function that takes (X_train, y_train) and returns a trained
        model (a prediction function). The returned prediction function
        should take a single sample and return a prediction.

        Example::

            def train_model(X, y):
                # Train your model here
                return lambda x: predict(x)  # Return prediction function

    data : List[List[float]]
        Feature vectors. Shape: (n_samples, n_features).

    labels : List[Any]
        Target labels/values corresponding to each sample.

    k_folds : int, default=5
        Number of folds. Common choices are 5 or 10. Higher values
        give more robust estimates but take longer.

    metric : {'accuracy', 'mse', 'r2'}, default='accuracy'
        The metric to compute for each fold:

        - 'accuracy': Classification accuracy (for classifiers)
        - 'mse': Mean Squared Error (for regressors)
        - 'r2': R-squared score (for regressors)

    random_seed : int, optional
        Seed for shuffling data before splitting into folds.
        Set for reproducible results.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing:

        - 'scores': List of scores for each fold
        - 'mean': Mean score across all folds
        - 'std': Standard deviation of scores
        - 'k_folds': Number of folds used

    Raises
    ------
    ValueError
        If k_folds < 2 or k_folds > n_samples.
        If data and labels have different lengths.

    Notes
    -----
    How k-fold cross-validation works:

    1. Shuffle and split data into k equal-sized folds
    2. For each fold i:
       a. Use fold i as test set
       b. Use remaining k-1 folds as training set
       c. Train model on training set
       d. Evaluate on test set
    3. Report mean and std of all k evaluations

    Benefits:
    - Uses all data for both training and testing
    - Provides variance estimate of performance
    - Reduces overfitting risk in model selection

    Choosing k:
    - k=5: Good balance of bias and variance
    - k=10: Lower bias, higher variance
    - k=n (Leave-One-Out): Unbiased but high variance, slow

    Examples
    --------
    Cross-validate a simple classifier:

    >>> def simple_classifier(X_train, y_train):
    ...     # A trivial "classifier" that always predicts the mode
    ...     from collections import Counter
    ...     mode = Counter(y_train).most_common(1)[0][0]
    ...     return lambda x: mode
    ...
    >>> data = [[i] for i in range(100)]
    >>> labels = [0] * 50 + [1] * 50
    >>> results = cross_validate(
    ...     simple_classifier, data, labels,
    ...     k_folds=5, metric='accuracy', random_seed=42
    ... )
    >>> print(f"Mean accuracy: {results['mean']:.2%} (+/- {results['std']:.2%})")

    Cross-validate a regressor:

    >>> def simple_regressor(X_train, y_train):
    ...     # A trivial regressor that predicts the mean
    ...     mean_y = sum(y_train) / len(y_train)
    ...     return lambda x: mean_y
    ...
    >>> data = [[i] for i in range(100)]
    >>> labels = [i * 2 + 1 for i in range(100)]  # y = 2x + 1
    >>> results = cross_validate(
    ...     simple_regressor, data, labels,
    ...     k_folds=5, metric='r2', random_seed=42
    ... )
    """
    if len(data) != len(labels):
        raise ValueError(
            f"data and labels must have same length: "
            f"{len(data)} vs {len(labels)}"
        )

    n_samples = len(data)

    if k_folds < 2:
        raise ValueError(f"k_folds must be >= 2, got {k_folds}")

    if k_folds > n_samples:
        raise ValueError(
            f"k_folds ({k_folds}) cannot be greater than "
            f"n_samples ({n_samples})"
        )

    # Shuffle indices
    if random_seed is not None:
        random.seed(random_seed)

    indices = list(range(n_samples))
    random.shuffle(indices)

    # Calculate fold sizes
    fold_size = n_samples // k_folds
    scores = []

    for fold in range(k_folds):
        # Determine test indices for this fold
        start_idx = fold * fold_size
        end_idx = start_idx + fold_size if fold < k_folds - 1 else n_samples

        test_indices = set(indices[start_idx:end_idx])
        train_indices = [i for i in indices if i not in test_indices]

        # Split data
        X_train = [data[i] for i in train_indices]
        y_train = [labels[i] for i in train_indices]
        X_test = [data[i] for i in test_idx for test_idx in [list(test_indices)]][0:0]  # Will fix
        y_test_list = []

        # Correct test data extraction
        test_idx_list = list(test_indices)
        X_test = [data[i] for i in test_idx_list]
        y_test = [labels[i] for i in test_idx_list]

        # Train model
        predict_fn = model_fn(X_train, y_train)

        # Get predictions
        y_pred = [predict_fn(x) for x in X_test]

        # Calculate metric
        if metric == "accuracy":
            score = accuracy_score(y_test, y_pred)
        elif metric == "mse":
            score = mean_squared_error(y_test, y_pred)
        elif metric == "r2":
            score = r2_score(y_test, y_pred)
        else:
            raise ValueError(
                f"Unknown metric '{metric}'. "
                f"Supported: 'accuracy', 'mse', 'r2'"
            )

        scores.append(score)

    # Calculate statistics
    mean_score = sum(scores) / len(scores)
    variance = sum((s - mean_score) ** 2 for s in scores) / len(scores)
    std_score = math.sqrt(variance)

    return {
        "scores": scores,
        "mean": mean_score,
        "std": std_score,
        "k_folds": k_folds,
    }
