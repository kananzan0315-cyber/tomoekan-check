import requests

url = "https://tomoekan.com/8tomoekan-calender/"

text = requests.get(url).text

if "八ﾄﾓ4名" in text and "〇" in text:
    print("空きあり！")
else:
    print("空きなし")
