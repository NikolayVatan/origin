import requests
import time


def search(email):
    headers = {
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/77.0.3865.90 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://signin.ea.com/p/originX/create?execution=e39729387s1&initref=https%3A%2F%2Faccounts.ea.'
                   'com%3A443%2Fconnect%2Fauth%3Fresponse'
                   '_type%3Dcode%26client_id%3DORIGIN_SPA_ID%26display%3DoriginXWeb%252Fcreate%26locale%3Dru_'
                   'RU%26release_type%3Dprod%26redirect_'
                   'uri%3Dhttps%253A%252F%252Fwww.origin.com%252Fviews%252Flogin.html',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'requestorId': 'portal',
        'email': email,
        '_': int(time.time() * 1000)
    }

    url = 'https://signin.ea.com/p/ajax/user/checkEmailExisted'
    r = requests.get(url, headers=headers, params=params)
    if 'register_email_existed' in r.text:
        result = {
            'exist': False
        }
    else:
        result = {
            'exist': True
        }

    return r.text, result


if __name__ == '__main__':

