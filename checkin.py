import requests, json, os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]

# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]


# #

def start():
    checkin_url = "https://glados.rocks/api/user/checkin"
    status_url = "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    payload = {
        'token': 'glados.network'
    }
    checkin = requests.post(checkin_url, headers={
        'cookie': cookie,
        'referer': referer,
        'origin': origin,
        'user-agent': useragent,
        'content-type': 'application/json;charset=UTF-8'
    }, data=json.dumps(payload))

    state = requests.get(status_url, headers={
        'cookie': cookie,
        'referer': referer,
        'origin': origin,
        'user-agent': useragent})

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + mess + '，you have ' + time + ' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
