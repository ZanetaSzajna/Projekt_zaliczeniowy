import requests
import json
import csv
from Today import today
from Today import new_today

my_dict = {}

NIP = []

def pobieranie_numerów_nip():
    try:
        with open("nip.csv", encoding='1250') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=";")
            for row in csvreader:
                NIP.append(row[0])
            #print(NIP)
    except (FileNotFoundError) as error:
        print(f"{error} -Niestety nie ma takiego pliku, sprawdź proszę  czy plik ma prawidłową nazwę ")

def pobieranie_z_białej_lity(NIP):
    pobieranie_numerów_nip()
    for nip in NIP:

        nip = nip.replace("-","").replace("PL","")
        #print(nip)
        response = requests.get(f"https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={today}")
        df = response.json()
        data_json=json.dumps(df)
        #print(data_json)
        file_name="user.json"
        with open(file_name,'w') as f:
            json.dump(df, f)
        with open(file_name, "r") as k:
            data= json.load(k)
        bank_acount=(data['result']['subject']['accountNumbers'])
        #print(bank_acount)
        my_dict[nip]=bank_acount



        with open(f'report{new_today}.csv', 'w') as csvf:
            fields=["NIP", "bank_acount"]
            csvwriter = csv.writer(csvf)

            # writing the fields
            csvwriter.writerow(fields)
            date = my_dict.items()
            for row in date:

                csvwriter.writerow(row)


def main():
    pobieranie_z_białej_lity(NIP)


if __name__ == "__main__":
    main()