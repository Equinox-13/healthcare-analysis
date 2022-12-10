import pandas as pd


class DepartmentDashboard:

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
        This method will append 'added_amt' column that consists of sum of all the expenses incurred by a patient
        to the patient_discharge_df
        return: patient_discharge_df
        """
        patient_discharge_df['added_amt'] = patient_discharge_df.iloc[:, 11:20].sum(axis=1)
        return patient_discharge_df

    def group_by_department_wise_script(self, patient_discharge_df):
        """
        Group by department wise with sum of 'added_amt', count of 'patientname' and sum of 'discountamount'
        return: group_by_department_df
        """
        group_by_department_df = patient_discharge_df.groupby("department").agg(
            added_amt=pd.NamedAgg(column='added_amt', aggfunc='sum'),
            patient_count=pd.NamedAgg(column='patientname', aggfunc='count'),
            discountamount=pd.NamedAgg(column='discountamount', aggfunc='sum'), ).reset_index()

        return group_by_department_df

    def to_csv(self, group_by_department_df, path):
        """
        this method  will write department_wise.csv file in dashboard_files/department directory
        return: True
        """
        group_by_department_df.to_csv(path, encoding='utf-8', index=False)
        return True


if __name__ == '__main__':
    department_wise_obj = DepartmentDashboard()
    patient_discharge_df = department_wise_obj.read_csv('../../clean_files/clean_patient_discharge_details_dump.csv')
    patient_discharge_df = department_wise_obj.add_total_expense_column(patient_discharge_df)
    group_by_department_df = department_wise_obj.group_by_department_wise_script(patient_discharge_df)
    department_wise_obj.to_csv(group_by_department_df, '../../dashboard_files/department/department_wise.csv')
    print("script executed succesfully=========")
