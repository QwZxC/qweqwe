import gspread

gs = gspread.service_account(filename='qwe.json')
sh = gs.open_by_key("1a-dZsSTf4umMqdZJd3zax-9btQEcR1k1rDS7-4MGGoE")
worksheet = sh.sheet1

numbers = worksheet.col_values(6)
name = worksheet.col_values(4)
Secondname = worksheet.col_values(3)
Fullname = [""] * len(Secondname)
Client_list = {}
client = ""
Find_list = {}

for i in range(len(Secondname)):
    Fullname[i] = Secondname[i] + " " + name[i]

for i in range(len(Fullname) - 1):
    Client_list[Fullname[i+1]] = numbers[i+1]

for i in range(len(Fullname) - 1):
    Client_list[numbers[i+1]] = Fullname[i+1]

client_name = str(input("Введите имя и фамилию клиента: "))

for i in range(len(Fullname) - 1):

    if client_name in Fullname[i+1]:
        client = Fullname[i+1]
        Find_list[client] = Client_list.get(client)
        print(client,": ", Client_list.get(client))

    if client_name in numbers[i+1]:
        number = numbers[i+1]
        Find_list[numbers[i+1]] = Client_list.get(number)
        print(number, ": ", Client_list.get(number))



