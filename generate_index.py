import os

# Katalog, z którego pobieramy pliki (np. bieżący katalog repozytorium)
directory = "."

# Plik, który generujemy
index_file = "index.html"

# Pobieramy listę plików, ignorując samego siebie i katalogi
files = [f for f in os.listdir(directory) if os.path.isfile(f) and f != index_file]

# Tworzymy zawartość HTML
html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista plików</title>
</head>
<body>
    <h1>Lista plików w repozytorium</h1>
    <ul>
        {''.join(f'<li><a href="{file}">{file}</a></li>' for file in files)}
    </ul>
</body>
</html>
"""

# Zapisujemy plik
with open(index_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Plik {index_file} został wygenerowany.")
