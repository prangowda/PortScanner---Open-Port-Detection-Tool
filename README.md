# PortScanner - Open Port Detection Tool

## 🔍 Project Description
PortScanner is a **Python-based tool** that scans **open ports on a system**. It helps in **network security audits, penetration testing, and vulnerability assessment** by detecting accessible ports on a given IP address or localhost.

---

## 🛠 Features
✅ Scans **open ports** on a target system (local or remote)  
✅ Supports **custom port ranges** (scan specific ports or all 65,535 ports)  
✅ Fast **multi-threaded scanning** for quick results  
✅ Identifies **common services** running on open ports  
✅ Works on **Windows, Linux, and macOS**  

---

## 📜 Installation
Install the required dependencies using pip:
```sh
pip install socket threading
```

---

## 📂 Usage
Run the tool and enter the target IP & port range:
```sh
python portscanner.py
```
The script will scan the ports and display open ones.

---

## 📊 Example Input & Output

### 🔹 **User Input**
```
Enter target IP: 127.0.0.1
Enter start port: 20
Enter end port: 100
```

### 🔹 **Output**
```
🔍 Scanning 127.0.0.1 for open ports...

✅ Port 22 is open on 127.0.0.1
✅ Port 80 is open on 127.0.0.1

✅ Port scanning completed!
```

---

## 🚀 Future Enhancements
🔹 **Add service detection** (e.g., SSH, HTTP, FTP)  
🔹 **Export results to a file**  
🔹 **Web-based UI for easy scanning**  


