import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]

# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]

# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]



# 新版Server酱推送
def send_server(title, content):
    server_content = {'text': title, 'desp': content}
    server_url = "https://sctapi.ftqq.com/%s.send" % sckey
    resp = requests.post(server_url, params=server_content)
    print('新版Server酱推送状态码为: %s' % resp.status_code)


if __name__ == '__main__':
    checkinUrl = 'https://glados.rocks/api/user/checkin'
    resp = requests.post(checkinUrl, data={'token': 'glados_network'}, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'},
                         cookies={
                             'Cookie': cookie})
    message = 'GLaDOS梯子签到 : \n\n' + json.loads(resp.text).get('message')
    print(message)
    # Server酱通知
    send_server('Glados签到通知', message)
    # Telegram通知
    # tgPush(message)