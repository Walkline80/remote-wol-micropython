"""
The MIT License (MIT)
Copyright © 2021 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/remote-wol-micropython
"""
from utils.utilities import Utilities


class Config(object):
	"""
	硬件配置文件
	"""
	VERSION_0 = "Version0"
	HARDWARE_VERSION = VERSION_0
	HARDWARE_NAME = "Remote WOL v0"

	"""
	# Internet 测试文件设置
	"""
	# 二选一，或者自己指定
	INTERNET_TESTING_URL = "https://walkline.wang/success.html"
	# INTERNET_TESTING_URL = "https://gitee.com/walkline/WeatherStation/raw/master/success.html"

	"""
	# WebSocket 设置
	"""
	WEBSOCKET_PATH = "/control"

	"""
	# AP 热点设置
	"""
	AP_SSID = "wol_{}".format(Utilities.get_chip_id())
	AP_AUTHMODE = 0
	AP_HOST = "192.168.66.1"
	AP_PORT = 80
	AP_ROOTPATH = "/web"
	AP_IFCONFIG = (AP_HOST, "255.255.255.0", AP_HOST, AP_HOST)