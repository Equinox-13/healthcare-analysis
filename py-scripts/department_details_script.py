import pandas as pd


class DepartmentCleaning:

    def read_csv(self):
        """
        this method  will read department_details_dump.csv file
        return: department_df
        """
        department_df = pd.read_csv('../data_files/department_details_dump.csv', header=0, delimiter=',')
        return department_df

    def benchmark(self):
        """
        This method will set benchmark values for no. of columns and list of headers
        return: no_of_columns, list_of_headers
        """
        no_of_columns = 2
        list_of_headers = ['dep_id', 'Department']
        return no_of_columns, list_of_headers

    def validation_fn(self, department_df, no_of_columns, list_of_headers):
        """
        This method will check 3 parameters to validate data file
        i)   delimeter check
        ii)  header content check
        iii) no. of columns check

        return: delimiter_check, header_content_check, no_of_columns_check
        """
        delimiter_check = len(department_df.columns) > 1
        header_content_check = list_of_headers == list(department_df)
        no_of_columns_check = len(department_df.columns) == no_of_columns
        return delimiter_check, header_content_check, no_of_columns_check

    def clean_data(self, department_df):
        """
        This method cleans inconsistent data
        i)   lower column name
        ii)  replace spacing between column headers with underscore
        iii) format dep_id to integer datatype
        """
        department_df.columns = map(str.lower, department_df.columns)
        department_df.columns = department_df.columns.str.replace(" ", "_")
        department_df['dep_id'] = department_df['dep_id'].astype(int)
        return department_df

    def write_clean_csv(self, department_clean_df):
        """
        this method  will write clean_department_details_dump.csv file in cleanfiles/ directory
        return: True
        """
        department_clean_df.to_csv('../clean_files/clean_department_details_dump.csv', encoding='utf-8', index=False)
        return True


if __name__ == '__main__':
    dpclean = DepartmentCleaning()
    department_df = dpclean.read_csv()
    no_of_columns, list_of_headers = dpclean.benchmark()
    delimiter_check, header_content_check, no_of_columns_check = dpclean.validation_fn(department_df, no_of_columns,
                                                                                       list_of_headers)

    if delimiter_check and header_content_check and no_of_columns_check:
        department_clean_df = dpclean.clean_data(department_df)
        dpclean.write_clean_csv(department_clean_df)
        print("script executed succesfully for department_details_script.py=========")

