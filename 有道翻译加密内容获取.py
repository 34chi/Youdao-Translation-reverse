import requests
import hashlib
import time

def md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest().upper()

a = int(time.time() * 1000)  # 当前时间戳（毫秒）
g = 'Vy4EQ1uwPkUoqvcP1nIu6WiAjxFeA3Y3'
d = 'fanyideskweb'
u = 'webfanyi'

def S(e, t):
    return f'client={d}&mysticTime={e}&product={u}&key={t}'

sign_str = S(a, g)
sign_md5 = md5(sign_str)


cookies = {
    'OUTFOX_SEARCH_USER_ID': '2010381122@120.235.166.30',
    'OUTFOX_SEARCH_USER_ID_NCOO': '611384573.2012368',
    'DICT_DOCTRANS_SESSION_ID': 'ZTY0NzE0NTQtZjg3Zi00YWY3LWJmNDgtYjc1ODhmMzRmNDg1',
    '_uetsid': 'ffd6e780414611f0b36d499e73ca0621',
    '_uetvid': 'ffd6e250414611f0a6c739c7f8fab471',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID=2010381122@120.235.166.30; OUTFOX_SEARCH_USER_ID_NCOO=611384573.2012368; DICT_DOCTRANS_SESSION_ID=ZTY0NzE0NTQtZjg3Zi00YWY3LWJmNDgtYjc1ODhmMzRmNDg1; _uetsid=ffd6e780414611f0b36d499e73ca0621; _uetvid=ffd6e250414611f0a6c739c7f8fab471',
}

input_str = input("请输入要翻译的内容: ")
data = {
    'i': input_str,
    'from': 'auto',
    'to': '',
    'useTerm': 'false',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign_md5,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': a,
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}


response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)

print("密文:"+response.text)

