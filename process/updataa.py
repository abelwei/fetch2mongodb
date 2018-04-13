# -*- coding: utf-8 -*-
import config
from lib.http import Http
from lxml import etree
from lib import log
from db import listt

class Updataa():
    def Catch(self):
        print 'updataa.Catch'
        obj_list = listt().read_one(config.runing['cfg_id'])
        if obj_list:
            log.Log.init().info('catch in:'+obj_list['url'])
            resp = Http.Transfer().get(obj_list['url'], encoding=config.runing['coding'])
            if not resp.abnormity:
                print resp.content
        else:
            log.Log.init().info('list in nothin')