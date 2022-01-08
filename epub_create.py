from ebooklib import epub
import base64
import os
from bs4 import BeautifulSoup
import requests
import save_file
from ex import p_red, p_green, p_blue

def chapter_gen(text):
    image = []
    soup = BeautifulSoup(text, 'html5lib')
    tags = soup.find_all('p')
    if len(tags) != 0:
        for span in soup.select('p'):
            if '''data-media-type="image"''' in str(span):
                soupb = BeautifulSoup(text, 'html5lib')
                spanb = soupb.find("img")
                img_tag_url = str(spanb["src"])
                img_name = (img_tag_url.split("/"))[-1] + ".jpg"
                meta = soup.new_tag('image')
                meta.attrs['l:href'] = "#" + img_name
                span.insert_after(meta)
                span.unwrap()
                ufr = requests.get(img_tag_url)
                image.append({"name":img_name, "base":ufr})
    return {"image":image, "text":str(soup).replace("<html><head></head><body>", "").replace("</body></html>", "")}

def m(book):
    p_green("[I] Saving in epub...")
    p_green("[I] Meta and information generation...")
    characters = book["characters"]
    bookr = epub.EpubBook()
    id_gen = "wattpad" + str(book["id"])
    bookr.set_identifier(id_gen)
    bookr.set_title(book["title"])
    bookr.set_language(book["description"])
    bookr.add_author(book["authors"])
    bookr.add_item(epub.EpubNcx())
    bookr.add_item(epub.EpubNav())
    bookr.set_cover("cover.jpg", book["cover"])
    book_spine = ['cover', 'nav']
    p_green("[I] Characters generation...")
    book_characters = []
    count_characters = 1
    for one_char in characters:
        print('[{c_num}/{c_all}] Generation "{chapter_title}": {chapter_id}'.format(c_num=str(count_characters), c_all=str(len(characters) + 1), chapter_title=one_char["title"], chapter_id=one_char["id"]))
        capt = chapter_gen(one_char["text"])
        captr = epub.EpubHtml(title=one_char["title"], file_name='chap_'+str(count_characters)+'.xhtml', lang='hr')
        count_characters += 1
        captr.content = capt["text"]
        book_spine.append(captr)
        book_characters.append(captr)
        bookr.add_item(captr)
    bookr.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
             (epub.Section('Simple book'),
             tuple(book_characters))
            )
    p_green("[I] Saving to epub...")
    save_name = os.getcwd() + "/downloads/" + str(book["id"]) + " - " + save_file.rename_valid_f(book["title"]) + ".epub"
    bookr.spine = book_spine
    epub.write_epub(save_name, bookr, {})
    p_green("[I] Saved to epub")


"""

# create chapter
c1 = epub.EpubHtml(title='Intro', file_name='chap_01.xhtml', lang='hr')


# add chapter
book.add_item(c1)

# define Table Of Contents
book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
             (epub.Section('Simple book'),
             (c1, ))
            )
"""