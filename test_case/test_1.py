import unittest
from framework.logger import Logger
import ddt
from framework.login_token import Login_Token
from framework.FindValue import FindValue
from framework.Method import Merhod
from framework.GetExceltolist import GetExceltolist
from framework.WriteExcel import WExcel
import datetime
logger = Logger(logger="Test1").getlog()

GetExceltolist =GetExceltolist()#接口数据列表
#token = Login_Token().login_token()['data']['token']  # 获取登录token
#token = Login_Token().token_() # 获取配置文件中的token
#token=''  #设置token为空


@ddt.ddt
class Test(unittest.TestCase):

    def setUp(self):
        print  ("----------SetUp -----\n")
    def tearDown(self):
        print  ("-----------TearDown----\n")
    @ddt.data(*GetExceltolist.GetExceltolist())
    def test_1(self,data):
        global param
        headers = eval(data["headers"])
        headers.update({"x-api-key":"4bRfkpv7nr9sBNOEa3vkN44iK5Q9vVh99loZSOnJ",'Content-Type': 'application/json;charset=UTF-8'})#添加token到头文件中
        param=data["param"]
        caseId=data["caseID"]
        if caseId=="3":
           param=GlobalVariables.response_data

        #logger.info(data)
        PM = Merhod().merhod(data["url"], data["method"], data["param"], headers, data["testname"],data["teststep"],data["caseID"])
        #logger.info(PM)
        #data["param"]["shipDate"]=datetime.date.today()

        print('测试Excel名称：' + str(data["path_ex"]).split('\\')[-1])
        print('测试项名称：'+str(data["testname"]))
        print('测试步骤：' + str(data["teststep"]))
        print('请求地址：' + (data["url"]))
        print('请求头：' + str(headers))
        print('请求参数：' + str(data["param"]))
        print('请求方式：' + str(data["method"]))
        print('响应时间：'+str(PM["time"]))
        print('响应码：'+str(PM["Status_Code"]))
        print('响应报文：'+ str(PM["Response_Data"]))
        print('断言关键字：'+str(data["expect"]))
        if str(data["expect"]) in str(PM["Response_Data"]):
            result1="通过"
        # if str(caseId) == "3":
        #     GlobalVariables.response_datarequestId = str(PM["Response_Data"])
        #     logger.info(caseId)
        else:
            result1="失败"
        logger.info('《'+str(data["path_ex"].split('\\')[-1])+'》'+('\n')+'接口名称：'+ str(data["testname"]) +('\n')+'测试步骤:'+('\n')
        +str(data["teststep"])+('\n')+'测试执行结果：'+('\n')+'接口测试'+result1+('\n')+'响应时间：' + str(PM["time"]) +'s'+('\n')+'状态码：' + str(PM["Status_Code"]))
        WExcel().WExcel(data["path_ex"],PM,data["expect"],data["row"]+1,data["path_ex"].split('\\')[-1])
        #assertIn(self, member, container, msg=None)
        #str(fvalue) in str(dir_data)
        self.assertIn(str(data["expect"]),str(PM["Response_Data"]))

if __name__=='__main__':

    # unittest.main() # 使用main()直接运行时，将按case的名称顺序执行
    suite=unittest.TestSuite()
    #suite.addTest(Relicl("test_entrance"))# 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    #suite.addTest(Relicl("test_entrance"))
    unittest.TextTestRunner().run(suite)  # 将根据case添加的先后顺序执行
