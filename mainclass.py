import pandas as pd


class EmployeeDataAnalysis:
    def __init__(self, file_path):
        """Load CSV data into a Pandas DataFrame."""
        self.df = pd.read_csv(file_path)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def highest_age_employee(self):
        """Find the employee with the highest age."""
        max_age = self.df.loc[self.df["Age"].idxmax(), "Employee ID"]
        return max_age

    def export_to_excel(self, output_file="employee_data.xlsx"):
        """Save the DataFrame to an Excel file."""
        self.df.to_excel(output_file, index=False)

    def verify_excel_saved(self, output_file="employee_data.xlsx"):
        """Verify if the Excel file is saved correctly by loading it back."""
        try:
            df_loaded = pd.read_excel(output_file)
            return not df_loaded.empty
        except Exception as e:
            return False
