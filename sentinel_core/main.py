import os
from log_analyzer import LogAnalyzer

def read_logs(log_file_path):
    if not os.path.exists(log_file_path):
        print(f"❌ Log file not found: {log_file_path}")
        return []

    with open(log_file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def main():
    log_path = r"C:\Ultron Sentinel\logs\example.log"  # Caminho do seu arquivo de log

    print("🔍 Ultron Sentinel - Log Analyzer v1.1 iniciado...\n")

    logs = read_logs(log_path)
    analyzer = LogAnalyzer()

    for line in logs:
        threats = analyzer.analyze_line(line)
        if threats:
            for threat in threats:
                print(f"\033[91m[ALERT] {threat} -> {line.strip()}\033[0m")

    print("\n✅ Análise concluída.")

if __name__ == "__main__":
    main()
