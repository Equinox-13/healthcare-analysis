import pandas as pd


class PatientDashboard:

    def read_csv(self, path):
        """
        This method  will read a csv file and returns a dataframe
        args : path
        return : df
        """
        df = pd.read_csv(path, header=0, delimiter=',')
        return df

    def add_total_expense_column(self, patient_discharge_df):
        """
        This method will append 'added_amt' column that consists of sum of all the expenses incurred
        by a patient to the patient_discharge_df
        return: patient_discharge_df
        """
        patient_discharge_df['added_amt'] = patient_discharge_df.iloc[:, 11:20].sum(axis=1)
        return patient_discharge_df

    def fetch_patient_phone(self, patient_discharge_df, order):
        """
        This method with return a dataframe with the top 10 or bottom 10 patient with their phoneno
        based on added_amt
        args: patient_discharge_df, order
        return: result_df
        """
        if order == "top_10":
            patient_df_largest_ten = patient_discharge_df.nlargest(10, ["added_amt"])
            result_df = patient_df_largest_ten[[
                "registrationno", "patientname", "phone", "department", "added_amt"]]
        elif order == "bottom_10":
            patient_df_smallest_ten = patient_discharge_df.nsmallest(10, ["added_amt"])
            result_df = patient_df_smallest_ten[[
                "registrationno", "patientname", "phone", "department", "added_amt"]]
        return result_df

    def fetch_patient_by_age(self, patient_discharge_df, patient_details_df):
        """
        This method will return a dataframe with the patient details sorted by max age
        args: patient_discharge_df, patient_details_df
        returns: patient_discharge_max_age_df
        """
        patient_discharge_df['age'] = patient_discharge_df.registrationno.map(patient_details_df.set_index(
            "registrationno")['age'])
        patient_discharge_max_age_df = patient_discharge_df[["registrationno", "phone", "patientname", "age",
                                                             "cityname", "districtname", "statename", "added_amt"]]
        patient_discharge_max_age_df = patient_discharge_max_age_df.sort_values(by=['age'], ascending=False)
        return patient_discharge_max_age_df

    def to_csv(self, df, path):
        """
        this method  will write csv file in dashboard_files/patient directory
        return: True
        """
        df.to_csv(path, encoding='utf-8', index=False)
        return True


if __name__ == '__main__':
    patient_wise_obj = PatientDashboard()

    patient_discharge_df = patient_wise_obj.read_csv('../../clean_files/clean_patient_discharge_details_dump.csv')

    patient_discharge_df = patient_wise_obj.add_total_expense_column(patient_discharge_df)

    # Top 10 records with max added_amt
    top_ten_added_amt_patient_df_phone = patient_wise_obj.fetch_patient_phone(
        patient_discharge_df, order="top_10")
    patient_wise_obj.to_csv(top_ten_added_amt_patient_df_phone, '../../dashboard_files/patient/max_patient_expense_wise.csv')
    print("max_patient_expense_wise.csv created succesfully=========")

    # Bottom 10 records with min added_amt
    bottom_ten_added_amt_patient_df_phone = patient_wise_obj.fetch_patient_phone(
        patient_discharge_df, order="bottom_10")
    patient_wise_obj.to_csv(bottom_ten_added_amt_patient_df_phone,
                            '../../dashboard_files/patient/min_patient_expense_wise.csv')
    print("min_patient_expense_wise.csv created succesfully=========")

    # Patient details ordered by max age
    patient_details_df = patient_wise_obj.read_csv('../../clean_files/clean_patient_details_dump.csv')
    patient_discharge_max_age_df = patient_wise_obj.fetch_patient_by_age(patient_discharge_df, patient_details_df)
    patient_wise_obj.to_csv(patient_discharge_max_age_df, '../../dashboard_files/patient/max_age_wise.csv')
    print("max_age_wise.csv created succesfully=========")