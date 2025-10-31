from frictionless import validate
import pandas as pd

def validate_csv(csv_path: str, schema_path: str) -> None:
    """
    Validates a CSV file against a Frictionless schema and checks that the 'ID' column is unique and sequential.

    Args:
        csv_path (str): Path to the CSV file.
        schema_path (str): Path to the schema JSON file.
    """

    print(f"🔍 Validating {csv_path} against schema {schema_path}...\n")

    # Frictionless schema validation
    report = validate(csv_path, schema=schema_path)
    print("📋 Frictionless schema validation report:")
    print(report)

    # Additional checks with pandas
    df = pd.read_csv(csv_path)

    # Check uniqueness
    if df["ID"].is_unique:
        print("✅ All IDs are unique.")
    else:
        print("❌ Duplicate IDs found.")

    # Check sequentiality
    expected_ids = list(range(1, len(df) + 1))
    actual_ids = sorted(df["ID"].dropna().astype(int).tolist())

    if actual_ids == expected_ids:
        print("✅ IDs are sequential.")
    else:
        print("❌ IDs are not sequential.")

# Optional: Run directly from CLI
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python validate_csv.py <csv_path> <schema_path>")
    else:
        validate_csv(sys.argv[1], sys.argv[2])