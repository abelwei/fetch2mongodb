import requests

headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1;  "
                  "Embedded Web Browser from: http://bsalsa.com/; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Accept": "image/gif, image/x-xbitmap, image/jpeg, "
              "image/pjpeg, application/vnd.ms-excel, "
              "application/msword, application/vnd.ms-powerpoint, application/x-shockwave-flash, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-cn",
    "Cache-Control": "no-cache",
}

conn = requests.session()

class Transfer:
    abnormity = False
    abnormity_reason = ''
    content = ''
    code = 0
    def get(self, url, referer="", encoding=""):
        headersAdd = headers
        if referer:
            headersAdd["Referer"] = referer
        resp = conn.get(url,headers=headersAdd)
        if encoding:
            resp.encoding = encoding
        self.content = resp.text
        self.code = resp.status_code
        if self.code != 200:
            self.abnormity = True
            self.abnormity_reason  = resp.reason
        return self

    def test(self, content):
        self.content = content
        return self

    def post(self, url, payload, referer="", encoding=""):
        headersAdd = headers
        if referer:
            headersAdd["Referer"] = referer
        resp = requests.post(url, data=payload, headers=headersAdd)
        if encoding:
            resp.encoding = encoding
        return resp.text

