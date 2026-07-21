# Log File Processor 🛡️📊

A high-performance, command-line utility designed to act as the foundation for server monitoring and cybersecurity analysis. When a website slows down or faces a cyber attack (such as a DDoS), system administrators don't have the time to manually read millions of log lines. This tool automatically parses the data, identifying which IP addresses are sending suspicious amounts of requests in a matter of seconds.

## 🌟 Key Features

* **Memory Efficient**: Processes massive log files line-by-line, ensuring minimal RAM consumption regardless of the file size.
* **Fast Analytics**: Leverages Python dictionaries for rapid `O(1)` counting and lambda functions for lightning-fast sorting algorithms.
* **CLI Integration**: Built as a native command-line tool, interacting directly with the operating system via `sys.argv`.
* **Robust Error Handling**: Implements strict `try/except` blocks to prevent unexpected crashes from malformed log lines or missing files.

## 📂 Project Structure

```text
Log-File-Processor/
│
├── src/
│   └── main.py             # Core log processing, parsing, and analysis logic
│
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MehdiAhmadiyan/Log-File-Processor.git
   cd Log-File-Processor
   ```

2. **Run the analyzer:**
   Execute the script via terminal, passing the path to your log file as an argument:
   ```bash
   python src/main.py access.log
   ```

## 📝 TODO: Future Enhancements

This project is actively evolving. Here are the planned features to transform it into a full-fledged monitoring suite:

- [ ] **Multi-Format Support**: Add parsing capabilities for different server logs (Nginx, Apache, IIS).
- [ ] **Advanced Regex Engine**: Implement Regular Expressions to extract deeper insights like HTTP status codes (e.g., finding 404/500 errors) and User-Agents.
- [ ] **Data Exporting**: Allow users to export the analysis results to CSV or JSON formats for further reporting.
- [ ] **GeoIP Integration**: Integrate a GeoIP library to map suspicious IP addresses to their physical countries/locations.
- [ ] **Real-Time Monitoring (Tailing)**: Add a feature to "tail" the log file and analyze requests in real-time as they happen.
- [ ] **Automated Alerting**: Build a notification module to send an email or Telegram message if traffic from a single IP exceeds a safe threshold.
- [ ] **Unit Testing**: Add `pytest` test cases to ensure the parsing logic remains accurate during future updates.

## 🛠️ Technologies Used
* **Python 3.x**

## 📜 License
This project is open-source and available under the terms of the included LICENSE.
