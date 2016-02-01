# mitmproxy-scripts

Scripts for [mitmproxy/mitmdump](https://mitmproxy.org/)

## Delaying a response

```sh
# mitmploxy|mitmdump -s "delay_response.py METHOD PATH SECONDS"
$ mitmproxy -s "delay_response.py GET /v1/something 10"
$ mitmdump -s "delay_response.py GET /v1/something 10"
```

## Tweaking status code of the response

```sh
# mitmploxy|mitmdump -s "tweak_status_code.py METHOD PATH STATUS_CODE"
$ mitmproxy -s "tweak_status_code.py PUT /v1/something 500"
$ mitmdump -s "tweak_status_code.py POST /v1/something 500"
```
