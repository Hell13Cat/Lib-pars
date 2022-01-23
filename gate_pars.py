import parsers.wattpad_com as wattpad_com
def url_to_domain(url):
    if "https://" in url or "http://" in url:
        return url.split("/")[2]
    else:
        return url.split("/")[0]

def main(url):
    domain = url_to_domain(url)
    if domain == "0":
        return {"code":0, "desc":"Test - ok"}
    elif url in wattpad_com.conf()["url_list"]:
        return wattpad_com.main(url)
    else:
        return {"code":0, "desc":"Site not support"}