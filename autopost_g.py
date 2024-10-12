import csv
import json
import requests as r
from bs4 import BeautifulSoup

# 1. Scraping the quotes from the site:
# response = r.get("https://blog.hubspot.com/sales/famous-quotes")
# data = response.text
# soup = BeautifulSoup(data, "html.parser")
#
# quote_id = soup.find(id="hs_cos_wrapper_post_body")
#
# quotes = quote_id.find_all("p")
# quotes_li = [quotes.getText(strip=True) for quotes in quotes]
#
# print(quotes_li)
#
# with open("data.json", "w") as data:
#     json.dump(quotes_li, data, indent=4)

# 2. Reading Quotes saved in SCV file
with open("quotes.csv", "r", encoding="utf-8") as file:
    quotes = csv.reader(file)
    new_data = []
    for row in quotes:
        new_data.append(row)

# 3. Saving required Quote and delete it
post_quote = new_data[0][1]
del new_data[0]

# 4. Saving the remaining Qoutes to SCV file 'its overwrite the existing file'
with open("quotes.csv", "w", encoding="utf-8", newline="") as new:
    new_file = csv.writer(new)
    new_file.writerows(new_data)
# print(new_data)
# print(post_quote)

# 5. Posting the Saved Quote to LinkedIn
access_token = ""#put your token
url = "https://api.linkedin.com/v2/ugcPosts"
post_json = {
    "author": "urn:li:person:", #put your urn
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": f"{post_quote}"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
    }


post = r.post(url=url, json=post_json, headers=headers)
print(post.json())
#use below code to get your urn code
# info = "https://api.linkedin.com/v2/userinfo"
# userinfo = r.get(info, headers=headers)
# print(userinfo.json())
