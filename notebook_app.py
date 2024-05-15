import json
import datetime
import os

FILENAME = "data.json"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write(json.dumps([]))

def save_file(data):
    with open(FILENAME, "w") as f:
        f.write(json.dumps(data, indent=4))

def main():
    with open(FILENAME) as f:
        data = json.loads(f.read())
    while True:
        command = input("Введите команду: ")
        if command == "add":
            idx = data[-1]['id'] + 1 if data else 0
            title = input("Введите заголовок заметки: ")
            msg = input("Введите тело заметки: ")
            date = datetime.datetime.now()
            date = date.strftime("%Y-%m-%d %H:%M:%S")
            new_record = {"id": idx, 'title': title, 'msg': msg, 'date': date}
            data.append(new_record)
            save_file(data)
        elif command == "read":
            for note in data:
                print(f"""
Title:
    {note['title']}
Text:
    {note['msg']}
Last modified:
    {note['date']}
""")
        elif command == "exit":
            exit()


main()