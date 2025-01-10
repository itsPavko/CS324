total = 0
count = 0
avg = 0
num = None


while (num != 0):
    try:
        num = float(input('(Unesite 0 ako zelite da zavrsite:) Unesite ocenu: '))
        if num == 0:
            break 
        if num >= 6: 
            count += 1
            total += num
            avg = total / count
            print(f'Trenutni prosek: {avg:.2f}')
        else:
            print('Ocena mora biti veca od 6.')
    except ValueError:  
        print('Greska. Unesite validan broj.')
        count = count + 1
        total = total + num
        avg = total / count
        print(avg)
    except:
        print('Greska.')
        continue




print('Prosek: ' + str(avg) )