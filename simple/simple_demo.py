import simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()

simple_message.id = 123
# False is the default value for  Boolean, default value will not appear on print message
simple_message.is_simple = False

# simple_message.is_simple = True


simple_message.name = "This is a simple Message"
# simple_message.name = 34343 #TypeError: 34343 has type int, but expected one of: bytes, unicode

sample_list = simple_message.sample_list
print(type(sample_list)) #<class 'google.protobuf.pyext._message.RepeatedScalarContainer'>
# print(sample_list)
sample_list.append(3)
sample_list.append(4)
sample_list.append(5)

print(simple_message)

with open("simple.bin","wb") as f: # simple.bin is protobuffer object. 
    print("write as binary")
    bytesAsString = simple_message.SerializeToString() #byte string
    f.write(bytesAsString)


with open("simple.bin","rb") as f:
    print("read values")
    simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())

print(simple_message_read)

print("Is Simple?: " + str(simple_message_read.is_simple) )
print("Id?: " + str(simple_message_read.id) )