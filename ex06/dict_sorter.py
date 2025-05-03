def dict_sorter():
    # Список кортежей
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    
    # Преобразуем список кортежей в словарь
    country_dict = {country: int(number) for country, number in list_of_tuples}
    
    # Сортируем сначала по числам (в убывание), затем по названию страны (по алфавиту)
    sorted_countries = sorted(country_dict.keys(), key=lambda country: (-country_dict[country], country))
    
    # Выводим страны по порядку
    for country in sorted_countries:
        print(country)

if __name__ == '__main__':
    dict_sorter()
