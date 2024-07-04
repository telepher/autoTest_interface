from common.readExcel import readExcel

# db = readExcel.open(r'D:\Desktop\backp\project\autoTest\autoTest_interface\datas.xls')
#
data = readExcel.find_sheet_byName(r'D:\Desktop\backp\project\autoTest\autoTest_interface\datas.xls', '账号登录')
print(data.cell(1,0))
dict = {}
sheet = readExcel.excel_to_dict_byName(r'/datas.xls', '账号登录')
print(sheet)