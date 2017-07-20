#coding:utf-8
import requests
from bs4 import BeautifulSoup


def func():
    doc = '''
    <li>
    <div class="u-cover u-cover-alb3" title="Sgt. Pepper's Lonely Hearts Club Band (Deluxe Edition)">
    <img src="http://p4.music.126.net/h_jUQ8EGXOPDUTjkXv-T8Q==/19053436997882005.jpg?param=120y120"/>
    <a class="msk" href="/album?id=35555092"></a>
    <a class="icon-play f-alpha" data-res-action="play" data-res-id="35555092" data-res-type="19" href="javascript:;" title="播放"></a>
    </div>
    <p class="dec dec-1 f-thide2 f-pre" title="Sgt. Pepper's Lonely Hearts Club Band (Deluxe Edition)">
    <a class="tit s-fc0" href="/album?id=35555092">Sgt. Pepper's Lonely Hearts Club Band (D...</a>
    </p>
    <p><span class="s-fc3">2017.5.26</span></p>
    </li>
    '''
    src = BeautifulSoup(doc,'lxml')
    print src.find('img')['src'],type(src.find('img')['src'])

    s = "The /Beatles With Tony Sheridan: First Recordings /50th Anniversary Edition"
    print s
    # ss = s.replace('/','')#.replace(':', ',')
    # print ss+'.jpg'

    t = ('http://p3.music.126.net/s2X7jekBqCr0XOK8TZT7aw==/653109906943896.jpg',
         u'2011.11.08-The Beatles With Tony Sheridan: First Recordings 50th Anniversary Edition.jpg')
    inlegal_ch = ['\\','/',':','*','?',''',''','<','>','|']
    f_name = t[1]
    for c in inlegal_ch:
        # print c
        f_name = f_name.replace(c,'')
        # print f_name
    # print s.replace('\\','')
    # print s.replace('/','')
    # print s
    sc = requests.get(t[0])
    with open(f_name,'wb') as f:
        f.write(sc.content)

if __name__ == '__main__':
    func()