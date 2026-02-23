my_heigh = 176
print(my_heigh)

my_name = "Никита"
my_name = "Никита Пономарев"
print(my_name)

pet_name = input("Как зовут вашего питомца?")
if not pet_name:
    pet_name = "Рыжий"
print("Мой любимчик - " + pet_name)


def print_python():
    print("Учу Python!")


print_python()


def print_letter(let):
    print(let, end='')


print_letter('С')
print_letter('т')
print_letter('у')
print_letter('д')
print_letter('е')
print_letter('н')
print_letter('т')
