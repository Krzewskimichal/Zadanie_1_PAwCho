Aplikacja składa się z dwóch serwisów: server oraz redis.
Serwer jest realizowany za pomocą języka programowania Python oraz frameworka Flask.
Główny kod aplikacji znajdują się w katalogu src który zawiera plik z aplikacją, 
Dockerfile oraz requirements.txt która definiuje dodatkowe biblioteki dla interpretera pythona. 
Poza katalogiem src znajdują się dwa pliki: docker-compose.yaml który służy do budowania serwisów oraz .env
do przechowywania zmiennych środowiskowych.


zbudowanie obrazów: docker-compose build
uruchomienie aplikacji: docker-compose up
