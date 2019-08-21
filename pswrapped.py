import xml.etree.ElementTree as et
root = et.parse('ps_man_final.xml')
root2 = root.getroot()
import PySimpleGUIWeb as Sg

dict = []
mod = {}
i = 0

names = [[]] # psg list (GUI)
detail_descriptions = [[]]
descriptions = [[]]
syntaxes = [[]]
layout = [[]]
dropdown_list = []

for tag in root2.iter('helpItems'):

    # DETAILS
    for commands in tag.iter('command'):
        i = i + 1
        details = commands.find('details')
        # NAME
        name = details.find('name')
        #print(name.text)
        # DETAILS DESCRIPTION
        detail_description = details.find('description')
        #print(detail_description.text)
        # DESCRIPTION
        description = commands.find('description')
        #print(description.text)
        # SYNTAX
        syntax = commands.findall('syntax/syntaxItem/parameter/name')
        syntax_list= []
        for syntax_param in syntax:
            #print(syntax_list.append(syntax_param.text))
            syntax_list.append(syntax_param.text)
        components = []
        #dict.append(name.text)
        modlist = []
        modlist.append(detail_description.text)
        modlist.append(description.text)
        modlist.append(syntax_list)

        mods = {name.text:modlist}
        mod.update(mods)

        syns_list = []
        dropdown_list.append(name.text)

        # for params in syntax_list:
        #     syns_list.append(Sg.InputText("{}".format(params)))
        # layout.append([Sg.Button("{}".format(name.text), key="{}".format(
         #        name.text))])
        # for x in syntax_list:
        #     layout.append([Sg.InputText("{}".format(x))])
        #PSG update:

    layout_final = [[Sg.DropDown(dropdown_list, enable_events=True)]]

    print("Total Modules: {}".format(i))
    print(mod)

    test = mod.get('Add-Computer')
    print(test[2])

#for x in mod:
#    layout.append([Sg.Button("{}".format(x))])

mainWindow = Sg.Window("pswrapped", layout=layout_final).Finalize()

old_v = None

while True:
    b, v = mainWindow.Read(timeout=100)

    if old_v != v:
        element = v
        layout_new = [[]]
        layout = layout_new
        layout_final_new = [[]]
        layout_final = layout_final_new

        print("Changing View...")

        test = mod.get("{}".format(element[0]))

        try:
            for x in test[2]:
                layout.append([Sg.InputText("{}".format(str(x)))])
        except:
            pass

        layout_finals = [[Sg.DropDown(dropdown_list, enable_events=True,
                                      default_value=v[0])],[Sg.Button(
                "Execute", size=(25,1)),
                         Sg.Column(layout_final), Sg.Column(layout)]]
        mainWindow = Sg.Window("pswrapped", layout=layout_finals).Finalize()

    print(v, old_v)
    old_v = v



    if b == "exit":
        quit()

    if b != Sg.TIMEOUT_KEY:
        pass

    if b is None:
        break
