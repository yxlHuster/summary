#coding: utf-8

import pycurl
import cStringIO as StringIO

to_str = lambda x: x.encode('utf-8') if isinstance(x, unicode) else x

def http_request(url, data = None, header = {}, timeout = 60):
    c = pycurl.Curl()
    buff = StringIO.StringIO()

    c.setopt(pycurl.URL, to_str(url))
    c.setopt(pycurl.WRITEFUNCTION, buff.write)
    c.setopt(pycurl.FOLLOWLOCATION, True)
    c.setopt(pycurl.MAXREDIRS, 5)
    c.setopt(pycurl.CONNECTTIMEOUT, 30)
    c.setopt(pycurl.TIMEOUT, timeout)
    c.setopt(pycurl.USERAGENT, "Mozilla/4self.0 (compatible; MSIE 6self.0; Windows NT 5self.1; SV1; self.NET CLR 1self.1.4322)")

    if data:
        c.setopt(c.POSTFIELDS, data)

    if header:
        headers = to_str(''.join(['%s: %s' % (k, v) for k, v in header.iteritems()]))
        c.setopt(pycurl.HTTPHEADER, headers)

    try:
        c.perform()
    except:
        return 404, None

    code = c.getinfo(pycurl.HTTP_CODE)
    value = buff.getvalue()
    buff.close()
    return code, value


if __name__ == "__main__":
    code, value = http_request("http://bbs.wdzj.com/forum-2-1.html")
    print code, value
