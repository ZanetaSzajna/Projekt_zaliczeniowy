# BIAŁA LISTA 

Skrypt powstał w celu pobierania kont bankowych  z Wykazu podatników VAT inaczej zwaną białą listę. 



## OPIS 

Przed uruchomieniem programu należy uzupełnić dane w pliku nip.csv

Program pobiera NIP z pliku nip.csv łączy się z białą listą za pomocą API https://wl-api.mf.gov.pl/api/search/nip/  i pobiera wszystkie dane doyczące podatnika.
Do numeru NIP przypisuje konto bankowe  i zapisuje dane w pliku raport  w bieżącą datą takk aby można było archwizować dane.



## Dane techniczne 

Plik wykorzystuje biblioteki:

 *json
 *csv
 *requests
#   P r o j e k t _ z a l i c z e n i o w y  
 