# coding:UTF-8
import json
import csv

xml_url_template = '''    <url>
        <loc>{}</loc>
    </url>
'''

base_url = 'https://nitncwind.org/'

#
key_list = [
    {
        'key': ''
    },
    {
        'key': 'about'
    },
    {
        'key': 'concerts'
    },
    {
        'key': 'concours/winds'
    },
    {
        'key': 'concours/ensemble'
    },
    {
        'key': 'link'
    },
    {
        'key': 'contact'
    },
    {
        'key': 'news'
    },
    {
        'key': 'news',
        'path': 'news.csv'
    },
    {
        'key': 'concerts',
        'path': 'concerts.csv'
    }
]


# XML書き込み
def outputXml(body):
    with open('sitemap.xml', mode='w') as f:
        f.write(body)


# CSV読み込み
def loadCsv(filename):
    res_body = []
    with open(filename, 'r') as f:
        for line in csv.DictReader(f):
            res_body.append(line)
    return res_body


# ID取得
def getIds(body):
    ids = []
    for b in body:
        ids.append(b['id'])
    return ids


# URL組み立て
def makeUrl(filename, base_url):
    body = loadCsv(filename)
    ids = getIds(body)

    urls = []
    for id in ids:
        urls.append(base_url + id)
    return urls


def main():
    urls = []
    for d in key_list:
        if 'path' in d:
            urls = urls + makeUrl(d['path'], base_url + d['key'] + '/')
        else:
            urls.append(base_url + d['key'])

    xml_url = ''
    for url in urls:
        xml_url += xml_url_template.format(url)

    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="https: www.sitemaps.org schemas sitemap 0.9">\n' + xml_url + '</urlset>\n'

    outputXml(xml_str)


main()
