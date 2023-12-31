Projekt Samochód
——
Dzieli się na dwie części:
- Pilot
- Samochód

Pilot, komponenty:
- 8 przycisków
- wyświetlacz
- obudowa
- raspberry pi zero

Samochód, komponenty:
v raspberry pi pico x2
v raspberry pi pico w 1x
v czujniki odległości x4
v obudowa podwozie 
- obudowa karoseria
v 2 silniki 3000rpm
v bateria 11.1v
v stepdown 5v
v wyświetlacz
v sterownik do silnika 12v
v koła 2x

Samochód będzie posiadał cztery kola, dwa koła zasilane silnikiem, dwa koła stabilizujące.


Funkcje pilota
Przyciski:
- przód
- tył
- lewo
- prawo
- menu dol
- menu góra
- ok
- park
- czujnik on/off
- launch control

TODO Pilota:
- menu pilota
- wyswietlanie tego menu pilota
- włączanie programu podczas włączenia płytki
- automatyczne łączenie się po wifi
- zaprojektowanie obudowy pilota
v wysyłanie requestow po wifi

TODO Samochodu:
- polaczenie wszystkich trzech mikrokontrolerów za pomocą UART
- zaprojektowanie karoserii (wyjście na wyświetlacz)
- tryb testowy
- inwencja twórcza na wyświetlacz.
- wysylanie danych czujnikow z wifi do pilota
v (serwer) odbieranie requestow
v zasilenie dwóch płytek ze step down 5v
v zaprojektowanie podwozia
v obsługa czujników zbliżeniowych
v przesyłanie danych z kontrolera silnika do kontrolera wifi
v zwracanie informacji o stanie samochodu do kontrolera wifi

