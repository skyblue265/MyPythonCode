  
import requests
import sys

def lineNotifyMessage(token, msg, url):
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
	
      payload = {'message': msg,  'imageThumbnail': url,'imageFullsize': url}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
      return r.status_code
	
# 修改為你要傳送的訊息內容
#message = sys.argv[1]
#url = sys.argv[2]
month=5
date=6
time=1100
if time>1200:
    for i in range(1,10)
        message = "today is "+str(month)+"/"+str(date)+"晚安"
else:
    message = "today is "+str(month)+"/"+str(date)+"早安"
    
url = "https://pic3.zhimg.com/v2-274f834fdf2b1efda98319f56bf29d8a_b.jpg"

# 修改為你的權杖內容
token = 'SPDHPvqyJIlsAcW8YdTvCxVq0vDXsxjJccAH3MQL2zC'

lineNotifyMessage(token, message, url)