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
- raspberry pi pico x2
- raspberry pi pico w 1x
- czujniki odległości x?
- obudowa podwozie 
- obudowa karoseria
- 2 silniki 3000rpm
- bateria 11.1v
- stepdown 5v
- wyświetlacz
- sterownik do silnika 12v
- koła 2x

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
- wysyłanie requestow po wifi
- włączanie programu podczas włączenia płytki
- automatyczne łączenie się po wifi
- zaprojektowanie obudowy pilota

TODO Samochodu:
- (serwer) odbieranie requestow
- polaczenie wszystkich trzech mikrokontrolerów za pomocą UART
- zasilenie dwóch płytek ze step down 5v
- zaprojektowanie podwozia
- zaprojektowanie karoserii (wyjście na wyświetlacz)
- obsługa czujników zbliżeniowych
- przesyłanie danych z kontrolera silnika do kontrolera wifi
- zwracanie informacji o stanie samochodu do kontrolera wifi
- tryb testowy
- inwencja twórcza na wyświetlacz.