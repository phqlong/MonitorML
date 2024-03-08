import os
import json


def get_ml_monitor_data(token: str):
    with open("ml_monitor_db.json") as ml_monitor_db_file:
        for item in json.load(ml_monitor_db_file):
            if item["token"] == token:
                return item
    return None


def save_raw_data_to_file(files_iterator, data_path):
    messages = []

    for file_data in files_iterator:
        try:
            if not os.path.exists(data_path):
                os.makedirs(data_path)

            filename = data_path + "/" + file_data.filename
            
            with open(filename, "wb") as f:
                f.write(file_data.content)
                ok_message = f"File uploaded successfully: {file_data.filename}"
                messages.append(ok_message)
        except Exception as e:
            failed_message = f"Failed to save file {file_data.filename}: {str(e)}"
            messages.append(failed_message)

    return messages
