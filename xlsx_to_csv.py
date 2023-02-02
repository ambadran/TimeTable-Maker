import pandas as pd
data_xls = pd.read_excel('UG-SCHEDULE-FALL20 (1).xlsx', 'Schedule', index_col=None)
data_xls.to_csv('main_timetable.csv', encoding='utf-8')