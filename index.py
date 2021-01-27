import random
import function
items = {1:'Batu', 2:'Gunting', 3:'Kertas'}
print('')
print("Silahkan Pilih :")
for item in items:
    print(str(item) + '. ' + items[item])

print('     ')
hand = int(input("Anda pilih apa :  "))

if(hand > 3):
    print('Pilihan tidak ada')
    print('Komputer menang')

else:
    hand_computer = random.randint(1,3)
    print("Anda memilih      : " + items[hand]) 
    print("Komputer  memilih : " + items[hand_computer]) 

    result = function.hasil(hand, hand_computer)
    
    print('   ')
    print("Hasilnya anda " + result)





