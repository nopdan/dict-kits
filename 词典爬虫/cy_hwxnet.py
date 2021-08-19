import requests
from lxml import etree
from multiprocessing import Pool, pool

def spider(url):
    r = requests.get(url)
    if r.status_code == '200':
        print(f'{url} is failed!')
        return [""]
    r.encoding = None
    html = etree.HTML(r.text)
    chengyu = html.xpath('//span[@class="peru f14 fw_bold"]/text()')
    pinyin = html.xpath('//span[@class="pinyin f16"]/text()')
    try:
        res = [chengyu[i]+"\t"+pinyin[i] for i in range(len(chengyu))]
        return res
    except:
        print(chengyu,pinyin)
        return [""]

#print(spider("https://cy.hwxnet.com/search.do?qt=1&wd=*&pageno=1"))

if __name__ == "__main__":

    xhy = open("成语_hwxnet.txt", 'w', encoding='utf-8')
    url_prefix = "https://cy.hwxnet.com/search.do?qt=1&wd=*&pageno="
    urlss = []
    #1 4317
    for i in range(86):
        urls = []
        for j in range(1,51):
            the_id = 50 * i + j
            print(the_id)
            urls.append(url_prefix + str(the_id))
        urlss.append(urls)

    urls = []
    for j in range(4301,4318):
        print(j)
        urls.append(url_prefix + str(j))
    urlss.append(urls)
    pool = Pool(processes = 12)
    for i in range(len(urlss)):
        res = pool.map(spider, urlss[i])
        print(i, len(urlss))
        for j in res:
            for k in j:
                xhy.write(k+'\n')
    xhy.close()
    