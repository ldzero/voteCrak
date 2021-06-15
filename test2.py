import requests



def vote(ip,data):
    header = {'User-Agent':'Mozilla/5.1 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'X-Forwarded-For':ip}
    try:
        r = requests.post(url,data=data,headers=header)
        print(r.text)
    except:
        print('err')
        pass

url = 'https://cqqyg.cn/wechatVote/toVoteItem.do'
data = {'voteItemId':'22fa9c92521d42f08414523a392c010e',
        'voteId':'0f7143dafad34dbb9b90828ec380d04b'}

counter = 1
for i in range(1500):
    ip = '10.2.23.'+str(i)
    vote(ip,data)
    print('counter',counter)
    counter+=1
    vote(ip,data)
    print('counter',counter)
    counter+=1

