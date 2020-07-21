#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import base64
import logging

data = {			#下面是打卡数据，没有备注的字段均是未知，字段大部分是拼音首拼
	"jbsks": "否",
	"jbsfl": "否",
	"jbsbs": "否",
	"jbslt": "否",
	"jbsyt": "否",
	"jbsfx": "否",
	"name": "",									#姓名
	"xh": "",									#学号
	"xb": "",									#性别
	"latitude": 29.575339,						#北纬
	"longitude": 106.596929,					#东经
	"locationBig": "中国,重庆市,重庆市,南岸区",	#大区位置
	"locationSmall": "重庆市南岸区石溪路",		#定位
	"lxdh": "13752961731",						#手机号码
	"szdq": "重庆市,重庆市,南岸区",				#现在位置
	"xxdz": "涂山路xxx号",						#现在住址
	"hjsfly": "否",								#坐过飞机(??)
	"ywjchblj": "无",							#有没经过湖北
	"ywjcqzbl": "无",
	"xjzdywqzbl": "无",
	"twsfzc": "是",								#体温是否正常
	"ywytdzz": "无",
	"brsfqz": "无",
	"brsfys": "无",
	"jbs": "无",
	"sfyfy": "无",
	"fyjtgj": "无",
	"fyddsj": "无",
	"sfbgsq": "无",
	"sfjjgl": "无",
	"jjglqssj": "无",
	"wjjglmqqx": "无",
	"beizhu": "无",								#备注
	"qtycqk": "无",
	"timestamp": int(time.time())				#这是时间戳，自动获取不用管
}

def main(*args):

	#下面进行base64编码，构造打卡数据包
	strdata = json.dumps(data,ensure_ascii=False, separators=(',',':'))
	bytes_url = strdata.encode("utf-8")
	str_url = base64.b64encode(bytes_url).decode('ascii')
	post_data = {
		"key": str_url
		}

	#下面构造http头部
	header = {
		"charset": "utf-8",
		"Accept-Encoding": "gzip",
		"referer": "https://servicewechat.com/wx8227f55dc4490f45/52/page-frame.html",
		"content-type": "application/json",
		"User-Agent": "Mozilla/5.0 (Linux; Android 9; STF-TL10 Build/HUAWEISTF-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/WIFI Language/zh_CN Process/appbrand0",
		"Host": "we.cqu.pt"
		}

	#url = "https://we.cqu.pt/api/mrdk/get_mrdk_flag.php" #通过这个地址可以判断今日是否打卡

	url = "https://we.cqu.pt/api/mrdk/post_mrdk_info.php" #这是打卡地址

	try:
		logging.basicConfig(filename="mrdk.log", filemode='a', level=logging.INFO, format="%(asctime)s: %(levelname)s, %(message)s", datefmt="%Y/%d/%m %H:%M:%S")
	except:
		pass

	try:
		response = requests.post(url=url, headers=header, data=json.dumps(post_data))
		logging.info(f'打卡信息（{response.text}）')
	except Exception as e:
		logging.error(f'签到异常，原因为{str(e)}')

main()