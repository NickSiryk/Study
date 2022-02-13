while True:
    tel_num = input('Print Your phone number here: +38').strip()
    if not tel_num.isdigit():
        print('There is a letter. Try, please, one more time!')
    elif len(tel_num) < 10:
        print('Too short. Try, please, one more time!')
    elif len(tel_num) > 10:
        print('Too long. Try, please, one more time!')
    else:
        print('Ok, I\'ll remember: +38('+tel_num[0:3]+')'+tel_num[3:6]+'-'+tel_num[6:8]+\
              '-'+tel_num[8:10])
        question = input('Is it correct? (Y/N): ')
        if question == 'Y':
            print('See You!')
            break
        else:
            print('Somewhere was a mistake. We will try one more time!')
            continue
