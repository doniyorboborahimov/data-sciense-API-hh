#!/bin/sh

# Проверяем, что файл hh_positions.csv существует
if [ ! -f ../ex03/hh_positions.csv ]; then
  echo "Файл hh_positions.csv не найден!"
  exit 1
fi
{
  echo "name,count"
  cut -d, -f3 ../ex03/hh_positions.csv | tail -n +2 | tr -s ' ' | grep -v '^-$' | sort | uniq -c | sort -nr | awk '{print $2 "," $1}'
} > hh_uniq_positions.csv

echo "Результат подсчета уникальных позиций сохранен в hh_uniq_positions.csv"
