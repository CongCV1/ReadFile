'''
Created on Jul 16, 2019

@author: PC
'''
import cantools
import lxml.etree as ET
#import xml.etree.ElementTree as ETS
db = cantools.database.load_file("CAN.dbc")
#print(db)
my_data=""
messages = db.messages
for message in messages:
    print(message)
    root_message = message.name
    print(root_message)
    root = ET.Element("message", name=root_message)
    print(root)
    ET.SubElement(root, "frame_id").text = str(message.frame_id)
    ET.SubElement(root, "sender").text = str(message.senders[0])
    ET.SubElement(root, "comment").text = str(message.comment)
    ET.SubElement(root, "send_type").text = str(message.send_type)
    ET.SubElement(root, "bus_name").text = str(message.bus_name)
    for signal in message.signals:
        sub_signal = ET.SubElement(root, "signal", name = signal.name)
        ET.SubElement(sub_signal, "start").text = str(signal.start)
        ET.SubElement(sub_signal, "length").text = str(signal.length)
        ET.SubElement(sub_signal, "byte_order").text = str(signal.byte_order)
        ET.SubElement(sub_signal, "is_signed").text = str(signal.is_signed)
        ET.SubElement(sub_signal, "initial").text = str(signal.initial)
        ET.SubElement(sub_signal, "scale").text = str(signal.scale)
        ET.SubElement(sub_signal, "offset").text = str(signal.offset)
        ET.SubElement(sub_signal, "minimum").text = str(signal.minimum)
        ET.SubElement(sub_signal, "maximum").text = str(signal.maximum)
        ET.SubElement(sub_signal, "unit").text = str(signal.unit)
        ET.SubElement(sub_signal, "choices").text = str(signal.choices)
        ET.SubElement(sub_signal, "comment").text = str(signal.comment)
        ET.SubElement(sub_signal, "receivers").text = str(signal.receivers[0])
        ET.SubElement(sub_signal, "is_multiplexer").text = str(signal.is_multiplexer)
        ET.SubElement(sub_signal, "is_float").text = str(signal.is_float)
    
    my_data += ET.tostring(root)
    #my_data = ET.ElementTree(root)
    
myfile = open("CAN.xml", "w") 
myfile.write(my_data)
myfile.close()


#with open("CAN.xml", "w") as file:
    #my_data.write(file, pretty_print = True)
#print(db)

