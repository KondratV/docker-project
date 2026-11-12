from flask import Flask, request, redirect
import csv
import os

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # Имена полей должны совпадать с name="..." в твоем HTML
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    laptop_number = request.form.get('laptop_number')
    
    file_path = '/app/data/data.csv'
    file_exists = os.path.isfile(file_path)
    
    # Открываем файл в режиме добавления ('a')
    with open(file_path, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';') # Точка с запятой лучше для русского Excel
        if not file_exists:
            writer.writerow(['Имя', 'Фамилия', 'Номер ноутбука']) # Заголовки
        writer.writerow([first_name, last_name, laptop_number])
        
    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)