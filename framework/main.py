import tushare as ts

# ts.set_token('your token here')
# pro = ts.pro_api()
pro = ts.pro_api('58cf834df2a4b9a5404f6416248cffa0da78d10e31496385251d7aef')
df = pro.query('ggt_top10', ts_code='00700', start_date='20180701', end_date='20180727')
print(df)