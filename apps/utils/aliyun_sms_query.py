# -*- coding: utf-8 -*-
# import sys
# from importlib import reload
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from .aliyun_sms_const import ACCESS_KEY_ID, ACCESS_KEY_SECRET

"""
短信业务调用接口示例，版本号：v20170525

Created on 2017-06-12

"""
# try:
#     reload(sys)
#     sys.setdefaultencoding('utf8')
# except NameError:
#     pass
# except Exception as err:
#     raise err

# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)

def query_send_detail(biz_id, phone_number, page_size, current_page, send_date):
    queryRequest = QuerySendDetailsRequest.QuerySendDetailsRequest()
    # 查询的手机号码
    queryRequest.set_PhoneNumber(phone_number)
    # 可选 - 流水号
    queryRequest.set_BizId(biz_id)
    # 必填 - 发送日期 支持30天内记录查询，格式yyyyMMdd
    queryRequest.set_SendDate(send_date)
    # 必填-当前页码从1开始计数
    queryRequest.set_CurrentPage(current_page)
    # 必填-页大小
    queryRequest.set_PageSize(page_size)
	
	# 数据提交方式
	# queryRequest.set_method(MT.POST)
	
	# 数据提交格式
    # queryRequest.set_accept_format(FT.JSON)

    # 调用短信记录查询接口，返回json
    queryResponse = acs_client.do_action_with_exception(queryRequest)

    # TODO 业务处理

    return queryResponse


if __name__ == '__main__':
    print(query_send_detail("141324518542671592^0", "13000000000", 10, 1, "20180214"))
