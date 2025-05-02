#!/bin/sh
# Проверяем, что передан ровно один аргумент
if [ $# -ne 1 ]; then
  echo "Использование: $0 \"<название вакансии>\""
  exit 1
fi

# Кодируем пробелы в названии вакансии для URL
query=$(printf "%s" "$1" | sed 's/ /%20/g')

# Запрос к API HeadHunter и сохранение как массива
curl -s "https://api.hh.ru/vacancies?text=$query&per_page=20" \
  | jq '[.items[] | {id, created_at, name, has_test, alternate_url}]' \
  > hh.json

echo "Данные сохранены в hh.json"
