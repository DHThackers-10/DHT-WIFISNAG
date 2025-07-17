# DHT-WIFISNAG  
![DHT-HACKERS](https://img.shields.io/badge/DHT-HACKERS-magenta?style=for-the-badge) 

The ultimate WiFi Credential Snagging Tool designed for testing Wi-Fi network authentication and password capturing in a stealthy and pro style — wrapped in a Rich UI with pyfiglet banners and clean console logging.  
  
  
---  
  
# 🎯 DHT-WIFISNAG – Snag WiFi Like a Pro  
  
Welcome to DHT-WIFISNAG, your go-to tool for capturing Wi-Fi passwords through a realistic fake login portal. Built with Flask, Rich, and pyfiglet, this tool offers a polished UI and logs every captured password with timestamp, IP, and user-agent for maximum clarity.  
  
  
---  
  
# ⚠️ Disclaimer  
  
> This tool is meant for educational & authorized testing only.  
Do NOT use this on networks without explicit permission.  
The author holds no responsibility for any illegal misuse.  
  
  
  
  
---  
  
# 🚀 Installation Guide  
  
Install on Termux or Linux:  
```
apt update && apt upgrade -y  
pkg install python git -y  
pip install flask rich pyfiglet  
git clone https://github.com/DHThackers-10/DHT-WIFISNAG.git  
cd DHT-WIFISNAG  
python3 DHT_WIFISNAG.py  
```  
  
---  
  
# 🖥️ Screenshots  
  
> Terminal Banner + Intro Panel + Fake Wi-Fi Login Page UI  
  
  ![Screenshot_20250717-142006](https://github.com/user-attachments/assets/e0f7e7fb-c698-447c-a4be-602fdf328e5c)
![Screenshot_20250717-142038](https://github.com/user-attachments/assets/cb869858-9f39-4c13-8619-3b7f894e828b)  
   
---  
  
# ⚙️ Features  
  
✅ Realistic fake Wi-Fi password prompt with spinner animation  
✅ Terminal banner and rich panels with DHT branding  
✅ Logs captured passwords with timestamp, IP address & user-agent  
✅ Auto opens YouTube subscribe page on Termux before running  
✅ Clean, colorful console output using Rich and pyfiglet  
✅ Easy deployment with Flask, works on Termux and Linux  
✅ Supports cloudflared tunnel for public URL phishing  
✅ Lightweight and beginner-friendly codebase  
  
  
---  
  
# 🔧 How It Works  
  
1. Run the tool, watch the DHT-branded banner and intro panel  
  
  
2. It opens the official DHT Hackers YouTube for subscription  
  
  
3. Flask server starts and serves the fake Wi-Fi login page  
  
  
4. Target visits the URL, sees the legit-looking login prompt  
  
  
5. When password submitted, it’s logged with IP & user-agent info  
  
  
6. Terminal shows the logs live with neat timestamps and colors  
  
  
7. Use cloudflared tunnel to get public URL for remote targets  
  
  
  
  
---  
  
# 📂 Log File Example  
  
.dht_logs/wifi_passwords.log  
  
[2025-07-17 19:45:12] [IP: 192.168.1.5] [Agent: Mozilla/5.0 ...] Captured Password: mywifi123  
[2025-07-17 19:46:33] [IP: 192.168.1.6] [Agent: Mozilla/5.0 ...] Captured Password: letmein!  
...  
  
  
---  
  
# 🌐 Educational Use Only  
  
This tool is strictly for educational awareness, security testing, and authorized pen-testing only.  
Never use it to exploit networks you do not have explicit permission to test.  
  
  
---  

# 👨‍💻 Credits

**Author:** Ali Sabri – DHT Hackers  
**GitHub:** [DHThackers-10](https://github.com/DHThackers-10)  
**YouTube:** [DHT Hackers](https://youtube.com/@dht-hackers_10)  
**WhatsApp Community:** [Join Group](https://chat.whatsapp.com/G2hCkCzylra2OENEfhH8Os)
  
---  
  
# 💡 More DHT Tools  
  
> Try these fire scripts too:  
  
  
  
DHT-SOCIALKIT — All-in-One Brute + Phishing  
  
DHT-BGMI-PHISH — BGMI Phishing Tool  
  
DHT-PHISHER — Phishing Engine Generator  
  
  
Browse them all here: github.com/DHThackers-10
