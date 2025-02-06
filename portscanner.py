import socket
import threading

def scan_port(ip, port):
    """Check if a port is open on a given IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"✅ Port {port} is open on {ip}")
        s.close()
    except socket.error:
        pass

def scan_ports(ip, start_port, end_port):
    """Scan a range of ports using multi-threading."""
    print(f"🔍 Scanning {ip} for open ports...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n✅ Port scanning completed!")

if __name__ == "__main__":
    target_ip = input("Enter target IP (e.g., 127.0.0.1): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    scan_ports(target_ip, start_port, end_port)
