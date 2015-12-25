#-*- coding:utf-8 -*

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def stripHTMLTags (html):
    """
       Strip HTML tags from any string and transfrom special entities
    """
    import re
    text = html
 
    # apply rules in given order!
    rules = [
      { r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>' : u' '},
      { r'<\s*style[^>]*>[^<]*<\s*/\s*style\s*>' : u''},
      { r'>\s+' : u'>'},                  # remove spaces after a tag opens or closes
      { r'\s+' : u' '},                   # replace consecutive spaces
      { r'\s*<br\s*/?>\s*' : u'\n'},      # newline after a <br>
      { r'</(div)\s*>\s*' : u'\n'},       # newline after </p> and </div> and <h1/>...
      { r'</(p|h\d)\s*>\s*' : u'\n\n'},   # newline after </p> and </div> and <h1/>...
      { r'<head>.*<\s*(/head|body)[^>]*>' : u'' },     # remove <head> to </head>
      { r'<a\s+href="([^"]+)"[^>]*>.*</a>' : r'\1' },  # show links instead of texts
      { r'[ \t]*<[^<]*?/?>' : u'' },            # remove remaining tags
      { r'^\s+' : u'' }                   # remove spaces at the beginning
    ]
 
    for rule in rules:
        for (k,v) in rule.items():
            regex = re.compile (k, re.M)
            text  = regex.sub (v, text)

    # replace special strings
    special = {
      '&nbsp;' : ' ', '&amp;' : '&', '&quot;' : '"',
      '&lt;'   : '<', '&gt;'  : '>'
    }
 
    for (k,v) in special.items():
        text = text.replace (k, v)
    return text


with open(sys.argv[1]) as f:
    content = f.read()
    print stripHTMLTags(content)
