# 🔓 UnlockSpy

**UnlockSpy** is a lightweight, stealthy Python tool that sends a WhatsApp notification to the device owner every time the system is unlocked. It’s built for personal security and monitoring, without consuming unnecessary system resources.

---

## 📦 Features

- 🕵️ Silent execution (via `pythonw` or `.pyw`)
- 💬 Sends a WhatsApp message via Twilio API
- 🚀 Automatically triggered when the system is unlocked
- 🧠 No background processes or battery usage
- 🪶 Lightweight and clean
- 💻 Works seamlessly with Windows Task Scheduler

---

## 🧪 Use Case Example

- You leave your laptop at home or office.
- Someone unlocks it (without your knowledge).
- You instantly get a WhatsApp message with timestamp.
- Script exits silently. No trace. No tray icon. No console.

---

## 📁 Project Structure

```bash
UnlockSpy/
├── unlockspy.pyw               # Main script
├── .env                        # Environment variables
├── requirements.txt            # Dependencies
├── README.md                   # You are here :)
└── docs/
    ├── setup_task_scheduler.md     # Task Scheduler steps
    ├── setup_startup_shortcut.md  # Alternative startup method
    └── advanced_usage.md          # Optional: stealth tricks
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/safi-ullah-031/UnlockSpy.git
cd UnlockSpy
```

### 2. Install Dependencies
Use a virtual environment if preferred.

```bash
pip install -r requirements.txt
```

### 3. Setup .env File
Update the .env file in the root directory with the required credentials.
#### Test the script before moving to step 4.


### 4. Configure Task Scheduler
Follow the step-by-step setup here:
```bash
📄 docs/setup_task_scheduler.md
```

### 5. Optional: Auto Run on Startup
If you want UnlockSpy to trigger every time the PC starts, not just unlock:

Use Task Scheduler with "At log on"
Or follow: 
```bash 
docs/setup_startup_shortcut.md
```

---

## 🔐 Security Rules & Ethical Usage
UnlockSpy is powerful. Please use it ethically and legally.

❗ Must Follow:
✅ Use only on your own devices
✅ Inform any users if used on shared systems
✅ Secure your .env file (never share your credentials)
✅ Don’t run on machines without permission
❌ Never use for surveillance or malicious spying
❌ Never upload credentials to GitHub

---

## 📬 Contact

For support, questions, or improvements, feel free to reach out:

- 📧 Email: safiullah@pafiastcommunity.com
- 🐙 GitHub: [Safi-ullah-031](https://github.com/safi-ullah-031)  

---

## 🤝 Contribution

Contributions are welcome!

If you find a bug, have an idea for a new feature, or want to help improve UnlockSpy:

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a pull request

Please ensure your code is clean and follows the existing style.

---

## ⚠️ Disclaimer & Security Notice

UnlockSpy is intended **for educational and personal use only**. You must **own the device** or have **explicit permission** to run this tool.

By using this tool, you agree to the following:

- You are **solely responsible** for how you use this project.
- This software must **not be used for surveillance, stalking, spying**, or any unauthorized tracking.
- Misuse of this tool may be **illegal** in your country or region.
- The creator and contributors are **not liable** for any consequences resulting from misuse.

Please be ethical. Always prioritize **user privacy** and **consent**.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

You are free to:

- ✅ Use this code in personal and commercial projects  
- ✅ Modify and distribute with proper attribution  
- ✅ Learn and build upon it for your own use

**You must not:**

- ❌ Hold the original authors liable for any misuse or damage  
- ❌ Use this software for unauthorized surveillance or malicious activity

Please review the full [LICENSE](LICENSE) file for more details.

