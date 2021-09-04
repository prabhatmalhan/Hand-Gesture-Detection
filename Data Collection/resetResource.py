from EditJson import EditConfig


def resetConfig():
    p = int(input('enter user id : '))
    for i in range(22):
        x = EditConfig('./Resources/'+str(i)+'/info.json').readConfig()
        x['count'] = str(p*240)
        EditConfig('./Resources/'+str(i)+'/info.json').writeConfig(x)
