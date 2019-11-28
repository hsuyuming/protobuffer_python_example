#https://developers.google.com/protocol-buffers/docs/reference/python-generated
import addressbook_example_pb2 

# addressbook_message = addressbook_example_pb2.AddressBook()

# addressbook_message.people.add(
#     name="Abe", 
#     id=123, 
#     email="abe@xxx.com", 
#     phones=addressbook_example_pb2.Person.phones.add(
#         number="0888888", 
#         type=addressbook_example_pb2.Person.HOME 
#     )
#     # last_updated=tttt
# )

# print(addressbook_message)

# person_message = addressbook_example_pb2.Person()
# person_message.name = "Abe"
# person_message.id = 1234
# person_message.email = "abe@xxx.com"
# person_message.phones.add(number="555-4321",type=addressbook_example_pb2.Person.HOME)

# print(person_message)



# def PromptForAddress(person):

addressbook_message = addressbook_example_pb2.AddressBook()
print(addressbook_message)
with open("addressbook.bin","wb") as f:
    f.write(addressbook_message.SerializeToString())


def PromptForAddress(person):
    person.id = int(raw_input("Enter person ID number: "))














# with open("addressbook.bin","rb") as f :
#     addressbook_message_read = addressbook_example_pb2.AddressBook().FromString(f.read())

# print(addressbook_message_read)