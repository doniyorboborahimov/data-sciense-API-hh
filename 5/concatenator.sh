#!/bin/sh

OUTPUT_FILE="hh_positions_combined.csv"

# Удалим старый результат
rm -f "$OUTPUT_FILE"

# Получаем список всех нужных CSV
FILES=$(ls hh_positions_*.csv 2>/dev/null | grep -v combined)
if [ -z "$FILES" ]; then
  echo "Нет файлов hh_positions_*.csv для объединения."
  exit 1
fi

# Извлекаем заголовок
HEADER=$(head -n 1 $(echo "$FILES" | head -n 1))

# Объединяем без заголовков, сортируем и удаляем дубликаты
{
  for f in $FILES; do
    tail -n +2 "$f"
  done
} | sort -u > tmp_data.csv

# Добавляем заголовок наверх
echo "$HEADER" > "$OUTPUT_FILE"
cat tmp_data.csv >> "$OUTPUT_FILE"
rm tmp_data.csv

echo "Файл $OUTPUT_FILE создан с корректным заголовком."

