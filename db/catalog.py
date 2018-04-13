# -*- coding: utf-8 -*-
from mongoengine import *
#from lib import log
import config

connect(config.database['DB'])
class catalog(Document):
    cfg_id = StringField(default='')
    next_paper = StringField(default='')
    pager = IntField(default=0)
    org_pager = StringField(default='')
    state = IntField(default=0)
    last_pager = StringField(default='')
    next_count = IntField(default=0)

    # 插入单条数据
    def insdb(self, dic_dbs):
        sub = catalog(cfg_id=dic_dbs['cfg_id'],
                      next_paper=dic_dbs['next_paper'],
                      pager=dic_dbs['pager'],
                      org_pager=dic_dbs['org_pager'],
                      state=dic_dbs['state'],
                      last_pager=dic_dbs['last_pager'],
                      next_count=dic_dbs['next_count'])
        sub.save()

    def read_one(self, cfg_id):
        return catalog.objects(cfg_id=cfg_id, state=1).first()

    def update_nextpage(self, id, pager, nextpage, last_pager=''):
        catalog.objects(id=id).update(pager=pager,next_paper=nextpage, last_pager=last_pager)

    def check_echo(self, cfg_id, obj_json):
        result = catalog.objects(cfg_id=cfg_id, org_pager=obj_json['org_pager']).first()
        if result:
            return True
        else:
            obj_json['cfg_id'] = cfg_id
            self.insdb(obj_json)
            return False

    def install_list(self, cfg_id, ls_json):
        dicRsult = {'echo':0, 'no':0}
        for rf_josn in ls_json:
            isEcho = self.check_echo(cfg_id, rf_josn)
            if isEcho:
                dicRsult['echo'] = dicRsult['echo'] + 1
            else:
                dicRsult['no'] = dicRsult['no'] + 1
        return dicRsult