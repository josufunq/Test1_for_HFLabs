import re

# Определение функции process_address для обработки адресов
def process_address(address):
    # Задание шаблона для поиска частей адреса
    pattern = r'(\d+)\s*(\D+)\s*(\d+)\s*(\D+)'
    # Задание строки замены для найденных частей адреса
    replacement = r'\1 \2 \4'

    # Проверка, содержит ли адрес слово "МОСКВА" и добавление цифры "1" после него
    if "МОСКВА" in address:
        address = re.sub(r'(МОСКВА)', r'\g<1> 1', address)

    # Выполнение замены согласно шаблону и строке замены
    processed_address = re.sub(pattern, replacement, address)
    return processed_address

# Задание строк адресов
address1 = "140002 ЛЮБЕРЦЫ 2 ОКТЯБРЬСКИЙ ПР 123/4"
address2 = "143095 ГОЛИЦЫНО 5 ПАРКОВАЯ 7"
address3 = "123459 МОСКВА 1 МОЛОСТОВЫХ 19"

# Обработка адресов с помощью функции process_address
processed_address1 = process_address(address1)
processed_address2 = process_address(address2)
processed_address3 = process_address(address3)

# Вывод обработанных адресов на экран
print(processed_address1)
print(processed_address2)
print(processed_address3)


