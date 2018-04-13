# -*- coding: utf-8 -*-
import db, config
from lib.http import Http
from lxml import etree
from lib import log

class Book():
    def Catch(self):
        log.Log.init().info('book.Catch')
        obj_cfg = config.runStatic['obj_cfg']
        obj_catalog = db.catalog().read_one(obj_cfg['id'])
        #obj_cfg = config.runing['obj_cfg']
        if obj_catalog:
            if not config.runing['catalog']:
                config.runing['catalog']['next_count'] = obj_catalog['next_count']
            #config.runing['cfg_id'] = obj_cfg['id']
            #config.runing['coding'] = obj_cfg['coding']
            #config.runing['site_root'] = obj_cfg['site_root']
            sNextpaper = obj_catalog['next_paper']
            iPager = obj_catalog['pager']
            if not sNextpaper:
                sNextpaper = obj_catalog['org_pager'].replace("{pager}", "1")
            resp = Http.Transfer().get(sNextpaper, encoding=obj_cfg['coding'])
            if not resp.abnormity:
                obj_html = etree.HTML(resp.content)
                xp_list_html = obj_html.xpath(config.runMode['filter']['CatchBook']['list'])
                #list_info_book = []
                for obj_html in xp_list_html:
                    dic_info_book = self.__analysis_xpath(etree.tostring(obj_html))
                    is_echo = db.book().check_echo(dic_info_book, obj_cfg['id'], obj_catalog['id'])
                    if is_echo:
                        config.runing['catalog']['next_count'] = config.runing['catalog']['next_count'] - 1
                if config.runMode['filter']['EndPager'] in resp.content \
                        and config.runing['catalog']['next_count'] > 0 \
                        and len(xp_list_html)>0:
                    log.Log.init().info('the next page exists. current next_count:' + str(config.runing['catalog']['next_count']))
                    iPager = iPager + 1
                    sNextpaper = obj_catalog['org_pager'].replace("{pager}", str(iPager))
                    db.catalog().update_nextpage(obj_catalog['id'], iPager, sNextpaper)
                else:
                    db.catalog().update_nextpage(obj_catalog['id'], 1, '', last_pager=sNextpaper)
                    config.runing['catch_select'] = 1
        else:
            # 一切从cfg开始，如果没有cfg的配置信息，下面就无法执行
            log.Log.init().info('cfg nothing')

    def __analysis_xpath(self, sHtml):
        dic_result = {}
        obj_html1 = etree.HTML(sHtml)
        for key, value in config.runMode['filter']['CatchBook']['itme2'].items():
            val = obj_html1.xpath(value['xpath'])
            if val:
                if value['funs']:
                    if value['funs'] == 'title':
                        dic_result[key] = self.__analysis_itme2_title(val[0])
                    if value['funs'] == 'cls':
                        dic_result[key] = self.__analysis_itme2_cls(val[0])
                else:
                    dic_result[key] = val[0]
            else:
                dic_result[key] = ''
        return dic_result

    def __analysis_itme2_title(self, strStr):
        return strStr[:-4]

    def __analysis_itme2_cls(self, strStr):
        return strStr[2:]