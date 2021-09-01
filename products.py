products = []
while True:
    name = input('請輸入"名稱": ')
    if name == 'q':
        break
    #products.append(name)

    price = input('請輸入"價格": ')
    
    # p = [] #變成二維清單，先假設有一個小清單，之後再放到大清單裡面
    # p.append(name)
    # p.append(price)
    # p = [name, price] #上面3行可以改寫成這一行

    # products.append(p) #二維清單，小清單放到大清單裡
    products.append([name, price]) #進階改寫成這樣

#print(products) #本來這是一維清單，只放了products名稱
print(products) #變成二維清單，清單中再放入清單，大清單裝小清單

print(products[0][0]) #先大清單，依序小清單 位置
print(products[0][1])
print(products[1][0])
print(products[1][1])