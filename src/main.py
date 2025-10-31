from validate_benchmark import validate_csv
from frictionless import Resource
from pathlib import Path

# Get the path to the current script (main.py)
current_dir = Path(__file__).parent

# Build the path to the CSV file
csv_path = current_dir.parent / "data" / "isco_benchmark_data.csv"
schema_path = current_dir.parent / "data" / "isco_benchmark_data_schema.json"

benchmark_data_source = Resource(path=csv_path, trusted=True)
validate_csv(benchmark_data_source, str(schema_path))
