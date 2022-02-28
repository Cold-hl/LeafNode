import xlrd
from py2neo import Node, Relationship, Graph
import Make_Neo4J

if __name__ == '__main__':
    xl = xlrd.open_workbook(root)
    table = xl.sheet_by_index(0)
    rowNum = table.nrows  # 行数
    colNum = table.ncols  # 列数
    weapon_list = []

    print(rowNum)
    all_list = []
    for row in range(1, rowNum):
        table.row_values(row)[1]