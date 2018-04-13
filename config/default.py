# -*- coding: utf-8 -*-
test = '666'
database = {'type':'MONGODB', 'DB':'fetch2mongodb',}
runMode = {
    'name':'ybducom',
    'ignore':{
        'http_error':[404],
    },
    'filter':{
        'CatchList':"",
        'EndPager':'class="next">&gt;</a>',
        'CatchUpdata':'',
        'CatchBook':{
            'list':"//div[@class='clearfix rec_rullist']/ul",
            'itme2':{
                'url':{
                    'xpath':"//ul/li[@class='two']/a/@href",
                    'funs':"",
                },
                'title':{
                    'xpath':"//ul/li[@class='two']/a/text()",
                    'funs':"title",
                },
                'author':{
                    'xpath':"//ul/li[@class='four']/text()",
                    'funs':"",
                },
                'total':{
                    'xpath':"//ul/li[@class='five']/text()",
                    'funs':"",
                },
                'cls':{
                    'xpath':"//ul/li[@class='sev']/*/a/text()",
                    'funs':"cls",
                },
            },
        },
        'CatchChapterList':{
            'introduction':"//div[@class='mu_contain']/p/text()",
            'list':"//ul[@class='mulu_list']/li/a",
            'itme':{
                'url':"//a/@href",
                'title':"//a/text()",
            },
        },
        'CatchChapterContent':{
            'itme4':{
                'content':{
                    'xpath':"//div[@id='htmlContent']",
                    'remove':["//div[@class='ad00']","//div[@class='chapter_Turnpage']",],
                },
            },
        },
    },
    'timer':2,
}

runing= {
    'catch_select':0,
    'catalog':{},
    'ignore':{
        'http_err':10
    },
}

runStatic = {
    'obj_cfg':{},
    'obj_cfg_hide':{
        'cfg_id':'5a9630adac6a31576ab5df80',
        'coding':'gbk',
        'site_root':'',
        'next_count':100,
    }
}
