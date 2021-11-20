# -*- coding: utf-8 -*-

numbers = {
    1: "واحد",
    2: "اثنين",
    3: "ثلاثة",
    4: "اربعة",
    5: "خمسة",
    6: "ستة",
    7: "سبعة",
    8: "ثمانية",
    9: "تسعة",
    10: "عشرة",
}

numbers2 = {
    1: "عشر",
    2: "عشرون",
    3: "ثلاثون",
    4: "اربعون",
    5: "خمسون",
    6: "ستون",
    7: "سبعون",
    8: "ثمانون",
    9: "تسعون",
}

numbers3 = {
    1: "مئة",
    2: "مئتان",
    3: "ثلاثمائة",
    4: "اربعة مائة",
    5: "خمس مائة",
    6: "ستة مائة",
    7: "سبعة مائة",
    8: "ثماني مائة",
    9: "تسع مائة",
}

extensions = {
    1: "الف",
    2: "مليون",
    3: "مليار",
    4: "تريليون"
}


def get_first(lis,i=0):
    string = ""
    first = numbers.get(int(lis[0]),None)
    ext = extensions.get(i, None)
    if i >= 1:
        string = "%s %s" % (first,ext)
    else:
        string = first
    return string


def get_second(lis,i=0):
    string = ""
    first = numbers.get(int(lis[0]),None)
    second = numbers2.get(int(lis[1]),None)
    ext = extensions.get(i, None)

    if i >= 1:
        if first is None:
            string = "%s %s" % (second,ext)

        if second is None:
            string = "%s %s" % (first,ext)

        if first is not None and second is not None and int(lis[1]) == 1:
            string = "%s %s %s" % (first, second,ext)

        if first is not None and second is not None and int(lis[1]) > 1:
            string = "%s و %s %s" % (first, second,ext)
    else:
        if first is None:
            string = second

        if second is None:
            string = first

        if first is not None and second is not None and int(lis[1]) == 1:
            string = "%s %s" % (first, second)

        if first is not None and second is not None and int(lis[1]) > 1:
            string = "%s و %s" % (first, second)


    return string


def get_third(lis,i=0):
    string = ""
    first = numbers.get(int(lis[0]), None)
    second = numbers2.get(int(lis[2]), None)
    third = numbers3.get(int(lis[1]), None)
    ext = extensions.get(i,None)

    if first is None:
        if ext is not None:
            string = "%s %s و %s" % (third, ext, second)
        else:
            string = "%s و %s" % (third, second)

    if third is None :
        string = get_second([lis[0],lis[2]],0)

    if third is None and second is None:
        string = get_first(lis[0],0)

    if second is None and third is not None:
        if first is not None:
            if ext is not None:
                string = "%s %s و %s" % (third, ext, first)
            else:
                string = "%s و %s" % (third, first)
        else:
            if ext is not None:
                string = "%s %s " % (third, ext)
            else:
                string = third

    if first is not None and second is not None and third is not None:
        if ext is not None:
            string = "%s و %s" % (third, get_second([lis[0], lis[2]],i))
        else:
            string = "%s و %s" % (third, get_second([lis[0], lis[2]],0))

    return string


def split_list(lis, nu):
    rev = list(reversed(lis))
    spiltted = []
    for x in range(0, len(rev), nu):
        spiltted.append(rev[x:x + nu])
    return spiltted


def change_order(lis):
    final_list = []
    for x in lis:
        if len(x) == 3:
            list_sp = list(x)
            list_sp[1], list_sp[2] = list_sp[2], list_sp[1]
            final_list.append(list_sp)
        else:
            list_sp = list(x)
            final_list.append(list_sp)
    return list(final_list)


def Convert(number):
    spiltted = split_list(str(number), 3)
    orderd = change_order(spiltted)
    final = []
    if len(str(number)) > 13:
        return number

    for i, x in enumerate(orderd):
        sub = get_first(x,i) if len(x) == 1 else get_second(x,i) if len(x) == 2 else get_third(x,i) if len(x) == 3 else None
        if sub != None:
            final.append(sub)

    res = " و".join(list(reversed(final)))

    return res



# print(Convert(7999113555222))
#سبعة تريليون وتسع مائة و تسعة و تسعون مليار ومئة و ثلاثة عشر مليون وخمس مائة و خمسة و خمسون الف ومئتان و اثنين و عشرون