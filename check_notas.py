import requests,time,json,re,os,sys,hashlib

USERNAME = ""
PASSWORD = ""
WAITING = 10 #10 minutos

UCS = [
        {'uc':'SO','url':'https://ead.ipleiria.pt/2017-18/course/view.php?id=3659'},
        {'uc':'P2','url':'https://ead.ipleiria.pt/2017-18/course/view.php?id=3711'},
        {'uc':'Dummy','url':'https://ead.ipleiria.pt/2017-18/course/view.php?id=6969'},
        {'uc':'Outra','url':'https://ead.ipleiria.pt/2017-18/course/view.php?id=1234'},
      ]

hashpath = os.path.join(sys.path[0],'hashfiles.dat')
s = requests.Session()

def login():
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'ead.ipleiria.pt',
    'Origin': 'https://ead.ipleiria.pt',
    'Referer': 'https://ead.ipleiria.pt/2017-18/login/index.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

    data = {'username': USERNAME,
            'password': PASSWORD,
            'anchor': ''}

    info = s.post('https://ead.ipleiria.pt/2017-18/login/index.php',headers=headers, data=data).text
    if '<div id="content-wrapper">' in info:
        print("Login OK")
        return True
    else:
        print("Login falhou")
        exit(0)
        #return False

def request_uc(url):
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'ead.ipleiria.pt',
        'Referer': 'https://ead.ipleiria.pt/2017-18/my/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}

    info = s.get(url,headers=headers).text

    if not '<div id="content-wrapper">' in info:
        login()
        info = s.get(url,headers=headers).text

    content = re.compile('<section id="region-main">(.+?)</section>').findall(info.replace('\n','').replace('\r','').replace('\t',''))[0]
    for x in re.compile('<input(.+?)>').findall(content):
        content = content.replace(x,'')
    return hashlib.md5(content.encode('utf-8')).hexdigest()
    
def return_hashfile():
    if os.path.exists(hashpath):
        stream = open(hashpath,'r')
        var = stream.read()
        stream.close()
        return var
    else:
        return '{}'

def save_hashfile(content):
    stream = open(hashpath,'w')
    stream.write(content)
    stream.close()    

if __name__ == "__main__":
    if login():
        while True:
            hashes = json.loads(return_hashfile())
            print("A verificar alterações... ", end = "")
            for x in UCS:
                hash = request_uc(x['url'])
                if x['uc'] in hashes:
                    if hashes[x['uc']] != hash:
                        print("\n>>> Houve alteracoes a " + str(x['uc']) + "!!!")
                hashes[x['uc']] = hash

            save_hashfile(json.dumps(hashes))
            if WAITING < 5:
                print("a aguardar " + str(5) + " minutos")
                time.sleep(5 * 60)
            else:
                print("a aguardar " + str(WAITING) + " minutos")
                time.sleep(WAITING * 60)
