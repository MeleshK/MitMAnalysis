from mitmproxy.net.http.http1.assemble import assemble_request, assemble_response
import os

f = open(os.getcwd() + '/stream.txt', 'w')


def request(flow):
    f.write(assemble_request(flow.request).decode('utf-8'))


def response(flow):
    f.write(assemble_response(flow.response).decode('utf-8', 'replace'))
