# -*- coding: utf-8 -*-
#from db import cfg
import sys, config, db
from lib.common import Json

if __name__ == '__main__':
    #print sys.argv
    args = sys.argv
    if len(args)>1:
        if args[1] == 'start':
            print 'satrt'
            db.cfg().update_state(config.runMode['name'], 1)
        elif args[1] == 'stop':
            print 'stop'
            db.cfg().update_stop(config.runMode['name'], 0)
        elif args[1] == 'config':
            print 'create config'
            name = str(args[2])
            #aa = Json()
            obj_json = Json()
            dic_json = obj_json.readFile2Obj('config/json/cfg/'+name+'.json')
            str_cfg_id = db.cfg().create_cfg(dic_json)
            print 'cfg id:' + str_cfg_id
            ls_json = obj_json.readCatalog2List('config/json/cfg/'+name)
            dic_result = db.catalog().install_list(str_cfg_id, ls_json)
            print dic_result
        else:
            print 'args err'
    else:
        print 'pleace input agrs'
