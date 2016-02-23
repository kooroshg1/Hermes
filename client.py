__author__ = 'koorosh'
import httplib
import urllib
import sys


http_server = 'wolverine.cs.wright.edu:8000'
conn = httplib.HTTPConnection(http_server)
# Sending input parameters to the server
params = {'solver': 'PT',
          'wedgeLength': 1.0,
          'wedgeThickness': 0.1}
params = urllib.urlencode(params)
conn.request("POST", http_server, params)
rsp = conn.getresponse()
print(rsp.status)
print(rsp.reason)
print(rsp.read())

# Getting the response back
conn.request("GET", "")
rsp = conn.getresponse()
print(rsp.read())