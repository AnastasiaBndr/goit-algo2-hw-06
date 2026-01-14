import json
import os

def data_loader(file_path):
    absolute_file_path = f"{os.getcwd()}{file_path}"
    try:
        ips = []
        with open(absolute_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    log = json.loads(line)
                except json.JSONDecodeError:
                    continue

                ip = (
                    log["http_x_forwarded_for"].split(",")[0].strip()
                    if log.get("http_x_forwarded_for")
                    else log.get("remote_addr")
                )
                ips.append(ip)

            return ips

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
