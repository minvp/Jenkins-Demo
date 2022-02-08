def viewStudent_By_ID():
    if path.exists('database.csv'):
        idStudent = int(input('Enter student ID: '))
        print('________Student Information________')
        df_Student = pd.read_csv('database.csv')
        df_Student = df_Student[df_Student['ID'] == idStudent]
        print(df_Student.to_string())
        input('Back to menu.....')
    else:
        print('File not found! Please add data....')
        addStudent()

