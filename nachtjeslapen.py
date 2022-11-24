from datetime import date

vandaag = date.today
jaar = int(input("jaar: "))
maand = int(input("maand: "))
dag = int(input("dag: "))
datum = date(jaar, maand, dag)

