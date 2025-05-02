#!/bin/sh

# Проверяем, что файл hh_sorted.csv существует
if [ ! -f ../ex02/hh_sorted.csv ]; then
  echo "Файл hh_sorted.csv не найден!"
  exit 1
fi

# Применяем фильтрацию
{
  # Копируем первую строку (заголовки)
  head -n 1 ../ex02/hh_sorted.csv
  
  # Очищаем все строки и заменяем названия должностей
  tail -n +2 ../ex02/hh_sorted.csv | while IFS=, read -r id created_at name has_test alternate_url
  do
    # Преобразуем название должности, оставляя только Junior, Middle, Senior
    cleaned_name=$(echo "$name" | grep -o -i "Junior\|Middle\|Senior" | tr '\n' ' ' | sed 's/ $//')

    # Удаляем дублирующиеся слова
    cleaned_name=$(echo "$cleaned_name" | tr ' ' '\n' | sort -u | tr '\n' ' ' | sed 's/ $//')

    # Если название должности пустое, ставим "-"
    if [ -z "$cleaned_name" ]; then
      cleaned_name="-"
    fi

    # Выводим результат
    echo "$id,$created_at,$cleaned_name,$has_test,$alternate_url"
  done
} > hh_positions.csv

echo "Данные очищены и сохранены в hh_positions.csv"
