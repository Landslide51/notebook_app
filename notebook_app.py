import json
import datetime
import os

FILENAME = "data.json"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(json.dumps([], ensure_ascii=False))

def save_file(data):
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))

def main():
    with open(FILENAME, encoding="utf-8") as f:
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
            try:
                idx = int(input("Введите id сообщения или оставьте пустым, чтобы вывести всё: "))
            except ValueError:
                idx = -1
            for note in data:
                if note['id'] == idx:
                    print(f"""
Title:
    {note['title']}
Text:
    {note['msg']}
Last modified:
    {note['date']}
""") 
                    break
            else:
                print(json.dumps(data, indent=4, ensure_ascii=False))
        elif command == "exit":
            exit()


main()