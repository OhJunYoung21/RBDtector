import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def convert_flow_events(file_path: str, output_path: str):
    formatted_lines = []

    # encoding issue resolved!! 😄

    with open(file_path, 'r', encoding='cp949') as f:
        all_lines = f.readlines()

    header_line = all_lines[0].strip()

    for line in all_lines[2:]:
        line = line.strip().split('\t')

        if len(line) == 4:
            _, start_time, event, duration = line
            start_time = datetime.strptime('2025-07-07 ' + start_time, '%Y-%m-%d %H:%M:%S')
            end_time = start_time + timedelta(seconds=int(duration))
            formatted = f"{start_time.strftime('%H:%M:%S')},000000-{end_time.strftime('%H:%M:%S')},000000;{event}"
            formatted_lines.append(formatted)

        else:
            continue

    final_lines = [header_line] + formatted_lines

    # 4. 결과 저장
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for line in final_lines:
            out_file.write(line + '\n')

    return


def convert_arousal(file_path: str, output_path: str):
    return
