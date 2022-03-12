import os
import shutil

def clear_cache():
    clear_folder = os.getcwd() + "/cache"
    try:
        shutil.rmtree(clear_folder)
    except:
        pass
    os.mkdir(clear_folder)

def gen_parsers():
    import_ex = "import {} as {}\n"
    elif_ex = """    elif domain in {}.conf()["url_list"]:\n        return {}.main(url)\n"""
    elif_exs = """    elif site == {}.conf()["name"]:\n        return {}.search(query)\n"""
    elif_exn = """    dict_site.append("{}")\n"""
    parsers_folder = os.getcwd() + "/parsers"
    list_file = os.listdir(parsers_folder)
    list_file_ready = []
    for one_file in list_file:
        if os.path.isfile(parsers_folder + "/" + one_file):
            list_file_ready.append(one_file.replace(".py", ""))
    text_ready = ""
    for one_pars in list_file_ready:
        text_ready += import_ex.format("parsers."+one_pars, one_pars)
    text_ready += """def url_to_domain(url):\n    if "https://" in url or "http://" in url:\n        return url.split("/")[2]\n    else:\n        return url.split("/")[0]\n\n"""
    text_ready += """def main(url):\n    domain = url_to_domain(url)\n    if domain == "0":\n        return {"code":0, "desce":"Test - ok"}\n"""
    for one_pars in list_file_ready:
        text_ready += elif_ex.format(one_pars, one_pars)
    text_ready += """    else:\n        return {"code":0, "desce":"Site not support"}"""
    text_ready += """\ndef search(query, site):\n    if query == "0":\n        return {"code":0, "desce":"Test - ok"}\n"""
    for one_pars in list_file_ready:
        text_ready += elif_exs.format(one_pars, one_pars)
    text_ready += """    else:\n        return {"code":0, "desce":"Site not support"}"""
    text_ready += """\ndef name_list():\n    dict_site = []\n"""
    for one_pars in list_file_ready:
        text_ready += elif_exn.format(one_pars)
    text_ready += """    return dict_site"""
    file = open("gate_pars.py", "w")
    file.write(text_ready)
    