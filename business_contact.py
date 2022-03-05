from base_contact import BaseContact


class BusinessContact(BaseContact):
    def __init__(self, company_name, occupation, work_phone_nr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_name = company_name
        self.occupation = occupation
        self.work_phone_nr = work_phone_nr

    @property
    def label_length(self):
        return f'{self.first_name} {self.last_name} {len(self.first_name + self.last_name)}'


def contact(card):
    print(f'Wybieram numer {card.work_phone_nr} i dzwonię do  {card.first_name}, {card.last_name}')
