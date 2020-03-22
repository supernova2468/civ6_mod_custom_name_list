# generates a city name list xml that can be loaded as a mod
import xml.etree.ElementTree as ET

LANGUAGE = 'en_US'
INPUT_FILE = 'test_city_list.txt'
OUTPUT_FILE = 'city_name_list.xml'

city_list = []
with open(INPUT_FILE, 'r') as city_list_file_obj:
    for city_name in city_list_file_obj:
        city_list.append(city_name.rstrip())


game_data_element = ET.Element('GameData')
tree = ET.ElementTree(element=game_data_element)
localized_text_element = ET.SubElement(game_data_element, 'LocalizedText')

for city_name in city_list:
    row_element = ET.SubElement(localized_text_element, 'Row')
    row_element.attrib['Tag'] = 'LOC_CUSTOM_CITY_NAME_{}'.format(city_list.index(city_name))
    row_element.attrib['Language'] = LANGUAGE
    text_element = ET.SubElement(row_element, 'Text')
    text_element.text = city_name

tree.write(OUTPUT_FILE)