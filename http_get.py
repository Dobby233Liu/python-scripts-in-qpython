#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import httplib2
h = httplib2.Http("/sdcard/qpython/tmp/httplib2/")
resp, content = h.request("http://example.org/", "GET")
print(content.decode('utf-8'))
