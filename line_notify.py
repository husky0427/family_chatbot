import requests

def line_notify():

    token = "iNVSSHBHn6tKkengdgUDUTa2YbUX8sW9xACd0QOqlBO"
    message = "Hello! 這是測試文字123!"

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    requests.post(url=line_url, headers=line_header, data=line_data)






if __name__ == '__main__':
    line_notify()