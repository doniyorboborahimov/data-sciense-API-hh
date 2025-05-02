#!/bin/sh

# Проверяем, что файл hh.csv существует
if [ ! -f ../ex01/hh.csv ]; then
  echo "Файл hh.csv не найден!"
  exit 1
fi

# Сортируем hh.csv по колонке created_at (вторая колонка) и потом по id (первая колонка)
# Сначала сортируем по created_at, потом по id
# Оставляем строку заголовка на первом месте

{ head -n 1 ../ex01/hh.csv && tail -n +2 ../ex01/hh.csv | sort -t, -k2,2 -k1,1; } > hh_sorted.csv

echo "Данные отсортированы и сохранены в hh_sorted.csv"
