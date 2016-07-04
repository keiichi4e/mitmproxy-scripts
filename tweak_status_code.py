def start(context, argv):
    if len(argv) != 4:
        raise ValueError('Usage: mitmproxy|mitmdump -s "tweak_status_code.py PUT /v1/something 500"')
    context.method = argv[1]
    context.api = argv[2]
    context.status_code = argv[3]

def response(context, flow):
    req = flow.request
    res = flow.response
    if req.method == context.method and req.path.count(context.api):
        res.status_code = int(context.status_code)
