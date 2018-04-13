# -*- coding: utf-8 -*-
import db, config
from lib.http import Http
from lxml import etree
from lib import log

class Listt():

    def Catch(self):
        print 'listt.Catch'
        obj_cfg = db.cfg().read_one(config.runMode['name'])
        if obj_cfg:
            config.runing['cfg_id'] = obj_cfg['id']
            config.runing['coding'] = obj_cfg['coding']
            sNextpaper = obj_cfg['next_paper']
            iPager = obj_cfg['pager']
            if not sNextpaper:
                sNextpaper = obj_cfg['org_pager'].replace("{pager}", "1")
            resp = Http.Transfer().get(sNextpaper, encoding=config.runing['coding'])
            if not resp.abnormity:
                obj_html = etree.HTML(resp.content)
                xp_html = obj_html.xpath(config.runMode['filter']['CatchList'])
                for link in xp_html:
                    db.listt().check_echo(link, obj_cfg)
                    #print link
                if config.runMode['filter']['EndPager'] in resp.content and obj_cfg['next_count'] > 0:
                    log.Log.init().info('the next page exists')
                    iPager = iPager + 1
                    sNextpaper = obj_cfg['org_pager'].replace("{pager}", str(iPager))
                    db.cfg().update_nextpage(obj_cfg['id'], iPager, sNextpaper)
                else:
                    db.cfg().update_nextpage(obj_cfg['id'], 1, '', last_pager=sNextpaper)
                    config.runing['catch_select'] = 1
        else:
            #一切从cfg开始，如果没有cfg的配置信息，正面
            log.Log.init().info('cfg nothing')
