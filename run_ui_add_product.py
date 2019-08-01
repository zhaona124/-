# -*- coding:utf-8 -*-																		
# Author : 小吴老师                                                                        
# Data ：2019/7/12 7:41
import time

from tools import log_tool
from tools import shell_tool                                                               
from tools import log_tool                                                                 
import pytest                                                                              
                                                                                           
if __name__ == '__main__':
    # 修改成要执行的测试用例                                                               
    test_case = 'test_case/ui/mall/test_mall_add_product.py'
    cur = '{}'.format(time.strftime('%Y%m%d%H%M%S',time.localtime((time.time()))))
    xml_report_path = './reports/xml{}/'.format(cur)
    html_report_path = './reports/html{}/'.format(cur)
                                                                                           
    pytest.main(['-s', '-q', '--alluredir',                                                
                 xml_report_path, test_case])                                              
    cmd1 = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)        
    # cmd2 = 'allure serve %s' % (xml_report_path)
                                                                                           
    shell_tool.invoke(cmd1)                                                                
    # shell_tool.invoke(cmd2)
