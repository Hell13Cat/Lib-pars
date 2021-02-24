import wp
print("Universal parser for eBooks")

url = input("URL> ")
types = input("TYPE> ")

urlsp = url.split("/")
if "wattpad.com" in urlsp[2]:
    wp.download_story(wp.get_story_id(url), types)