import xml.etree.ElementTree as et
import PySimpleGUIWeb as Sg


class Posh(object):
    def __init__(self, mod_file, command="None"):
        self.root = et.parse(mod_file)  # 'ps_man_final.xml'
        self.root2 = self.root.getroot()
        i = 0
        self.dict = []
        mod = {}
        self.mod = mod
        self.pass_arg = None
        self.mod_list = []
        self.command = command
        self.names = [[]]  # psg list (GUI)
        self.detail_descriptions = [[]]
        self.descriptions = [[]]
        self.syntaxes = [[]]
        self.layout = [[]]
        self.dropdown_list = []
        self.layout_finals = []

        for tag in self.root2.iter('helpItems'):

            # DETAILS
            for commands in tag.iter('command'):
                i = i + 1
                self.details = commands.find('details')
                # NAME
                self.name = self.details.find('name')
                # print(name.text)
                # DETAILS DESCRIPTION
                self.detail_description = self.details.find('description')
                # print(detail_description.text)
                # DESCRIPTION
                self.description = commands.find('description')
                # print(description.text)
                # EXAMPLES
                self.examples = commands.findall('examples/example/code')
                self.example_list = []
                for example_items in self.examples:
                    ex_list = []
                    ex_list.append(example_items.text)
                    self.example_list.append(ex_list)

                # SYNTAX
                self.syntax = commands.findall(
                        'syntax/syntaxItem/parameter/name')
                self.syntax_list = []
                for syntax_param in self.syntax:
                    # print(syntax_list.append(syntax_param.text))
                    self.syntax_list.append(syntax_param.text)
                components = []
                # dict.append(name.text)
                self.modlist = []
                self.modlist.append(self.detail_description.text)
                self.modlist.append(self.description.text)
                self.modlist.append(self.syntax_list)
                self.modlist.append(self.example_list)

                self.example_format_list = [[]]

                self.mods = {self.name.text: self.modlist}
                self.mod.update(self.mods)

                syns_list = []
                self.dropdown_list.append(self.name.text)

            self.layout_final = [[Sg.DropDown(self.dropdown_list,
                                            enable_events=True)]]

            print("Total Modules: {}".format(i))
            print(self.mod)

            # self.test = self.mod.get('Add-Computer')
            # print(self.test[2])

    def reset(self):
        self.layout_new = [[]]
        self.layout = self.layout_new
        self.layout_final_new = [[]]
        self.layout_final = self.layout_final_new

    # def __set__(self, command):
        # pass
        # self.command = command
        #self.mod_list.append(command)

    # def __get__(self):
      #   pass
        #return self.mod(self.command)

    def ping(self, ping_target):
        self.ping_target = ping_target
        self.pass_arg = "ping {}".format(ping_target)

    def poshit(self):
        proc = subprocess.Popen(["powershell.exe", self.pass_arg],
                                stdout=sys.stdout).communicate()




launch = Posh('ps_man_final.xml')

#for x in mod:
#    layout.append([Sg.Button("{}".format(x))])

mainWindow = Sg.Window("pswrapped", size=(1000, 1000),
    layout=launch.layout_final).Finalize()

old_v = ['ok', 'ok', 'ok']
v = ['nope', 'nope', 'nope']


while True:
    b, v = mainWindow.Read(timeout=100)

    if old_v[0] != v[0] and old_v[0] is not None:
            element = v
            launch.layout_new = [[]]
            launch.layout = launch.layout_new
            launch.layout_final_new = [[]]
            launch.layout_final = launch.layout_final_new

            print("Changing View...")

            test = launch.mod.get("{}".format(element[0]))

            print(launch.mod.get("Add-Computer")[1])
            for x in test[2]:
                launch.layout.append([Sg.InputText("{}".format(str(x)))])

            launch.layout_finals = [[Sg.DropDown(launch.dropdown_list,
                                           enable_events=True,
                                          default_value=v[0])],[Sg.Button(
                    "Execute", size=(25,1))],
                             [Sg.Column(launch.layout_final), Sg.Column(
                        launch.layout), Sg.Text(
                        launch.mod.get("{}".format(element[0]))[1],
                                     size=(800, 200), auto_size_text=True),
                              Sg.DropDown(
                                      launch.mod.get("{}".format(element[0]))[
                                          3], key="dd_ex")]]
            mainWindow = Sg.Window("pswrapped",
                                   layout=launch.layout_finals).Finalize()



    #print(v, old_v)
    #print(v)
    old_v = v

    if b == "Execute":
        run = Posh()

    if b == "exit":
        quit()

    if b != Sg.TIMEOUT_KEY:
        pass

    if b is None:
        break
