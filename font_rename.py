import os

from fontTools.ttLib import TTFont

"""
PlatformID == 1
NameRecord.nameID   |   String ID
record.nameID==0        Copyright
record.nameID==1        Family
record.nameID==2        Styles(SubFamily): Regular/Bold/Italic/Bold Italic
record.nameID==3        UniqueID
record.nameID==4        Fullname: {family} {style}
record.nameID==5        Version
record.nameID==6        Postscript Fullname: {family}-{style} no space 
record.nameID==16       Preferred Family, just same as Styles for regular and bold weight
record.nameID==17       Preferred Styles, just same as Styles for regular and bold weight

"""


def rename_font(filename, *, family, weight, style, version):
    global folder
    path = folder
    """style: Regular/Bold/Italic/Bold Italic"""
    usWeightClass_map = {
        "Regular": 400,
        "Bold": 700,
    }
    usWeightClass = usWeightClass_map[weight]

    id1 = f'{family}'
    id2 = f'{style}'
    id4 = f'{family} {style}'
    id6 = f'{family}-{style.replace(' ', '')}'
    # UniqueID
    id3 = f'{family} {style} Version {version}'
    id16 = id1
    id17 = id2
    id19 = f'printf("Hello, {family}!")'

    full_path = os.path.join(path, filename)
    tt = TTFont(full_path)

    tt['OS/2'].usWeightClass = usWeightClass

    name_records = tt["name"].names

    for record in name_records:
        print(f'{record.nameID}: {record}')

    for i in range(len(name_records) - 1, -1, -1):
        record = name_records[i]
        if record.nameID == 1:
            record.string = id1
        elif record.nameID == 2:
            record.string = id2
        elif record.nameID == 4:
            record.string = id4
        elif record.nameID == 6:
            record.string = id6
        elif record.nameID == 3:
            record.string = id6
        elif record.nameID == 3:
            record.string = id3
        elif record.nameID == 16:
            record.string = id16
        elif record.nameID == 17:
            record.string = id17
        elif record.nameID == 19:
            record.string = id19

    new_font_file = f'{id6}.ttf'
    tt.save(os.path.join(path, new_font_file))


folder = 'C:\\Users\\zhimoe\\Documents'
v = '2.611'
fm = 'WenKaiCode'
rename_font('LXGWBrightCode-Light.ttf', family=fm, weight='Regular', style='Regular', version=v)
rename_font('LXGWBrightCode-LightItalic.ttf', family=fm, weight='Regular', style='Italic', version=v)
rename_font('LXGWBrightCode-Regular.ttf', family=fm, weight='Bold', style='Bold', version=v)
rename_font('LXGWBrightCode-Italic.ttf', family=fm, weight='Bold', style='Bold Italic', version=v)
# 测试根据当前的