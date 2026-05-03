from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("1234 5678 8765 4321", "11/28", "alex f.")

alex.addCard(card)
alex.getCard().pay(1000)

