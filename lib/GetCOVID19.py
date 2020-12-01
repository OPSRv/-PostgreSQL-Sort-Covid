import psycopg2
import requests
from conf import *s


class GetCOVID19:
    def __init__(self, USER, PASSWORD, HOST, COVID19API):
        self.__COVID19API = COVID19API

        self.__db = psycopg2.connect(
            database='covid_19', user=USER, password=PASSWORD, host=HOST)
        self.__cursor = self.__db.cursor()
    #     self.__cursor.execute("CREATE DATABASE covid_19")
    #     self.__cursor.execute("USE covid_19")
    #     self.__cursor.execute(
    #         "CREATE TABLE sort_covid_19 (id SERIAL, Country VARCHAR(64), CountryCode VARCHAR(3), Slug VARCHAR(128), NewConfirmed INT, TotalConfirmed INT, NewDeaths INT, TotalDeaths INT, NewRecovered INT, TotalRecovered INT, Date VARCHAR(128))")
        self.__get_covid19_info()

    def __get_covid19_info(self):
    #     responce = requests.get(self.__COVID19API)
    #     self.__covid_data = responce.json()
        self.__cursor.execute("TRUNCATE sort_covid_19")
    #     for item in self.__covid_data['Countries']:
    #         sql = "INSERT INTO sort_covid_19 (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #         val = (item['Country'], item['CountryCode'], item['Slug'], item['NewConfirmed'], item['TotalConfirmed'],
    #                item['NewDeaths'], item['TotalDeaths'], item['NewRecovered'], item['TotalRecovered'], item['Date'])
    #         self.__cursor.execute(sql, val)
    #     self.__db.commit()

    def sort_by_total_confirmed(self):
        print('Hello')
        table_total_confirmed = self.__cursor.execute(
            "SELECT TotalConfirmed FROM sort_covid_19 ORDER BY TotalConfirmed").fetchall()
        records = table_total_confirmed
        for i in records:
            print(i)
        # print(table_total_confirmed)
        # _file = open("access.txt", "a")
        # _file.write(table_total_confirmed)
        self.__cursor.close()
        self.__cursor.close()

    def sort_by_new_confirmed(self):
        pass

    def sort_by_country_name(self):
        pass




if __name__ == "__main__":
    pass