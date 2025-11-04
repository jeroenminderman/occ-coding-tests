import pandas as pd

class CheckBenchmarkData:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.results = []

    def add_result(self, check_name, success, message, raise_error=False):
        """
        Helper to record the result of a validation check and optionally raise an error.

        This function creates a structured output of a validation check and appends this to self.results.
        Includes the name of the check, whether it was successful, and any message.
        'raise_error' controls whether a ValueError should be generated immediately.

        Parameters
        ----------
        check_name: str
            Name of the validation check to be reported.
        success: bool
            Whether the check was successful/passes.
        message: str
            Message associated with the validation result.
        raise_error: bool, optional, default = False.
            Whether a ValueEorror should be raised immediately if the check was not successful (if not True, the function simply outputs the result of the test.)
        
        Returns
        -------
        None
        
        Raises
        ------
        ValueError
            If 'raise_error' is True, and the check failed.

        """
        
        self.results.append({
            "check": check_name,
            "success": success,
            "message": message
        })
        if raise_error and not success:
            raise ValueError(f"Validation failed: {check_name} - {message}")

    def check_columns(self, required_columns, allow_extra=False, raise_error=False):
        present_cols = set(self.df.columns)
        required_cols = set(required_columns)

        missing = required_cols - present_cols
        extra = present_cols - required_cols

        success = True
        message_parts = []

        if missing:
            success = False
            message_parts.append(f"Missing columns: {', '.join(sorted(missing))}")
        
        if extra:
            success = False
            message_parts.append(f"Unexpected columns: {', '.join(sorted(extra))}")

        message = " | ".join(message_parts) if message_parts else "OK"

        self.add_result(
            "Required Columns",
            success,
            message,
            raise_error
        )

    def check_text_length(self, column, max_length, raise_error=False):
        if column not in self.df:
            self.add_result("Text Length", False, f"Column '{column}' missing", raise_error)
            return
        too_long = self.df[column].dropna().astype(str).apply(len) > max_length
        success = not too_long.any()
        self.add_result(
            f"Text Length - {column}",
            success,
            f"{too_long.sum()} values exceed max length {max_length}" if not success else "OK",
            raise_error
        )

    def check_missing_values(self, column, raise_error=False):
        if column not in self.df:
            self.add_result("Missing Values", False, f"Column '{column}' missing", raise_error)
            return
        missing_count = self.df[column].isna().sum()
        success = missing_count == 0
        self.add_result(
            f"Missing Values - {column}",
            success,
            f"{missing_count} missing values" if not success else "OK",
            raise_error
        )

    def check_unique_integers(self, column, raise_error=False):
        if column not in self.df:
            self.add_result("Unique Integers", False, f"Column '{column}' missing", raise_error)
            return

        valid_ints = self.df[column].apply(lambda x: isinstance(x, int))
        success = valid_ints.all() and self.df[column].is_unique

        message = []
        if not valid_ints.all():
            message.append("Non-integer values found")
        if not self.df[column].is_unique:
            message.append("Duplicate values found")

        self.add_result(
            f"Unique Integers - {column}",
            success,
            "; ".join(message) if message else "OK",
            raise_error
        )

    def check_lookup_values(self, column, lookup_values, raise_error=False):
        if column not in self.df:
            self.add_result("Lookup Values", False, f"Column '{column}' missing", raise_error)
            return

        col = self.df[column]
        valid_digit_count = col.apply(lambda x: isinstance(x, str) and len(x) <= 4)
        in_lookup = col.isin(lookup_values)
        success = valid_digit_count.all() and in_lookup.all()

        message = []
        if not valid_digit_count.all():
            message.append("Invalid digit length or non-integer values")
        if not in_lookup.all():
            invalid_vals = col[~in_lookup].unique()
            message.append(f"Invalid lookup values: {invalid_vals}")

        self.add_result(
            f"Lookup Values - {column}",
            success,
            "; ".join(message) if message else "OK",
            raise_error
        )

    def check_allowed_values(self, column, allowed_set, raise_error=False):
        if column not in self.df:
            self.add_result("Allowed Values", False, f"Column '{column}' missing", raise_error)
            return

        col = self.df[column]

        invalid_mask = ~col.isin(allowed_set) & ~col.isna()
        invalid = col[invalid_mask]
        success = invalid.empty

        self.add_result(
            f"Allowed Values - {column}",
            success,
            f"Invalid values: {invalid.unique()}" if not success else "OK",
            raise_error
        )

    def get_report(self):
        return pd.DataFrame(self.results)