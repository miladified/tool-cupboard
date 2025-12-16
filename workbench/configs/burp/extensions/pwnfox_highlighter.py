from burp import IBurpExtender, IHttpListener
from java.util import Arrays

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Auto Highlighter for PwnFox")
        callbacks.registerHttpListener(self)
        print("[+] PwnFox Highlighter loaded")

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest:
            return
        request = messageInfo.getRequest()
        analyzed = self._helpers.analyzeRequest(request)
        headers = analyzed.getHeaders()
        color_map = {
            "red": "red",
            "blue": "blue",
            "green": "green",
            "orange": "orange",
            "yellow": "yellow",
            "cyan": "cyan",
            "pink": "pink",
            "gray": "gray",
            "purple": "magenta"
        }
        for header in headers:
            if header.lower().startswith("x-pwnfox-color:"):
                color_value = header.split(":", 1)[1].strip().lower()
                highlight_color = color_map.get(color_value, None)
                if highlight_color:
                    messageInfo.setHighlight(highlight_color)
                    print("[+] Highlighted request as {}".format(highlight_color))
                break