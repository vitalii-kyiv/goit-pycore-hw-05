import sys
import os

def parse_log_line(line: str) -> dict:
    """Парсує рядок лог-файлу в словник з компонентами."""
    try:
        parts = line.strip().split(' ', 3)
        if len(parts) < 4:
            return {}
        return {
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'message': parts[3]
        }
    except Exception as e:
        print(f"Помилка парсингу рядка: {line}. Деталі: {e}")
        return {}

def load_logs(file_path: str) -> list:
    logs = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл '{file_path}' не знайдено.")
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parsed_line = parse_log_line(line)
            if parsed_line:
                logs.append(parsed_line)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict, level=None, logs=None):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for type, count in counts.items():
        print(f"{type:<10} | {count:<10}")
    if level and logs:
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [<рівень_логування>]")
        return
    file_path = sys.argv[1]
    if len(sys.argv) > 2:
        level = sys.argv[2]
    else:
        level = None

    try:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        if level:
            filtered_logs = filter_logs_by_level(logs, level)
            display_log_counts(counts, level, filtered_logs)
        else:
            display_log_counts(counts)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
