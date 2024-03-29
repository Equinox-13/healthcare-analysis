import pandas as pd

class PowerplayDashboard:

    def latest_50_admit_date_wise(self):
        patient_discharge_df = pd.read_csv('../../clean_files/clean_patient_discharge_details_dump.csv', header=0,
                                           delimiter=',')
        patient_details_df = pd.read_csv('../../clean_files/clean_patient_details_dump.csv', header=0, delimiter=',')

        # Registration_No ,  Age , Gender , City_Name , District_Name , Statename,  latest by admit date
        result_df = pd.merge(patient_discharge_df, patient_details_df[["registrationno", "age", "gender"]],
                             on='registrationno')
        merged_df = result_df[
            ["registrationno", "age", "gender", "cityname", "districtname", "statename", "admitdatetime"]]
        merged_df = merged_df.sort_values(by=['admitdatetime'], ascending=False).head(50)

        # Export to csv
        merged_df.to_csv('../../dashboard_files/powerplay/latest_50_admitdate_wise.csv', encoding='utf-8', index=False)
        print("latest_50_admitdate_wise.csv created succesfully=========")

    def latest_50_opdate_wise(self):
        # registration, opdate(order by desc), patientname, age, city, district -(50 records)
        outpatient_details_df = pd.read_csv('../../clean_files/clean_outpatient_details_dump.csv', header=0,
                                            delimiter=',')
        patient_discharge_details_df = pd.read_csv('../../clean_files/clean_patient_discharge_details_dump.csv',
                                                   header=0,
                                                   delimiter=',')

        result_df = pd.merge(outpatient_details_df,
                             patient_discharge_details_df[["registrationno", "cityname", "districtname", "statename"]],
                             on='registrationno')
        result_df = result_df[["registrationno", "opdate", "patname", "cityname", "districtname", "statename"]]
        result_df['opdate'] = pd.to_datetime(result_df['opdate'])
        result_df = result_df.sort_values(by=['opdate'], ascending=False).head(50)

        # Export to csv
        result_df.to_csv('../../dashboard_files/powerplay/latest_50_opdate_wise.csv', encoding='utf-8', index=False)
        print("latest_50_opdate_wise.csv created succesfully=========")

    def amount_greater_than_500_wise(self):
        outpatient_details_df = pd.read_csv('../../clean_files/clean_outpatient_details_dump.csv', header=0,
                                            delimiter=',')
        patient_discharge_details_df = pd.read_csv('../../clean_files/clean_patient_discharge_details_dump.csv',
                                                   header=0,
                                                   delimiter=',')

        # registration, opdate, patientname,city, district, state, amount > 500
        result_df = pd.merge(outpatient_details_df,
                             patient_discharge_details_df[["registrationno", "cityname", "districtname", "statename"]],
                             on='registrationno')
        result_df = result_df[
            ["registrationno", "opdate", "patname", "amount", "cityname", "districtname", "statename"]]
        result_df = result_df[result_df.amount > 500]

        # Export to csv
        result_df.to_csv('../../dashboard_files/powerplay/amount_greater_than_500_wise.csv', encoding='utf-8',
                         index=False)
        print("amount_greater_than_500_wise.csv created succesfully=========")

    def sum_of_amount_department_wise(self):
        outpatient_details_df = pd.read_csv('../../clean_files/clean_outpatient_details_dump.csv', header=0,
                                            delimiter=',')

        # department group by, sum of amount
        group_by_department = outpatient_details_df.groupby("department").agg({'amount': 'sum'})

        # Export to csv
        group_by_department.to_csv('../../dashboard_files/powerplay/sum_of_amount_department_wise.csv',
                                   encoding='utf-8', index=True)
        print("sum_of_amount_department_wise.csv created succesfully=========")

    def sum_of_amount_status_wise(self):
        outpatient_details_df = pd.read_csv('../../clean_files/clean_outpatient_details_dump.csv', header=0,
                                            delimiter=',')

        # status group by, sum of amount
        group_by_department = outpatient_details_df.groupby("status").agg({'amount': 'sum'})

        # Export to csv
        group_by_department.to_csv('../../dashboard_files/powerplay/sum_of_amount_status_wise.csv', encoding='utf-8',
                                   index=True)
        print("sum_of_amount_status_wise.csv created succesfully=========")


if __name__ == '__main__':
    powerplay_wise_obj = PowerplayDashboard()
    powerplay_wise_obj.latest_50_admit_date_wise()
    powerplay_wise_obj.latest_50_opdate_wise()
    powerplay_wise_obj.amount_greater_than_500_wise()
    powerplay_wise_obj.sum_of_amount_department_wise()
    powerplay_wise_obj.sum_of_amount_status_wise()
