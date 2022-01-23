import parsers.wattpad_com as wattpad_com
print("Universal parser for eBooks")

url = input("URL> ")
types = input("TYPE> ")

urlsp = url.split("/")
if "wattpad.com" in urlsp[2]:
    wattpad_com.download_story(wattpad_com.get_story_id(url), types)