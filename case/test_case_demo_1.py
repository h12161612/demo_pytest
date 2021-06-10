# -*- coding: UTF-8 -*-
import os

import pytest
import requests
import common.get_event_list

host = 'http://127.0.0.1:8000/api'


class TestAllCase:
    # test_case_1 依赖的参数
    path_get_event_list = os.path.join(os.getcwd(), './data/case_get_event_list.scv')
    get = common.get_event_list.GatEventList()
    lis_test_case_1 = get.make_case_data(path_get_event_list)

    @pytest.mark.parametrize('eid,expt', lis_test_case_1)
    def test_case_1(self, eid, expt):
        url = host + '/get_event_list'
        data = {'eid': eid}
        header = {'Content-Type': 'application/json'}
        response = requests.get(url=url, params=data, headers=header)
        i = response.json()
        assert i == expt


# if __name__ == '__main__':
#     pytest.main([__file__, '-s'])
