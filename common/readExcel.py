import xlrd
class readExcel:
    @classmethod
    def excel_to_dict_byName(cls, path, name):
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_name(name)
        nrows = sheet.nrows
        ncols = sheet.ncols
        list = []
        for i in range(1, nrows):
            dict = {}
            for j in range(0, ncols):
                dict[sheet.cell_value(0, j)] = sheet.cell_value(i, j)
            list.append(dict)
        return list