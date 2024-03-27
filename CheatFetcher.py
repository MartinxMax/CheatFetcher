# S-H4CK13@Maptnh
import requests
from bs4 import BeautifulSoup
import urllib3
import time
import random
from tqdm import tqdm
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logo = '''
 ██████╗██╗  ██╗███████╗ █████╗ ████████╗███████╗███████╗████████╗ ██████╗██╗  ██╗███████╗██████╗
██╔════╝██║  ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
██║     ███████║█████╗  ███████║   ██║   █████╗  █████╗     ██║   ██║     ███████║█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ██╔══██║   ██║   ██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗██║  ██║   ██║   ██║     ███████╗   ██║   ╚██████╗██║  ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
-----------------------------------------------------------------------------------------
                        风灵月影中文修改器快速下载 V1.0                            @Maptnh
-----------------------------------------------------------------------------------------
>>>>>>PS:请勿将该工具用于非法用途,否则自行须承担法律责任,使用该工具则默认同意协议>>>>>>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''


class flingtrainer:

    def __init__(self):
        self.top_link={}

    def run(self):
        choice = 98
        while True:
            if choice == 98:
                result = self.__translation(input("[+] 请输入你所要查询的游戏:"))
                results = self.__query_game(result)
            self.__display_toplink()
            num = int(input("[+] 请输入作弊器页面序号:"))
            print(f'[+] 正在获取[{self.top_link[num]["name"]}] 序号[{num}]作弊器链接...')
            res = self.__second_link(self.top_link[num]['url'])
            while True:
                self.__display_sceond_link(res)
                choice = int(input("[+] 请输入作弊器序号进行下载[输入99返回上一页,输入98重新搜索游戏]:")) or 0
                if choice != 99 and choice !=98:
                    self.__download_file(res[choice-1]['File URL'],res[choice-1]['File Name'])
                else:
                    break


    def __download_file(self, url,name):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://flingtrainer.com/?s=Left+4+Dead",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Te": "trailers"
        }
        response = requests.get(url, headers=headers, verify=False, stream=True)
        if response.status_code == 200:
            file_name = name.split('/')[-1]+'.zip'
            save_path = os.path.join('./Download', file_name)
            total_size = int(response.headers.get('content-length', 0))
            with open(save_path, 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name, ncols=100) as pbar:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
            print(f"[+] 作弊器 '{file_name}' 下载成功! 路径:[./Download]")
        else:
            print(f"[!] 下载失败:{url}. 状态码: {response.status_code}")


    def __display_toplink(self):
        print('-' * 74)
        print('| {:<5} | {:<45} | {:<20} |'.format('序号', '游戏名', 'URL'))
        print('-' * 74)
        for index, (key, value) in enumerate(self.top_link.items(), start=1):
            game_name = value['name']
            url = value['url']
            print('| {:<5} | {:<45} | {:<20} |'.format(index, game_name, url))
        print('-' * 74)


    def __display_sceond_link(self, info):
        print('-' * 98)
        print('| {:<5} | {:<45} | {:<45} | {:<8} | {:<12} |'.format('序号', '修改器', '地址', '文件大小', '下载次数'))
        print('-' * 98)
        for i, item in enumerate(info, 1):
            file_name = item['File Name']
            file_url = item['File URL']
            file_size = item['Size']
            download_count = item['Download Count']
            print('| {:<5} | {:<45} | {:<45} | {:<8} | {:<12} |'.format(i, file_name, file_url, file_size, download_count))
        print('-' * 98)


    def __second_link(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://flingtrainer.com/?s=Left+4+Dead",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Te": "trailers"
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            rows = soup.find_all('tr', class_='zip')
            results = []
            for row in rows:
                file_name = row.select_one('td.attachment-title a').text.strip()
                file_date = row.select_one('td.attachment-date').text.strip()
                file_size = row.select_one('td.attachment-size').text.strip()
                download_count = row.select_one('td.attachment-downloads').text.strip()
                file_url = row.select_one('td.attachment-title a')['href']  # 提取地址
                results.append({
                    'File Name': file_name,
                    'Date': file_date,
                    'Size': file_size,
                    'Download Count': download_count,
                    'File URL': file_url.rstrip(',')
                })

            return results
        else:
            print(f"Request failed with status code: {response.status_code}")


    def __query_game(self,name):
        url = f"https://flingtrainer.com/?s={name}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Te": "trailers"
        }

        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_elements = soup.select("html > body > div:nth-of-type(1) > div > div > div > div:nth-of-type(3) > div:nth-of-type(1) > article")
            print(f"[+] 搜索到:{len(article_elements)}个结果..")
            results = {}
            for idx, article in tqdm(enumerate(article_elements, start=1), total=len(article_elements), desc="[*] 1数据处理", unit="载入"):
                target_element = article.select_one("div:nth-of-type(2) > h2 > a")
                if target_element:
                    name = self.__translation(target_element.get_text(),1) or '???'
                    url = target_element.get('href')
                    results[idx] = {'name': name, 'url': url}
                else:
                    print(f"[!] 没有找到索引:{idx}.")

            self.top_link=results
            return results
        else:
            print(f"[!] 服务端请求失败,返回码: {response.status_code}")
            return None


    def __translation(self, query, en_zh=0):
        time.sleep(random.randint(1, 3))
        url = f"https://fanyi.so.com/index/search?eng={en_zh}&validate=&ignore_trans=0&query={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://fanyi.so.com/?src=onebox",
            "Pro": "fanyi",
            "Origin": "https://fanyi.so.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Content-Length": "0",
            "Te": "trailers"
        }
        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()
            return response.json()['data']['fanyi']
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return False

# 示例用法
if __name__ == '__main__':
    print(logo)
    flingtrainer().run()


