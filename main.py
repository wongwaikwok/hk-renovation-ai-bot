from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

ACCESS_TOKEN = "EAF4oSC2lvcYBRIFZAZAV2ZA1RpEkkmkHvDdeJOxqxRfMU3EnsD8hWiwjwDjJWHCyFsnREEGCAMqFSdKGltoZB2HoDEiSG7d0qwNqn8ya36zLAZApwE88oGge6aVJpZBFx6cyFis8yY12gNDOA9XZB4nvFFa37wU4F9vwtIByCyCBkLWPqfCBswqJaXjQ2cL4ylPizwPYhb0QPob4C7FDHZCsXkk3RLgpFlbzL9mQ7nYMtSnAVVoZD"
PHONE_NUMBER_ID = "1092262440626421"
VERIFY_TOKEN = "mysecret2026"

def send_reply(to_number, text):
    url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {"body": text}
    }
    requests.post(url, json=payload, headers=headers)

@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid token", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        message = data['entry'][0]['changes'][0]['value']['messages'][0]
        from_number = message['from']
        user_text = message.get('text', {}).get('body', '（語音或圖片）')

        reply = f"""🛒 香港裝修AI採購平台
AI採購單已生成 (3秒完成)

材料 | 數量 | 單位 | 備註
水泥 | 50 | 包 | 
沙 | 10 | 噸 | 

確認請回覆「確認」或修改材料。"""

        send_reply(from_number, reply)
    except:
        pass
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
