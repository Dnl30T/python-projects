print('---------------Menu---------------')
print('|.cod.|.....Juices....|..price..|')
print('|.001.|......grape....|..$9.00..|')
print('|.002.|.strawberry....|..$8.00..|')
print('|.003.|.....orange....|..$3.00..|')
print('|.004.|..pineapple....|..$0.50..|')
print('|..(1)add............(0)close...|')

stop = False
index = 0
juices_amount = 0
final_price = 0

def addJuice(index):
    prices = {1 : 9.00, 2 : 8.00, 3 : 3.00, 4 : 0.50}
    return prices[index]

while stop == False:
    
    index = int(input('Insert your operation: '))

    if(index == 1):
        juices = {'grape' : 1, 'strawberry' : 2, 'orange' : 3, 'pineapple' : 4}
        juices_amount+=1
        x = input('add a juice: ')
        final_price += addJuice(juices[x])

    elif(index != 1):
            stop = True

print('Juices sold: ', juices_amount)
print('price total: ', final_price)