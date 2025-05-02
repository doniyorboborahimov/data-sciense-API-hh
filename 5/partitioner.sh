#!/bin/sh

INPUT_FILE="../ex03/hh_positions.csv"

if [ ! -f "$INPUT_FILE" ]; then
  echo "Файл $INPUT_FILE не найден!"
  exit 1
fi

# Извлекаем уникальные даты
dates=$(cut -d ',' -f2 "$INPUT_FILE" | tail -n +2 | cut -d 'T' -f1 | sort | uniq)

for date in $dates; do
  output_file="hh_positions_${date}.csv"
  {
    head -n 1 "$INPUT_FILE"
    awk -F, -v d="$date" 'BEGIN{OFS=","} NR>1 {split($2, a, "T"); if (a[1] == d) print $0}' "$INPUT_FILE"
  } > "$output_file"
  echo "Создан файл: $output_file"
done
