import requests
import re
import random
import telebot
class Sin:
	def __init__(self):
		self.TOKEN=input('TOKEN : ')
		self.id=input('ID : ')
		self.bot=telebot.TeleBot(self.TOKEN)
	def COODE(self):
		while True:
			sin = "".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890.') for i in range(random.randint(6, 11))) + random.choice(['@gmail.com', '@hotmail.com'])
			url = "https://www.ulayers.com/wp-admin/admin-ajax.php"
			payload = f"action=couponwheel_wheel_run&form_data=email%3D{sin}%26first_name%3DJsjsjss%26wheel_hash%3D77a1b4&preview_key=false"
			headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    'sec-ch-ua-platform': "\"Android\"",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'sec-ch-ua-mobile': "?1",
    'origin': "https://www.ulayers.com",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://www.ulayers.com/video-services/",
    'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
}
			try:
				response = requests.post(url, data=payload, headers=headers).json()
				couponcode= response.get('notice')
				MAS= re.search(r'"couponcode_raw":"(.*?)"', couponcode)
				MM=re.search(r'<div id="couponwheel_notice_escaper">(.*?)</div>',couponcode,re.DOTALL)
				co=MAS.group(1)
				end = MM.group(1)
				print("تم صيد كود ", co)
				print("مده انتهاء الصلاحيه",end)
				
				self.bot.send_message(chat_id=self.id,text=f'''
•••••••••••••••••••: 
CODE : {co}  «~~ هذا الكود 
•••••••••••••••••••
Expiration : {end}
••••••••••••••••••• : 
♕ PY : @ebn_elnegm

			
				''')
			except:
				print('BAD')				
XX=Sin()
XX.COODE()			 	
