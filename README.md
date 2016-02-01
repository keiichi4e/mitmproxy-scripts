# mitmproxy-scripts

Scripts for [mitmproxy/mitmdump](https://mitmproxy.org/)

## Delaying a response

```sh
# mitmploxy|mitmdump -s "delay_response.py METHOD PATH SECONDS"
$ mitmproxy -s "delay_response.py GET /v1/something 10"
$ mitmdump -s "delay_response.py GET /v1/something 10"
```
