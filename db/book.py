# -*- coding: utf-8 -*-
from mongoengine import *
from lib import log
import config

connect(config.database['DB'])
class book(Document):
    cfg_id = StringField(default='')
    catalog_id = StringField(default='')
    title = StringField(default='')
    url = StringField(default='')
    introduction = StringField(default='')
    author = StringField(default='')
    total = StringField(default='')
    cls = StringField(default='')
    state = IntField(default=0)

    def insdb(self,dic_dbs):
        book(cfg_id=dic_dbs['cfg_id'], catalog_id=dic_dbs['catalog_id'], title=dic_dbs['title'], url=dic_dbs['url'],
                   author=dic_dbs['author'], total=dic_dbs['total'], cls=dic_dbs['cls'],
                   state=0).save()

    def check_echo(self, db_dic, cfg_id, catalog_id):
        #db_dic['url'] = obj_cfg['site_root'] + obj_cfg['site_cat'] + db_dic['url']
        db_dic['cfg_id'] = cfg_id
        db_dic['catalog_id'] = str(catalog_id)
        result = book.objects(url=db_dic['url'], cfg_id=db_dic['cfg_id']).first()
        if result:
            log.Log.init().info('url[' + db_dic['url'] + '] is echo')
            return True
        else:
            self.insdb(db_dic)
            log.Log.init().info('url is not echo')
            return False

    def read_one(self, cfg_id):
        return book.objects(cfg_id=cfg_id, state=0).first()

    def updata_introduction(self, id, introduction):
        book.objects(id=id).update(introduction=introduction)

    def updata_state_1(self, id):
        book.objects(id=id).update(state=1)