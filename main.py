import os
import requests
from bs4 import BeautifulSoup

url = "https://tomoekan.com/8tomoekan-calender/?ct=1785542400"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")

found = False

for link in links:

    href = link.get("href")

    if not href:
        continue

    # booking-form のリンクだけ見る
    if "booking-form" not in href:
        continue

    # 八ﾄﾓ4名 (6005)
    if "6005" not in href:
        continue

    # 8/22
    if "1787356800" in href:
        found = True


if found:

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
                "text": "8/22 八ﾄﾓ4名に空きあり！"
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
