# -*- coding: utf-8 -*-
from db import cfg
from process import book, chapter, files
import config, time
from lib import log

if __name__ == '__main__':
    print 'start'

    #for i in range(1):
    while True:
        obj_cfg = cfg().read_one(config.runMode['name'])
        if obj_cfg:
            if not config.runStatic['obj_cfg']:
                config.runStatic['obj_cfg'] = obj_cfg
                config.runStatic['obj_cfg']['id'] = str(obj_cfg['id'])
            #print config.runStatic['obj_cfg']['id']
            #exit(0)

            if obj_cfg['state'] == 1:
                if config.runing['catch_select'] == 0:
                    book.Book().Catch()
                elif  config.runing['catch_select'] == 1:
                    chapter.Chapter().Catch()
                elif  config.runing['catch_select'] == 2:
                    files.Files().Catch()
                elif config.runing['catch_select'] == 3:
                    log.Log.init().fatal('main was end, will be exit.')
                    exit(0)
        else:
            log.Log.init().warn('main was stopping')
        time.sleep(config.runMode['timer'])


