import parsers.test as test
import parsers.wattpad_com as wattpad_com
def url_to_domain(url):
    if "https://" in url or "http://" in url:
        return url.split("/")[2]
    else:
        return url.split("/")[0]

def main(url):
    domain = url_to_domain(url)
    if domain == "0":
        return {"code":0, "desce":"Test - ok"}
    elif url in test.conf()["url_list"]:
        return test.main(url)
    elif url in wattpad_com.conf()["url_list"]:
        return wattpad_com.main(url)
    else:
        return {"code":0, "desce":"Site not support"}
def search(query, site):
    if query == "0":
        return {"code":0, "desce":"Test - ok"}
    elif site == test.conf()["name"]:
        return test.search(query)
    elif site == wattpad_com.conf()["name"]:
        return wattpad_com.search(query)
    else:
        return {"code":0, "desce":"Site not support"}
def name_list():
    dict_site = []
    dict_site.append("test")
    dict_site.append("wattpad_com")
    return dict_site