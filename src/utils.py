import pandas as pd

def count_matches(df: pd.DataFrame, match_col: str, prediction_cols: list, output: str = "absolute"):
    """
    Calculate the number or proportion of cases where values in a given column (match_col) 
    in a Pandas dataframe (df) matches the values in both the first column name given in 
    prediction_cols, as well as ANY of the values in column names given in prediction_cols.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing the manual and prediction columns.
    match_col : str
        Name of the column containing manual labels.
    prediction_cols : list
        Names of the columns to compare values in match_col to. Should be a list of column names in df.
    output : str, optional (default = "absolute")
        If "absolute", return counts.
        If "proportion", return proportions of total rows.

    Returns
    -------
    dict
        {
            'pred1_match': number/proportion where manual == prediction 1,
            'any_pred_match': number/proportion where manual matches at least one prediction
        }
    """

    total = len(df)

    pred1_match = (df[match_col] == df[prediction_cols[0]])
    # Comparison against all prediction columns
    any_pred_match = pd.Series(False, index=df.index)
    for col in prediction_cols:
        any_pred_match = any_pred_match | (df[match_col] == df[col])

    if output == "proportion":
        return {
            "pred1_match": pred1_match.mean(),
            "any_pred_match": any_pred_match.mean()
        }
    else:  # absolute counts
        return {
            "pred1_match": pred1_match.sum(),
            "any_pred_match": any_pred_match.sum()
        }