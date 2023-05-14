import re
from pprint import pprint
import csv

def format_phone(phone):
    """
    Функция для приведения телефона к формату +7(999)999-99-99 доб.9999
    """
    phone = re.sub(r'\D', '', phone)
    if len(phone) == 10:
        return '+7({}){}-{}-{}'.format(phone[:3], phone[3:6], phone[6:8], phone[8:])
    elif len(phone) == 11:
        return '+7({}){}-{}-{} доб.{}'.format(phone[1:4], phone[4:7], phone[7:9], phone[9:11], '')
    else:
        return phone

def merge_duplicates(_list):
    """
    Функция для объединения дублирующих записей
    """
    unique_contacts = {}
    for contact in contacts_list:
        full_name = contact[0] + contact[1] + contact[2]
        if full_name in unique_contacts:
            unique_contacts[full_name] = [unique_contacts[full_name][i] or contact[i] for i in range(len(contact))]
        else:
            unique_contacts[full_name] = contact
    return list(unique_contacts.values())

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for contact in contacts_list:
    fio = re.findall(r'^(\w+)(?:\s+(\w+))?(?:\s+(\w+))?$', contact[0])
    contact[0], contact[1], contact[2] = fio[0]

for contact in contacts_list:
    contact[5] = format_phone(contact[5])
contacts_list = merge_duplicates(contacts_list)


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
    
pprint(contacts_list)
