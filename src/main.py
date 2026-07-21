import sys

def parse_line(log_line):
    try:
        parts = log_line.split()
        ip = parts[0]
        status_code = parts[-2]
        return ip, status_code
    except IndexError:
        return None, None


if len(sys.argv) < 2:
    print("Usage: python main.py <logfile>")
    sys.exit()


filename = sys.argv[1]
ip_counts = {}

print(f"Analyzing {filename}...\n")

try:
    with open(filename, "r") as file:
        for line in file:
            ip, status_code = parse_line(line)

            if ip is not None:
                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1

    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

    print("--- Top 5 Most Active IPs ---")
    for ip, count in sorted_ips[:5]:
        print(f"IP: {ip:<15} | Requests: {count}")

except FileNotFoundError:
    print(f"Error: Could not find the file '{filename}'.")
