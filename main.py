from application.salary import get_salary
from application.db.people import get_emploees
from datetime import datetime
from tcolors import Color


def time():
    print(Color.RED + datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))


if __name__ == '__main__':
    get_emploees()
    get_salary()
    time()
