'''
Created by auto_sdk on 2018.03.22
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningGetproductgrouplistRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.getproductgrouplist'
