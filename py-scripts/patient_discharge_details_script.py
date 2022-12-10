import pandas as pd
import numpy as np


class PatientDischargeCleaning:

    def read_csv(self):
        """
        this method  will read patient_discharge_details_dump.csv file
        return: patient_discharge_df
        """
        patient_discharge_df = pd.read_csv('../data_files/patient_discharge_details_dump.csv', header=0, delimiter=',')
        return patient_discharge_df

    def benchmark(self):
        """
        This method will set benchmark values for no. of columns and list of headers
        return: no_of_columns, list_of_headers
        """
        no_of_columns = 20
        list_of_headers = ['REGISTRATIONNO', 'PATIENTNAME', 'CITYNAME', 'DISTRICTNAME',
                           'STATENAME', 'PHONE', 'ADMITDATETIME', 'DISCHARGEDATETIME',
                           'COMPANY NAME', 'DEPARTMENT', 'DISCOUNTAMOUNT', 'BILLAMOUNT',
                           'ROOM TARIFF', 'PHARMACY', 'Investigations', 'Bedside Procedures',
                           'Physiotherapy', 'Surgeries', 'CONSUMABLES', 'Doctor Consultations']
        return no_of_columns, list_of_headers

    def validation_fn(self, patient_discharge_df, no_of_columns, list_of_header):
        """
        This method will check 3 parameters to validate data file
        i)   delimeter check
        ii)  header content check
        iii) no. of columns check

        return: delimiter_check, header_content_check, no_of_columns_check
        """
        delimiter_check = len(patient_discharge_df.columns) > 1
        header_content_check = list_of_headers == list(patient_discharge_df)
        no_of_columns_check = len(patient_discharge_df.columns) == no_of_columns
        return delimiter_check, header_content_check, no_of_columns_check

    def clean_data(self, patient_discharge_df):
        """
        This method cleans inconsistent data and converts datatype of some columns
        i)   lower column name
        ii)  replace spacing between column headers with underscore
        iii) filter phone no. to 10 digits
        iv)  replace nan with 0
        """
        patient_discharge_df.columns = map(str.lower, patient_discharge_df.columns)
        patient_discharge_df.columns = patient_discharge_df.columns.str.replace(" ", "_")
        patient_discharge_df['admitdatetime'] = pd.to_datetime(patient_discharge_df['admitdatetime'])
        patient_discharge_df['dischargedatetime'] = pd.to_datetime(patient_discharge_df['dischargedatetime'])
        patient_discharge_df['phone'] = patient_discharge_df['phone'].apply(
            lambda x: x if len(x) == 10 else '8888999999')
        patient_discharge_df.fillna(0, inplace=True)
        return patient_discharge_df

    def write_clean_csv(self, patient_discharge_clean_df):
        """
        this method  will write clean_patient_discharge_details_dump.csv file in cleanfiles/ directory
        return: True
        """
        patient_discharge_clean_df.to_csv('../clean_files/clean_patient_discharge_details_dump.csv', encoding='utf-8',
                                          index=False)
        return True


if __name__ == '__main__':
    pdclean = PatientDischargeCleaning()
    patient_discharge_df = pdclean.read_csv()
    no_of_columns, list_of_headers = pdclean.benchmark()
    delimiter_check, header_content_check, no_of_columns_check = pdclean.validation_fn(patient_discharge_df,
                                                                                       no_of_columns, list_of_headers)
    if delimiter_check and header_content_check and no_of_columns_check:
        patient_discharge_clean_df = pdclean.clean_data(patient_discharge_df)
        #         print(patient_discharge_clean_df.head())
        pdclean.write_clean_csv(patient_discharge_clean_df)
        print("script executed succesfully=========")