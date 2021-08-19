import requests
from lxml import etree
from multiprocessing import Pool

def spider(url):

    r = requests.get(url)
    r.encoding = None
    html = etree.HTML(r.text)
    riddle = html.xpath('//h1[@id="question"]/text()')[0]
    answers = html.xpath('//h2[@id="answer"]/text()')[0]
    res = riddle[4:] + '\t' + answers[3:].replace('；', ' ')
    print(res)
    return res

# print(spider("https://www.diyifanwen.com/tool/xhy/194454.html"))

def get_urls(url):

    r = requests.get(url)
    r.encoding = None
    html = etree.HTML(r.text)
    urls = html.xpath('//div[@id="AListBox"]/ul/li/a/@href')
    return ["https:" + url for url in urls]

if __name__ == "__main__":

    xhy = open("歇后语_diyifanwen.txt", 'w', encoding='utf-8')
    url_prefix = "https://www.diyifanwen.com/tool/xhy/"
    table_urls = [url_prefix]
    for i in range(2,41):
        table_urls.append(f'{url_prefix}index_{i}.html')
    pool = Pool(processes = 12)
    urls = pool.map(get_urls, table_urls)
    print(urls[30])
    for a in urls:
        pool = Pool(processes = 12)
        res = pool.map(spider, a)
        # print(res)
        for i in res:
            xhy.write(i+'\n')
    xhy.close()
    