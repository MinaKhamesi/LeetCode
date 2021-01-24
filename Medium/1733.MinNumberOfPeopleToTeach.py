def minimumTeaching(n , languages, friendships):
    cant_communicates = {}
    for p1,p2 in friendships:
        can_communicate = False
        for l in languages[p1 - 1]:
            if l in languages[p2 - 1]:
                can_communicate = True
        if not can_communicate:
            cant_communicates[p1] = True
            cant_communicates[p2] = True
    if not len(cant_communicates): return 0
    
    langs = {}
    for p in cant_communicates:
        for l in languages[p - 1]:
            if l not in langs:
                langs[l] = 0
            langs[l] += 1
    return len(cant_communicates) - max(langs.values())