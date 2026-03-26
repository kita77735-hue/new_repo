from address import Address
from mailing import Mailing

# Создаём адреса
from_addr = Address("101000", "Москва", "ул. Пушкина", "10", "5")
to_addr = Address("202000", "Санкт-Петербург", "ул. Колотушкина", "20", "10")

# Создаём отправление
mailing = Mailing(to_addr, from_addr, 500, "TRACK123456")

# Печатаем в нужном формате
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")