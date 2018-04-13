# -*- coding: utf-8 -*-
from mongoengine import *
from lib import log
import config

connect(config.database['DB'])
class chapter(Document):
    cfg_id = StringField(default='')
    book_id = StringField(default='')
    title = StringField(default='')
    url = StringField(default='')
    content = StringField(default='')
    state = IntField(default=0)

    # 插入单条数据
    def insdb_url(self,dic_dbs):
        sub = chapter(url=dic_dbs['url'], title=dic_dbs['title'], book_id=dic_dbs['book_id'], cfg_id=dic_dbs['cfg_id'])
        sub.save()


    # 读取数据库中某条信息
    def read_one(self, cfg_id):
        return chapter.objects(cfg_id=cfg_id, state=0).first()

    def update_state_1(self,id,dic_dbs):
        chapter.objects(id=id).update(state=1,content=dic_dbs['content'])

    def update_state(self, id, state):
        chapter.objects(id=id).update(state=state)