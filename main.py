import os
import requests

url = "https://tomoekan.com/8tomoekan-calender/"

text = requests.get(url).text

if "八ﾄﾓ4名" in text and "〇" in text:

    line_token = os.environ["LINE_TOKEN"]
    user_id = os.environ["USER_ID"]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {line_token}"
    }

    data = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": "トモエ館に空きあり！"
            }
        ]
    }

    requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        json=data
    )

    print("LINE送信！")

else:
    print("空きなし")
