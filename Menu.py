import datetime
from datetime import date
import os.path
from os import path
import pandas as pd

def menu():
    print('''
    _______Student Management______
    1. View Students
    2. Edit Students
    3. Create Students
    4. Delete students
    5. Save and Exit
    ''')

header = ['ID', 'First Name', 'Last Name', 'Date of Birth', 'Math Score', 'Literature Score', 'GPA', 'Status']
df_Student = pd.DataFrame(header)
