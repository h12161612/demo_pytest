import html
import os

import pytest

if __name__ == '__main__':
    # pytest.main(["./case/", '-s'])
    report_path = os.path.join(os.getcwd(), 'report/abc.html')
    print('laiba', report_path)
    pytest.main(['-s', f'--html={report_path}'])
