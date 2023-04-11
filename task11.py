a = 8
b = 'autotest'

def list(name):
    if len(name) > 36:
        raise ValueError('Количество символов больше 36')
    if len(name) < 36:
        raise ValueError('Количество символов меньше 36')
    else:
        name = f'{b} {name[a:]}'
    print(name)

list('ac7fa857-2778-421f-8950-e8879002c4f0')
