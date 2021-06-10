import os
import re


class GatEventList:
    def __init__(self):
        pass

    def make_case_data(self, file):
        """
        读取文件并把文件内容转换成 [('login_case_001','admin','123456','0000','login-pass'),(),()
        :param file: 文件地址
        :return:
        """
        with open(file, encoding='utf8') as f:
            contents = f.readlines()  # 按行读取所有内容
        data_li = []  # 声明空列表，用于存放 测试数据
        for i in range(1, len(contents)):  # 剔除第一行
            lin = contents[i].strip().split('*')
            va = eval(lin[1])  # 去掉两头的“” eval的一个巧用
            tup_temp = (lin[0], va)
            # tup_temp = tuple(contents[i].strip().split('*'))
            data_li.append(tup_temp)
        # print('scv---', tup_temp,data_li, sep='\n')
        return data_li

# if __name__ == '__main__':
#     gat = GatEventList()
#     gat.make_case_data(os.path.join(os.getcwd(), '../data/case_get_event_list.scv'))
