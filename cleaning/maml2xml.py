# utilize on MS Help MAML dump
# must clear "maml:", "command:", "dev:", "<para>", "</para>"

with open("ps_man.xml") as y:
    data = y.read()
    res = data.replace("</para>", "")

with open("ps_man_final.xml", 'w') as file:
    file.write(res)
