# -*- coding: utf-8 -*-
from mongoengine import *
import config

connect(config.database['DB'])
class cfg(Document):
    name = StringField(default='')
    state = IntField(default=0)
    coding = StringField(default='')
    site_root = StringField(default='')
    site_cat = StringField(default='')
    pxy = StringField(default='')

    # 插入单条数据
    def insdb(self, dic_dbs):
        cfg(name=dic_dbs['name'], coding=dic_dbs['coding'], site_root=dic_dbs['site_root'], site_cat=dic_dbs['site_cat'], pxy=dic_dbs['pxy']).save()

    def read_one(self, name):
        return cfg.objects(name=name, state=1).first()

    def update_state(self, name, state=1):
        cfg.objects(name=name).update(state=state)

    def create_cfg(self, data_json):
        obj_cfg = cfg.objects(name=data_json['name']).first()
        if obj_cfg:
            return str(obj_cfg['id'])
        else:
            self.insdb(data_json)
            obj_cfg_id = cfg.objects(name=data_json['name']).first()
            return str(obj_cfg_id['id'])