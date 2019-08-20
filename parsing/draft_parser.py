# utilized post MAML to XML conversion


import xml.etree.ElementTree as et
root = et.parse('ps_man_final.xml')
root2 = root.getroot()

for tag in root2.iter('helpItems'):

    # DETAILS
    for commands in tag.iter('command'):
        details = commands.find('details')
        
        # NAME
        name = details.find('name')
        print(name.text)
        
        # DETAILS DESCRIPTION
        detail_description = details.find('description')
        print(detail_description.text)
        
        # DESCRIPTION
        description = commands.find('description')
        print(description.text)
        
        # SYNTAX
        syntax = commands.findall('syntax/syntaxItem/parameter/name')
        for syntax_param in syntax:
            print(syntax_param.text)
