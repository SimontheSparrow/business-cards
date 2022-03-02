class BaseContact:
    def __init__(self, first_name, last_name, email, phone_nr):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_nr = phone_nr

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    @property
    def label_length(self):
        return f'{self.first_name} {self.last_name} {len(self.first_name + self.last_name)}'


def contact(card):
    print(f'Wybieram numer {card.phone_nr} i dzwonię do  {card.first_name}, {card.last_name}')
