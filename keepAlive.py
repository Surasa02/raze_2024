from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return 'เข้าดิสกูกันด้วย\nhttps://discord.gg/adshop'

def run():
  app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
  thred = Thread(target = run)
  thred.start()

# ไม่ต้องแก้ไรนะไอสัส
# discord.gg/adshop
