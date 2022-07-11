month=int(input())
if month>12:
    print('Error')
if 0<month<3:
    print('Winter')
if 2<month<6:
    print('Spring')
if 5<month<9:
    print('Summer')
if 8<month<12:
    print('Autumn')
if month==12:
    print('Winter')