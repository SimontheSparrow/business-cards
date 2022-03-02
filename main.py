import base_contact
import faker
from business_contact import BusinessContact
from base_contact import BaseContact

fake = faker.Faker()

card_one = BaseContact("Tommy", "Emery", "Emery@armyspy.com", "123456789")
card_two = BaseContact("Mary", "Horton", "Horton@armyspy.com", "123456789")
card_three = BaseContact("Louise", "Treat", "Treat@armyspy.com", "123456789")
card_four = BaseContact("Stephen", "Martin", "Martin@armyspy.com", "123456789")
card_five = BaseContact("Rena", "Williams", "Williams@armyspy.com", "123456789")

list_of_cards = [card_one, card_two, card_three, card_four, card_five]

# Do wglądu:

# for card in list_of_cards:
#   print(f'First name: {card.first_name}, last name: {card.last_name}, email:  {card.email}')

print(card_one)

sorted_by_first_name_list_of_cards = sorted(list_of_cards, key=lambda person: person.first_name)
sorted_by_last_name_list_of_cards = sorted(list_of_cards, key=lambda person: person.last_name)
sorted_by_email_list_of_cards = sorted(list_of_cards, key=lambda person: person.email)

print(card_one.label_length)


def create_contacts(card_type, number):
    for card in range(number):
        new_card = card_type(fake.first_name(), fake.last_name(), fake.email(), fake.phone_number())


create_contacts(BaseContact)
