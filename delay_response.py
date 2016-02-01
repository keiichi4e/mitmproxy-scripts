import time

def start(context, argv):
    if len(argv) != 4:
        raise ValueError('Usage: mitmproxy|mitmdump -s "delay_response.py GET /v1/lists 10"')
    context.method = argv[1]
    context.api = argv[2]
    context.delay = int(argv[3])

def response(context, flow):
    req = flow.request
    if req.method == context.method and req.path.count(context.api):
        context.log("Delaying response of %s for %s second(s)..." % (req.path, context.delay))
        time.sleep(context.delay)
