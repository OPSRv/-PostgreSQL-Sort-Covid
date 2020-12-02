import psycopg2
import requests
from prettytable import PrettyTable


# Enter PASSWORD to conf.py !

class GetCOVID19:
    def __init__(self, USER, PASSWORD, HOST, COVID19API):
        self.__COVID19API = COVID19API
        self.__db = psycopg2.connect(database='covid_19', user=USER, password=PASSWORD, host=HOST)
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("SELECT COUNT(*) = 0 FROM pg_catalog.pg_database WHERE datname = 'covid_19'")
        not_exists_row = self.__cursor.fetchone()
        not_exists = not_exists_row[0]
        if not_exists:
            self.__cursor.execute('CREATE DATABASE covid_19')
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS sort_covid_19 (id SERIAL, Country VARCHAR(64), CountryCode VARCHAR(3), Slug VARCHAR(128), NewConfirmed INT, TotalConfirmed INT, NewDeaths INT, TotalDeaths INT, NewRecovered INT, TotalRecovered INT, Date VARCHAR(128))")
        self.__get_covid19_info()

    def __get_covid19_info(self):
        responce = requests.get(self.__COVID19API)
        self.__covid_data = responce.json()
        self.__cursor.execute("TRUNCATE sort_covid_19")
        for item in self.__covid_data['Countries']:
            sql = "INSERT INTO sort_covid_19 (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (item['Country'], item['CountryCode'], item['Slug'], item['NewConfirmed'], item['TotalConfirmed'],
                   item['NewDeaths'], item['TotalDeaths'], item['NewRecovered'], item['TotalRecovered'], item['Date'])
            self.__cursor.execute(sql, val)
        self.__db.commit()

    def get_enter_sort(self):
        exit = False
        while not exit:
            choice = int(
                input("1. Країна\n2. Нові підтверджені\n3. Заг.підтверджені\n4. Нові смерті\n5. Заг. к-ть смертей\n6. Нові одужані\n7. Заг. одужало\n0. Exit\n=:>> "))
            if choice == 1:
                sing_sort = 'country'
                self.__sort_by_field(sing_sort)
            elif choice == 2:
                sing_sort = 'newconfirmed'
                self.__sort_by_field(sing_sort)
            elif choice == 3:
                sing_sort = 'totalconfirmed'
                self.__sort_by_field(sing_sort)
            elif choice == 4:
                sing_sort = 'newdeaths'
                self.__sort_by_field(sing_sort)
            elif choice == 5:
                sing_sort = 'totaldeaths'
                self.__sort_by_field(sing_sort)
            elif choice == 6:
                sing_sort = 'newrecovered'
                self.__sort_by_field(sing_sort)
            elif choice == 7:
                sing_sort = 'totalrecovered'
                self.__sort_by_field(sing_sort)
            elif choice == 0:
                exit = True
                self.__cursor.close()
                self.__db.close()
            else:
                print("Ok")

    def __sort_by_field(self,sing_sort):
        th_country = ["Країна", "Нові підтверджені", "Заг.підтверджені","Нові смерті", "Заг. к-ть смертей", "Нові одужані", "Заг. одужало"]
        reverse = 'DESC'
        print(sing_sort)
        if sing_sort == 'country':
            reverse = ''
        self.__cursor.execute(f"SELECT country, newconfirmed, totalconfirmed, newdeaths, totaldeaths, newrecovered, totalrecovered FROM sort_covid_19 ORDER BY {sing_sort} {reverse}")
        td = []
        for row in self.__cursor:
            for key in row:
                td.append(key)
        columns = len(th_country)
        table = PrettyTable(th_country)
        td_data = td[:]
        while td_data:
            table.add_row(td_data[: columns])
            td_data = td_data[columns:]
        print(table)


if __name__ == "__main__":
    pass