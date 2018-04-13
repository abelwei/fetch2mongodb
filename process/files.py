# -*- coding: utf-8 -*-
import db, config, re
from lib.http import Http
from lxml import etree
from lib import log


class Files():

    def Catch(self):
        log.Log.init().info('files.Catch')
        obj_cfg = config.runStatic['obj_cfg']
        obj_chapter = db.chapter().read_one(obj_cfg['id'])
        if obj_chapter:
            log.Log.init().info(obj_chapter['url'])
            resp = Http.Transfer().get(obj_chapter['url'], encoding=obj_cfg['coding'])
            if not resp.abnormity:
                #obj_html = etree.HTML(resp.content)
                #xp_html_list = obj_html.xpath(config.runMode['filter']['CatchChapterContent']['content'])
                dic_db = self.__analysis_xpath(resp.content)
                #print dic_db
                db.chapter().update_state_1(obj_chapter['id'], dic_db)
            else:
                if self.__ignore_http_err(resp.code):
                    db.chapter().update_state(obj_chapter['id'], resp.code)
                    log.Log.init().warn('ignore http error, this code:' + str(resp.code) + ', text:' + resp.abnormity_reason)
                    config.runing['ignore']['http_err'] = config.runing['ignore']['http_err'] - 1
                    if config.runing['ignore']['http_err'] < 0:
                        raise Exception("http error ignore times has been used up")
                else:
                    raise Exception("http error, code :" + str(resp.code))
        else:
            db.cfg().update_state(obj_cfg['id'], state=2)
            log.Log.init().info('these files is nothing, will be next')
            config.runing['catch_select'] = 3

    def __analysis_xpath___(self, sHtml):
        dic_result = {}
        obj_html1 = etree.HTML(sHtml)
        for bad in obj_html1.xpath("//div[@class='ad00']"):
            bad.getparent().remove(bad)
        print etree.tostring(obj_html1)
        return dic_result

    def __analysis_xpath(self, sHtml):
        dic_result = {}
        obj_html1 = etree.HTML(sHtml)
        dic_result = self.__analysis_item4(obj_html1)

        return dic_result

    def __analysis_item4(self, obj_html1):
        dic_result = {}
        config_itme = config.runMode['filter']['CatchChapterContent']['itme4']
        #xp_content = obj_html1.xpath(config_itme4['content']['xpath'])
        for fr_remove in config_itme['content']['remove']:
            #xp_remove = obj_html1.xpath(fr_remove)
            for bad in obj_html1.xpath(fr_remove):
                bad.getparent().remove(bad)
        xp_content = obj_html1.xpath(config_itme['content']['xpath'])
        #print xp_content[0].xpath('string(.)')
        str_content = ''
        if len(xp_content)>0:
            str_content = etree.tostring(xp_content[0])
        dic_result['content'] = self.__analysis_text(str_content.replace('<br />', "\n"))
        return dic_result

    def __analysis_text(self, strHtml):
        obj_html1 = etree.HTML(strHtml)
        xp_content = obj_html1.xpath('//text()')
        if len(xp_content)>0:
            return xp_content[0]
        else:
            log.Log.init().fatal('can\'t get content.')
            exit(0)

    def __ignore_http_err(self, err_code):
        for rf_ignore in config.runMode['ignore']['http_error']:
            if err_code == rf_ignore:
                return True
        return False
