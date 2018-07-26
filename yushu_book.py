from http import Http


class YuShuBook:
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        # 返回result为json格式的dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        # url = cls.isbn_url.format(keyword, cls.per_page, (page-1)*cls.per_page)
        result = Http.get(url)
        return result
