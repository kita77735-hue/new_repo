from address import Address
from mailing import Mailing


from_addr = Address("101000", "Москва", "ул. Пушкина", "10", "5")
to_addr = Address("202000", "Санкт-Петербург", "ул. Колотушкина", "20", "10")


mailing = Mailing(to_addr, from_addr, 500, "TRACK123456")


print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
