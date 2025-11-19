import pandas as pd
import os
import utils
from validator import CheckBenchmarkData
#from utils import count_matches
#from utils import get_isco_scheme_data
#from utils import process_excel_to_csv
from oc3i import Coder

ISCO_DATA_SOURCE = "https://raw.githubusercontent.com/datasciencecampus/occupationcoder-international/main/data/ISCO-08%20EN%20Structure%20and%20definitions.xlsx"
ISCO_DATA_FILE = "data/ISCO-08-scheme.xlsx"
PROCESSED_ISCO_DATA = "data/ISCO-08-processed.csv"
BENCHMARK_DATA_FILE = "data/isco_benchmark_data.csv"
allowed_types = {"Exact match", "Semantic ambiguity", "Scheme ambiguity", "Deeper ambiguity", "Input issue", "Exact match fail"}
columns_to_check = ["ID","TITLE","TASKS","INDUSTRY","MANUAL_ISCO1","MANUAL_ISCO2","MANUAL_ISCO3","TYPE","COMMENTS"]

benchmark_dat = pd.read_csv(BENCHMARK_DATA_FILE, dtype={'MANUAL_ISCO1': str, 'MANUAL_ISCO2': str, 'MANUAL_ISCO3': str})
if not os.path.exists(ISCO_DATA_FILE):
    get_isco_scheme_data(source_url=ISCO_DATA_SOURCE, local_file_path=ISCO_DATA_FILE)

isco_scheme_dat = pd.read_excel(ISCO_DATA_FILE, dtype={'ISCO 08 Code': str, 'Tasks include': str}, keep_default_na=False)

allowed_isco_codes = isco_scheme_dat["ISCO 08 Code"]

validator = CheckBenchmarkData(benchmark_dat)

validator.check_columns(columns_to_check, raise_error=True)
validator.check_text_length("TITLE", max_length=50, raise_error=True)
validator.check_missing_values("ID", raise_error=True)
validator.check_missing_values("TITLE", raise_error=True)
validator.check_unique_integers("ID", raise_error=True)
validator.check_lookup_values("MANUAL_ISCO1", allowed_isco_codes, raise_error=True)
validator.check_allowed_values("TYPE", allowed_types)

report = validator.get_report()
print(report)

if not report["message"].eq("OK").all():
    raise ValueError("Some validation checks on benchmark data failed, bailing out, sorry!")

# Process ISCO data for use with classifai
utils.process_excel_to_csv(ISCO_DATA_FILE, PROCESSED_ISCO_DATA)

# Initialise the coder with the desired coding scheme (here ISCO):
coder = Coder(scheme = "isco")

# Code benchmark data using oc3i:
coded_benchmark = coder.code_data_frame(benchmark_dat, 
                                        title_column = "TITLE", 
                                        description_column = "TASKS", 
                                        sector_column = "INDUSTRY")

# Count number of matches in coded data (currently assuming one [manual code] to many [predictions])
count_matches(coded_benchmark, match_col="MANUAL_ISCO1", 
              prediction_cols= ["prediction 1", "prediction 2", "prediction 3"], 
              output="proportion")





