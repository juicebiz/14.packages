from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from rembg import remove
from PIL import Image

def today():
    print(datetime.today().strftime("%d-%m-%Y"))

def remove_bg():
    input_path = 'in.png'
    output_path = 'out.png'
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    today()
    remove_bg()