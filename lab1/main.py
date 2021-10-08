import xml.etree.ElementTree as ET

INPUT_XML = 'input.xml'
OUTPUT_XML = 'output.xml'

def validate(input = INPUT_XML):
    from lxml import etree
    parser = etree.XMLParser(dtd_validation=True)
    try:
        etree.parse(input, parser)
    except Exception as e:
        print('Validation has been failed')
        print(f'\t>>>: {e}')
        return True

def dump(output = OUTPUT_XML):
    with open(output, 'wb') as f:
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n'.encode('utf8'))
        f.write('<!DOCTYPE group SYSTEM "task1.dtd">\n'.encode('utf8'))
        tree.write(f, encoding='utf-8')    

if __name__ == '__main__':


    failed = validate(INPUT_XML)
    if failed:
        exit(0)    
    print('Validation has been successful')
    print(f'INPUT XML="{INPUT_XML}"')
    print('-'*32)

    tree = ET.parse(INPUT_XML)
    root = tree.getroot()

    for student in root.findall('student'):
        # list all subject for a student
        subjects = student.findall('subject')
        actual_average = 0

        # find actual average
        for sub in subjects:
            actual_average += int(sub.attrib['mark'])
        actual_average /= len(subjects)

        # change to actual
        student.find('average').text = f'{actual_average:.1f}'

    dump(OUTPUT_XML)

    print('script has been finished')
    print(f'OUTPUT XML="{OUTPUT_XML}"')
    print('-'*32)

    