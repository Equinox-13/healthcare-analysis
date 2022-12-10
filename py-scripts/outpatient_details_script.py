import pandas as pd


class OutPatientCleaning:

    def read_csv(self):
        """
        this method  will read outpatient_details_dump.csv file
        return: out_patient_df
        """
        out_patient_df = pd.read_csv('../data_files/outpatient_details_dump.csv', header=0, delimiter=',')
        return out_patient_df

    def benchmark(self):
        """
        This method will set benchmark values for no. of columns and list of headers
        return: no_of_columns, list_of_headers
        """
        no_of_columns = 7
        list_of_headers = ['RegistrationNo', 'OPDATE', 'PatName', 'Amount', 'Department', 'Status', 'DISCOUNT']
        return no_of_columns, list_of_headers

    def validation_fn(self, out_patient_df, no_of_columns, list_of_headers):
        """
        This method will check 3 parameters to validate data file
        i)   delimeter check
        ii)  header content check
        iii) no. of columns check

        return: delimiter_check, header_content_check, no_of_columns_check
        """
        delimiter_check = len(out_patient_df.columns) > 1
        header_content_check = list_of_headers == list(out_patient_df)
        no_of_columns_check = len(out_patient_df.columns) == no_of_columns
        return delimiter_check, header_content_check, no_of_columns_check

    def clean_data(self, out_patient_df):
        """
        This method cleans inconsistent data and converts datatype of some columns
        i)   lower column name
        ii)  replace spacing between column headers with underscore
        iii) format date to standard format
        iv)  format registration no. to integer datatype
        v)   format amount in float datatype
        """
        out_patient_df.columns = map(str.lower, out_patient_df.columns)
        out_patient_df.columns = out_patient_df.columns.str.replace(" ", "_")
        out_patient_df['opdate'] = pd.to_datetime(out_patient_df['opdate'])
        out_patient_df['registrationno'] = out_patient_df['registrationno'].astype(int)
        out_patient_df['amount'] = out_patient_df['amount'].astype(float)
        return out_patient_df

    def write_clean_csv(self, out_patient_clean_df):
        """
        this method  will write clean_outpatient_details_dump.csv file in cleanfiles/ directory
        return: True
        """
        out_patient_clean_df.to_csv('../clean_files/clean_outpatient_details_dump.csv', encoding='utf-8', index=False)
        return True


if __name__ == '__main__':
    opclean = OutPatientCleaning()
    out_patient_df = opclean.read_csv()
    no_of_columns, list_of_headers = opclean.benchmark()
    delimiter_check, header_content_check, no_of_columns_check = opclean.validation_fn(out_patient_df, no_of_columns,
                                                                                       list_of_headers)

    if delimiter_check and header_content_check and no_of_columns_check:
        out_patient_clean_df = opclean.clean_data(out_patient_df)
        opclean.write_clean_csv(out_patient_clean_df)
        print("script executed succesfully=========")

