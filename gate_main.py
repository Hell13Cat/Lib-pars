import webbrowser
import gen_data
gen_data.gen_parsers()
gen_data.clear_cache()
import gate_pars

def update():
    pass

def go_git():
    url = "https://github.com/Hell13Cat/book-parsers"
    webbrowser.open(url, new=2, autoraise=True)

def get_info_book(url):
    return gate_pars.main(url)

def down(url):
    return gate_pars.down_book(url)

def search_books(query, site):
    return gate_pars.search(query, site)

def list():
    return gate_pars.name_list()