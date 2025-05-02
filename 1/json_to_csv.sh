#!/bin/sh

# Проверяем, что файл hh.json существует
if [ ! -f ../ex00/hh.json ]; then
  echo "Файл hh.json не найден!"
  exit 1
fi

# Конвертируем JSON-массив в CSV
jq -r '(["id","created_at","name","has_test","alternate_url"] | @csv), (.[] | [.id, .created_at, .name, .has_test, .alternate_url] | @csv)' ../ex00/hh.json > hh.csv

echo "Данные сохранены в hh.csv"
