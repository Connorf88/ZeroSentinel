# 🚨 ZeroSentinel

**ZeroSentinel** is a terminal-first anomaly detection pipeline built using Python, Docker, and GitHub—all 100% free and edited entirely with `nano`.  
No IDEs, no cloud costs—just raw CLI power.

## 🔍 What It Does

ZeroSentinel ingests simulated system logs, runs Isolation Forest anomaly detection, and outputs JSON alerts for suspicious behavior.  
Designed as a lightweight introduction to cybersecurity AI and local DevOps workflows.

---



---

## 🧠 Built For

- Free-tier learners  
- CLI enthusiasts  
- Cybersecurity AI explorers  
- Anyone who loves building from scratch  

---

## 💻 Terminal Preview

Here's a live Docker container executing the anomaly detection script:

```bash
$ docker run zerosentinel
[
  {
    "timestamp": "2025-07-08T03:05:20Z",
    "source_ip": "192.168.0.100",
    "action": "flood",
    "src_encoded": 2,
    "action_encoded": 2,
    "anomaly": -1
  },
  {
    "timestamp": "2025-07-08T03:05:27Z",
    "source_ip": "192.168.0.100",
    "action": "flood",
    "src_encoded": 2,
    "action_encoded": 2,
    "anomaly": -1
  }
]
