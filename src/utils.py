import pandas as pd
import requests

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
    
def process_excel_to_csv(input_file: str, output_file: str, code_digit_threshold: int = 4):
    """
    Reads an Excel file containing occupation codes and related text fields, filters rows based on the length of the occupation code,
    concatenates relevant text fields, and saves the processed data to a CSV file.  
    Parameters
    ----------
    input_file : str
        Path to the input Excel file.
    output_file : str
        Path to the output CSV file.
    code_digit_threshold : int, optional (default = 4)
        Minimum length of the occupation code to include a row in the output.
    Returns
    -------
    None
    """
    df = pd.read_excel(
        input_file,
        sheet_name='ISCO-08 EN Struct and defin',
        engine='openpyxl',
        dtype={'ISCO 08 Code': str}
    )

    df = df[df['ISCO 08 Code'].str.len() >= code_digit_threshold]

    df.fillna('', inplace=True)

    df['text'] = df['Title EN'] + ' ' + df['Definition'] + ' ' + df['Tasks include'] + ' ' + df['Included occupations']

    result_df = df[['ISCO 08 Code', 'Title EN', 'text']].rename(columns={
        'ISCO 08 Code': 'id',
        'Title EN': 'title'
    })

    result_df.to_csv(output_file, index=False)
    print(f"Filtered and processed data saved to {output_file}")


def get_isco_scheme_data(source_url: str, local_file_path: str):
    """
    Downloads the ISCO scheme data from the specified URL and saves it to a local file.
    Parameters
    ----------
    source_url : str
        URL to download the ISCO scheme data from.  
    local_file_path : str
        Path to save the downloaded ISCO scheme data.
    Returns
    -------
    None
    """
    response = requests.get(source_url)
    with open(local_file_path, "wb") as f:
        f.write(response.content)
