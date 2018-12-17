# -*- coding: utf-8 -*-
import logging
import sys
import traceback
import time
import config

startup_ts = int(time.time())

def get_app_name(mysql, appid):
    return config.APP_NAME

def get_bundle_id(mysql, appid):
    if appid == config.APPID:
        return config.BUNDLE_ID
    else:
        return None

def get_p12(mysql, sandbox, appid):
    with open(config.P12) as f:
        p12 = f.read()
        return p12, config.P12_SECRET, startup_ts
    
    return None, None, None

def get_pushkit_p12(mysql, appid):
    with open(config.PUSH_KEY) as f:
        p12 = f.read()
        return p12, config.PUSH_KEY_SECRET, startup_ts

    return None, None, None

def get_certificate(mysql, appid):
    return None, None

def get_xg_secret(mysql, appid):
    if appid == config.APPID:    
        return config.XG_ACCESS_ID, config.XG_SECRET_KEY
    else:
        return None, None


def get_mi_key(mysql, appid):
    if appid == config.APPID:
        return config.MI_APPID, config.MI_APP_SECRET
    else:
        return None, None

def get_hw_key(mysql, appid):
    if appid == config.APPID:
        return config.HW_APPID, config.HW_SECRET_KEY
    else:
        return None, None


def get_gcm_key(mysql, appid):
    if appid == config.APPID:
        return config.GCM_SENDER_ID, config.GCM_API_KEY
    else:
        return None, None

#todo add jg_app_key, jg_app_secret
def get_jg_key(mysql, appid):
    if appid == config.APPID:
        return config.JG_APP_KEY, config.JG_APP_SECRET
    else:
        return None, None

# 获取微信公众号id
def get_wx(db, appid):
    return None

def get_ali_key(mysql, appid):
    if appid == config.APPID:
        return config.ALI_ACCESS_KEY_ID, config.ALI_ACCESS_SECRET, config.ALI_APP_KEY
    else:
        return None, None, None
