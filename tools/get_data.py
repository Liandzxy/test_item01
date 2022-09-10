# 导包

import xlrd

dataList = []
def get_excelData(sheetName,startRow,endRow):
    # 路径
    path = '../data/web用例.xlsx'
    # 打开
    WorkBook = xlrd.open_workbook(path)
    # Sheet_Names = WorkBook.sheet_names()  # 打开表名
    # print(Sheet_Names)

    workSheet = WorkBook.sheet_by_name(sheetName)
    for i in range(startRow,endRow):
        resqBody = workSheet.cell_value(i,7)
        rexpect_result = workSheet.cell_value(i,8)
        url = workSheet.cell_value(i,2)
        status_code = workSheet.cell_value(i,5)
        dataList.append((url,resqBody,rexpect_result,status_code))
    return dataList


if __name__ == '__main__':
    get_excelData()


