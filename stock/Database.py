import psycopg2
connection = psycopg2.connect("user=postgres password=Paruchuru@1997")
current = connection.cursor()

current. execute("DROP TABLE IF EXISTS STATISTICS")
current. execute("DROP TABLE IF EXISTS PROFILES")
current. execute("DROP TABLE IF EXISTS FINANCES")

current.execute("CREATE TABLE STATISTICS(sno int, stat_ticker varchar PRIMARY KEY, marketcap varchar,enterprise_value varchar, "
                "return_on_assets varchar, total_cash varchar,operating_cash_flow varchar,levered_free_cash_flow varchar, total_debt varchar,"
                "current_ratio varchar, gross_profit varchar, profit_margin varchar)")
print("statistics created")

current.execute("CREATE TABLE PROFILES(prof_ticker varchar PRIMARY KEY, name varchar, Address varchar, phonenum varchar, website varchar,"
                "sector varchar, industry varchar, full_time varchar, bus_summ varchar )")
print("profiles created")

current.execute("CREATE TABLE FINANCES(Fin_ticker varchar PRIMARY KEY, Total_Revenue varchar, Cost_of_Revenue varchar,"
                " Income_Before_Tax varchar,Net_Income varchar)")
print("profiles created")

connection.commit()
connection.close()
current.close()

