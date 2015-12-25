#coding: utf-8

pattern_1 = '<dd[\s\S]+?<a href="([^\"]+)"[\s]{2}title="[\S]+?">([\S]+?)</a>'
pattern_2 = '<h2><a href="([^\"]+)"  style="">[^<]+</a>'
pattern_3 = '<a href="([^\"]+)" onclick="atarget\(this\)" class="s\sxst">[^\<]+</a>'
pattern_page_4 = '<a href="([^\"]+?)">[\d]+?</a>'
pattern_page_number = '<span title="共[\s]+([\d]+) 页"> /[\s]+[\d]+[\s]+页</span>'

def process_content():
    pass

pattern = {
    'entry': {
        'process': {'first': pattern_1},
    },

    'first': {
        'process': {'second': pattern_2, 'third': pattern_3},
        'is_pages': True,
        'pages_process': pattern_page_4,
        'page_number': pattern_page_number,
        'check_change': None
    },

    'second': {
        'process': {'third': pattern_3}, 
        'is_pages': True,
        'pages_process': pattern_page_4,
        'page_number': pattern_page_number, 
        'check_change': None
    }, 
    'third': {
        'process': {'fourth': process_content}
    },

    'fourth': {
        'process': {'NONE': 'SPIDER_CONTENT'}
    }
}

# wdzj = {
#     'entry': [('first', ), None, False], 
#     'first': [('second', 'third'), '<dd[\s\S]+?<a href="([^\"]+)"[\s]{2}title="[\S]+?">([\S]+?)</a>', True, '<a href="([^\"]+?)">[\d]+?</a>', '<span title="共[\s]+([\d]+) 页"> /[\s]+[\d]+[\s]+页</span>'],
#     'second': [('third', ), '<h2><a href="([^\"]+)"  style="">[^<]+</a>', False, None, None],
#     'third': [(), '<a href="([^\"]+)" onclick="atarget\(this\)" class="s\sxst">[^\<]+</a>', False, None, None]
# }
