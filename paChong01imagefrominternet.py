# coding:utf-8
import urllib
import re

#获取需要下载图片的URL
def get_html(url):
    page = urllib.urlopen(url)
    html_code = page.read()
    return html_code

#从指定网址下载图片
def get_image(html_code):
    reg = r'src="(.+?\.jpg)" width'
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
        urllib.urlretrieve(img, '%s.jpg' % x)
        x += 1

print u'-------网页图片抓取-------'
print u'请输入url:',
url = raw_input()
if url:
    pass
else:
    print u'---没有地址输入正在使用默认地址---'
    url = 'http://tieba.baidu.com/p/1753935195'
print u'----------正在获取网页---------'
html_code = get_html(url)
print u'----------正在下载图片---------'
get_image(html_code)
print u'-----------下载成功-----------'
raw_input('Press Enter to exit')