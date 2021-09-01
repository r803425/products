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

# print(products[0][0]) #先大清單，依序小清單 位置
# print(products[0][1])
# print(products[1][0])
# print(products[1][1])
for p in products: #for迴圈，把清單中的小清單，一次一次取出來
    print(p[0], '的價格是', p[1]) #小清單裡面的[0][1]的位置

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding='utf-8') as f: #寫入檔案模式，沒有檔案就會新增，w寫入的意思，打開而已
    f.write('商品,價格\n')
    for p in products: #從products裡面將P一行一行拿出來，代表說有幾行執行幾次
        f.write(p[0] + ',' + p[1] + '\n') #寫入檔案內容，string的加法