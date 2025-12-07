import re
from collections import defaultdict

class LogAnalyzer:
    def __init__(self):
        # Padrões suspeitos
        self.suspicious_patterns = [
            r'failed password',
            r'login failed',
            r'invalid user',
            r'unauthorized',
            r'connection refused',
            r'error 40\d',
            r'ssh.*failed',
            r'access denied',
            r'sql injection',
            r'xss attempt'
        ]
        self.ip_fail_count = defaultdict(int)
        self.bruteforce_threshold = 5

    # Extrair IPs de logs
    def extract_ip(self, line):
        match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
        return match.group(0) if match else None

    # Analisar uma linha
    def analyze_line(self, line):
        detected_threats = []

        for pattern in self.suspicious_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                detected_threats.append(f"Pattern detected: {pattern}")

        ip = self.extract_ip(line)
        if ip and any(p in line.lower() for p in ["failed", "invalid", "denied"]):
            self.ip_fail_count[ip] += 1
            if self.ip_fail_count[ip] >= self.bruteforce_threshold:
                detected_threats.append(
                    f"Brute force detected from IP {ip} ({self.ip_fail_count[ip]} attempts)"
                )

        return detected_threats

    # Analisar várias linhas de uma vez (continua)
    def analyze(self, lines):
        results = []
        for line in lines:
            threats = self.analyze_line(line)
            if threats:
                results.append({
                    "line": line.strip(),
                    "threats": threats
                })
        return results

