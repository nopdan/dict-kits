import requests
from lxml import etree
from multiprocessing import Pool

def spider(url):
    r = requests.get(url)
    if r.status_code == '200':
        print(f'{url} is failed!')
        return ""
    r.encoding = None
    html = etree.HTML(r.text)
    tables = html.xpath('//td[@colspan="2"]//td/text()')
    try:
        res = tables[1] + '\t' + tables[-1]
        return res
    except:
        print(tables)
        return ""
    #answers = html.xpath('//table[@id="table3"]/text()')[0]
    #res = riddle[4:] + '\t' + answers[3:].replace('；', ' ')
    #print(res)

#print(spider("http://www.20z.com/tool/xiehouyu/?id=1"))

# def get_urls(url):

#     r = requests.get(url)
#     r.encoding = None
#     html = etree.HTML(r.text)
#     urls = html.xpath('//div[@id="AListBox"]/ul/li/a/@href')
#     return ["https:" + url for url in urls]

if __name__ == "__main__":

    xhy = open("歇后语_20z.txt", 'w', encoding='utf-8')
    url_prefix = "http://www.20z.com/tool/xiehouyu/?id="
    urlss = []
    # 1 14033
    for i in range(140):
        urls = []
        for j in range(1,101):
            the_id = 100 * i + j
            urls.append(url_prefix + str(the_id))
        urlss.append(urls)

    urls = []
    for j in range(14001,14033):
        urls.append(url_prefix + str(j))
    urlss.append(urls)
    
    pool = Pool(processes = 12)
    for i in range(len(urlss)):
        res = pool.map(spider, urlss[i])
        print(i, len(urlss))
        for j in res:
            xhy.write(j)
    xhy.close()
    