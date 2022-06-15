# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/29
# @Author  : MashiroF
# @File    : HT_account.py
# @Software: PyCharm

## 账号管理样本
# {
#     'user':'',        # 备注,必要
#     'CK':'',          # Cookie,必要(建议全部粘贴)
#     'UA':''           # User-Agent,必要
# },

# 导入系统内置包
import os
import sys
import logging

# 配置文件
try:
    from HT_config import downFlag,notifyBlackList,logger
except Exception as error:
    logger.info(f'失败原因:{error}')
    sys.exit(0)


## 账号管理
accounts = [
    {
        'user':'fhk',
        'CK':'source_type=501; TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NTcyNTcyMzg0ODgsImlkIjoiNTc2MjU1OTgiLCJpZGMiOiJzaG91bWluZyIsInRpZCI6IkNqbDY2UU1wRkh5MFduMURrSUNNMEJXNTYzNTdVbVpGYW5uMk5HV2JPQVgxN3FyVU9hRVRmeHhYOEZ4YW96NVRCWmowYnFUdjdrdG5EbHVmS1BlaGFHWTNwbG1UbHVhOVk3OXEwWjlydHBVPSJ9.MEYCIQDLFC2pO7_mTCt6iAXwiJ220dyD7LMKXjJzLmofjJJwLAIhANQNilAwD7ZMHRcdbjVqhGt2hx2qVJI9pmzFvyYwD-2N; ENCODE_TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NTcyNTcyMzg0ODgsImlkIjoiNTc2MjU1OTgiLCJpZGMiOiJzaG91bWluZyIsInRpZCI6IkNqbDY2UU1wRkh5MFduMURrSUNNMEJXNTYzNTdVbVpGYW5uMk5HV2JPQVgxN3FyVU9hRVRmeHhYOEZ4YW96NVRCWmowYnFUdjdrdG5EbHVmS1BlaGFHWTNwbG1UbHVhOVk3OXEwWjlydHBVPSJ9.MEYCIQDLFC2pO7_mTCt6iAXwiJ220dyD7LMKXjJzLmofjJJwLAIhANQNilAwD7ZMHRcdbjVqhGt2hx2qVJI9pmzFvyYwD-2N; s_channel=oppo_appstore; s_version=300606; app_utm={"utm_source":"direct","utm_medium":"direct","utm_campaign":"direct","utm_term":"direct"}; app_param={"model":"TNA-AN00","brand":"HONOR","rom":"EMUI","guid":"","ouid":"","duid":"","udid":"","apid":"","sa_device_id":"7d4334325f2a19ab","romVersion":"MagicUI_6.1.0","apkPkg":"com.oppo.store"}; apkPkg=com.oppo.store; Personalized=1; path=/; section_id=null; scene_id=null; exp_id=null; strategy_id=null; retrieve_id=null; log_id=null; experiment_id=4181_1006_2591_-2133_4663_-4693_3551_-3557_329_1519_-922_23_14_2_2_4_3_3_1_2008_340_1021_-3360_2_2_7_2_2_34_113_-109_103_2_1038_-1001_9_41_2_76_2_37_2556_-107_-1575_-426_4_-2_434_2_3_37_-2_-1_-4_-2_-2_-3_-2_3119_-3123_698_-671_-2_91_283_25_57_1_2753_-2662_683_1_537_-2_-3_2_-5_-1_76_-2_-2_955_-932_896_2_2_5_1_2_58_1_3_2_-8_-2_-3_-1_142_-9_6_2; acw_tc=2760776a16546652535431872ea7c13a3dfd2a2968ab8fcbaab0787b7d87ce; ut=direct; utm_source=direct; utm_medium=direct; utm_campaign=direct; utm_term=direct; sajssdk_2015_cross_new_user=1; memberinfo=%7B%22id%22%3A%2257625598%22%2C%22name%22%3A%22%E5%8F%AA%E6%83%B3%E7%BB%A7%E7%BB%AD%22%2C%22oid%22%3A%22NkRiMnJkaWRrSmJNQVl0UG5xang2UT09%22%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22NkRiMnJkaWRrSmJNQVl0UG5xang2UT09%22%2C%22%24device_id%22%3A%2218141bc0e9a1-0230c5f0cc2287-521a224d-301920-18141bc0e9b401%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22NkRiMnJkaWRrSmJNQVl0UG5xang2UT09%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiI2NDIxNDA5IiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4MTQxYmMzNjliMTQwLTA2Y2Y3Yzg2MDE0M2EyOC01MjFhMjI0ZC0zMDE5MjAtMTgxNDFiYzM2OWM0MjkifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%226421409%22%7D%7D; uc=direct; app_innerutm={"us":"wode","um":"puka","uc":"direct","ut":"direct"}; us=wode; um=puka; sa_distinct_id=7d4334325f2a19ab;',
        'UA':'Mozilla/5.0 (Linux; Android 12; TNA-AN00 Build/HONORTNA-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 oppostore/300606 EMUI/MagicUI_6.1.0 brand/HONOR model/'
    },
    {
        'user':'',
        'CK':'',
        'UA':''
    },
]
try:
    accounts = os.environ["HT_COOKIE"].split("&")
except Exception as error:
    logger.info('请设置cookie')
    sys.exit(0)