import pandas as pd


class PatientCleaning:

    def read_csv(self):
        """
  this method  will read patient_details_dump.csv file
  return: patient_df
  """
        patient_df = pd.read_csv('../data_files/patient_details_dump.csv', header=0, delimiter=',')
        return patient_df

    def benchmark(self):
        """
  This method will set benchmark values for no. of columns and list of headers
  return: no_of_columns, list_of_headers
  """
        no_of_columns = 7
        list_of_headers = ['REGISTRATIONNO', 'PATIENTNAME', 'Age', 'IPID', 'Gender', 'ADMITDATETIME',
                           'DISCHARGEDATETIME']
        return no_of_columns, list_of_headers

    def validation_fn(self, patient_df, no_of_columns, list_of_header):
        """
  This method will check 3 parameters to validate data file
  i)   delimeter check
  ii)  header content check
  iii) no. of columns check

  return: delimiter_check, header_content_check, no_of_columns_check
  """
        delimiter_check = len(patient_df.columns) > 1
        header_content_check = list_of_headers == list(patient_df)
        no_of_columns_check = len(patient_df.columns) == no_of_columns
        return delimiter_check, header_content_check, no_of_columns_check

    def clean_data(self, patient_df):
        """
  This method cleans inconsistent data and converts datatype of some columns
  i)   lower column name
  ii)  replace spacing between column headers with underscore
  iii) format admitdatetime, dischargedatetime to standard format
  iv)  format registration no., age, ipid  to integer datatype
  """
        patient_df.columns = map(str.lower, patient_df.columns)
        patient_df.columns = patient_df.columns.str.replace(" ", "_")
        patient_df['admitdatetime'] = pd.to_datetime(patient_df['admitdatetime'])
        patient_df['dischargedatetime'] = pd.to_datetime(patient_df['dischargedatetime'])
        patient_df['registrationno'] = patient_df['registrationno'].astype(int)
        patient_df['age'] = patient_df['age'].astype(int)
        #         patient_df['ipid'] = patient_df['ipid'].astype(int)
        return patient_df

    def write_clean_csv(self, patient_clean_df):
        """
  this method  will write clean_patient_details_dump.csv file in cleanfiles/ directory
  return: True
  """
        patient_clean_df.to_csv('clean_files/clean_patient_details_dump.csv', encoding='utf-8', index=False)
        return True


if __name__ == '__main__':
    pclean = PatientCleaning()
    patient_df = pclean.read_csv()
    no_of_columns, list_of_headers = pclean.benchmark()
    delimiter_check, header_content_check, no_of_columns_check = pclean.validation_fn(patient_df, no_of_columns,
                                                                                      list_of_headers)

    if delimiter_check and header_content_check and no_of_columns_check:
        patient_clean_df = pclean.clean_data(patient_df)
        pclean.write_clean_csv(patient_clean_df)
        print("script executed succesfully=========")