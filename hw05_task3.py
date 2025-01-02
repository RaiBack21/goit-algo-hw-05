import sys
from pathlib import Path
from collections import Counter

def parse_log_line(line):
    '''Log string parsing'''
    line = line.strip().split(' ', 3)
    return {'date': line[0], 'time': line[1], 
            'level': line[2], 'text': line[3]}

def load_logs(file_path, level=None):
    '''Downloading log files'''
    logs = list()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Файл не існує.")


    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        output = f"Деталі логів для рівня '{level.upper()}':\n"
        filtered_logs = filter_logs_by_level(logs, level)
        for log in filtered_logs:
            output += f"{log['date']} {log['time']} - {log['text']}\n"
        print(output)

def filter_logs_by_level(logs, level):
    '''Filtering by log level'''
    logs = filter(
        lambda item: item['level'].lower() == level.lower(), logs)
    return list(logs)

def count_logs_by_level(logs):
    '''Counting entries by log level'''
    counts = Counter(list(map(lambda item: item['level'], logs)))
    return dict(counts)

def display_log_counts(counts):
    '''Display results'''
    output = f"Рівень логування | Кількість\n{'|':->18}{'-'*10}\n"
    for key, value in counts.items():
        output += f"{key:<17}| {value}\n"
    print(output)

def main(argv):
    try:
        if len(argv) == 3:
            load_logs(argv[1], argv[2])
        else:
            load_logs(argv[1])
    except IndexError:
        print("Помилка зчитування файлу.")

if __name__ == '__main__':
    main(sys.argv)