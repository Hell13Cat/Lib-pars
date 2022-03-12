def conf():
    return {
        "url_list":["test"],
        "name":"test"
    }

def main(url):
    results = {
        "code":1,
        "name":"Test book #1",
        "url":"https://test/1",
        "desc":"Book 1 get in test query",
        "status":"Ongoing",
        "chapters":13,
        "cover":"https://ip1.anime-pictures.net/direct-images/686/6865904b5c59fba6ba7ea48152e52c51.png?if=ANIME-PICTURES.NET_-_741934-1400x1980-virtual+youtuber-hololive-hakui+koyori-dabi+%28dabibubi%29-single-long+hair.png"
    }
    return results

def down_book(url):
    results = {
        "code":1,
        "chapters": [
            {
                "title":"Title 1 articles",
                "text":"<p>Текст</p>"
            },
            {
                "title":"Title 2 articles",
                "text":"<p>Текст</p>"
            }
        ],
        "files":{
            "cover":"433333fd783h648d5346534h5fh8"
        }
    }
    return results

def search(query):
    results = {
        "code":1,
        "count":2,
        "results": [
            {
                "id":1,
                "name":"Test book #1",
                "url":"https://test/1",
                "desc":"Book 1 get in test query",
                "status":"Ongoing",
                "chapters":13,
                "cover":"https://ip1.anime-pictures.net/direct-images/686/6865904b5c59fba6ba7ea48152e52c51.png?if=ANIME-PICTURES.NET_-_741934-1400x1980-virtual+youtuber-hololive-hakui+koyori-dabi+%28dabibubi%29-single-long+hair.png"
            },
            {
                "id":2,
                "name":"Test book #2",
                "url":"https://test/2",
                "desc":"Book 2 get in test query",
                "status":"Break",
                "chapters":12,
                "cover":"https://ip1.anime-pictures.net/direct-images/0f3/0f3100e79f5bcb33c53d7b8474e0041d.jpeg?if=ANIME-PICTURES.NET_-_741948-2480x3508-arknights-beanstalk+%28arknights%29-beanstalk+%28gift+uncompleted%29+%28arknights%29-luomuzhen-single-long+hair.jpeg"
            }
        ]
    }
    return results