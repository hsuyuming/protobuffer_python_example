#https://developers.google.com/protocol-buffers/docs/pythontutorial

import complex_example_pb2 as complex_example_pb2

complex_message = complex_example_pb2.ComplexMessage()

one_dummy_message = complex_example_pb2.DummyMessage()
one_dummy_message.id = 123
one_dummy_message.name = "Abe"

# complex_message.one_dummy = one_dummy_message
# print(complex_message) # AttributeError: Assignment not allowed to field "one_dummy" in protocol message object.

complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "Abe"


first_multiple_dummy = complex_message.multiple_dummy.add() #create a reference 
first_multiple_dummy.id = 345
first_multiple_dummy.name = "I'm the first element on an array."


complex_message.multiple_dummy.add(id=555, name="Second element") # more better, and recommand

#Be Careful, this does copy!!!
third_dummy_message = complex_example_pb2.DummyMessage()
third_dummy_message.id = 999
third_dummy_message.name = "Third one"

complex_message.multiple_dummy.extend([third_dummy_message]) # This way is create a copy of third_dummy_message

third_dummy_message.id = 111
print(third_dummy_message)


print(complex_message)