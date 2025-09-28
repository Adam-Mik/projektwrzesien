# Użyj oficjalnego obrazu Python 3.11 jako obrazu bazowego
FROM python:3.11-slim

# Ustaw zmienną środowiskową, aby Django nie buforowało stdout/stderr
ENV PYTHONUNBUFFERED 1

# Ustaw katalog roboczy wewnątrz kontenera
WORKDIR /usr/src/app

# Skopiuj plik requirements.txt do katalogu roboczego
COPY ../requirements.txt .

# Zainstaluj zależności z pliku requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj cały kod projektu do katalogu roboczego w kontenerze
COPY .. .

# Otwórz port 8000
EXPOSE 8000