# -*- coding: utf-8 -*-
import db, config
from lib.http import Http
from lxml import etree
from lib import log

class Chapter():

    def Catch(self):
        log.Log.init().info('chapter.Catch')
        obj_cfg = config.runStatic['obj_cfg']
        obj_book = db.book().read_one(obj_cfg['id'])
        if obj_book:
            log.Log.init().info(obj_book['url'])
            resp = Http.Transfer().get(obj_book['url'], encoding=obj_cfg['coding'])
            if not resp.abnormity:
                obj_html = etree.HTML(resp.content)
                xp_html_introduction = obj_html.xpath(config.runMode['filter']['CatchChapterList']['introduction'])
                if xp_html_introduction:
                    db.book().updata_introduction(obj_book['id'], xp_html_introduction[0])
                xp_html_list = obj_html.xpath(config.runMode['filter']['CatchChapterList']['list'])
                for fi_html_list in xp_html_list:
                    dic_db = self.__analysis_xpath(etree.tostring(fi_html_list))
                    dic_db['cfg_id'] = obj_cfg['id']
                    dic_db['book_id'] = str(obj_book['id'])
                    dic_db['url'] = obj_book['url'] + dic_db['url']
                    db.chapter().insdb_url(dic_db)
                db.book().updata_state_1(obj_book['id'])
                log.Log.init().info('this book\'s chapters is done, will be next book')
            else:
                log.Log.init().warn(resp.abnormity_reason)
        else:
            log.Log.init().info('these books is nothing, will be next')
            config.runing['catch_select'] = 2

    def __analysis_xpath(self, sHtml):
        dic_result = {}
        obj_html1 = etree.HTML(sHtml)
        for key, value in config.runMode['filter']['CatchChapterList']['itme'].items():
            val = obj_html1.xpath(value)
            #print val
            if val:
                dic_result[key] = val[0]
            else:
                dic_result[key] = ''
        return dic_result