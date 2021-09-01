import os #operating system

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f: #將下面讀取檔案功能全部移上來
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products
# 讀取檔案檢查檔案有沒有已經存在 #import os
# def read_file(filename): #定義成函式，程式碼可以合起來，再考慮寫進參數(filename)跟return，將函式下product.csv改成filename
#     if os.path.isfile(filename): #使用os的path檢查路徑功能的isfile功能:有沒有存在
#         print('GOOD有找到檔案')
#         #此函式  檢查檔案 / 讀取檔案
#         #此函式有做兩件事情，函式最好是一個函式一件事情，所以把讀取檔案拉出來
#         # with open(filename, 'r', encoding='utf-8') as f: #將下面讀取檔案功能全部移上來
#         #     for line in f:
#         #         if '商品,價格' in line:
#         #             continue
#         #         name, price = line.strip().split(',')
#         #         products.append([name, price])
#         print(products)
#     else:
#         print('找不到檔案哦!!!')
#     return products #def函式後，return products才能繼續使用
#     # 讀取檔案
#     # with open('products.csv', 'r', encoding='utf-8') as f: #要用utf-8編碼讀取檔案
#     #     for line in f:
#     #         if '商品,價格' in line: #if line字串裡面，有 商品,價格，就執行continue
#     #             continue #continue為強制執行下一回圈，不繼續做下面的code (continue / break只能寫在迴圈裡)
#     #         name, price = line.strip().split(',') #strip切掉換行\n 跟 前後空格 #split分割字串中的,符號
#     #         # name = s[0] #此兩行可以直接寫在上一行裡面，用,切割成幾塊，分別對應幾個變數
#     #         # price = s[1]
#     #         products.append([name, price])
#     #         #print(s) #將字串用split切割完後，變成清單
#     # print(products)

# 讓使用者輸入
def user_input(products):
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
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products: #for迴圈，把清單中的小清單，一次一次取出來
        print(p[0], '的價格是', p[1]) #小清單裡面的[0][1]的位置
    #return products 不用return任何東西，因為未改變任何東西

# 寫入檔案
def write_file(filename, products): #寫入參數filename代替products.csv，products也是外部參數需寫入
    with open(filename, 'w', encoding='utf-8') as f: #寫入檔案模式，沒有檔案就會新增，w寫入的意思，打開而已
        f.write('商品,價格\n')
        for p in products: #從products裡面將P一行一行拿出來，代表說有幾行執行幾次
            f.write(p[0] + ',' + p[1] + '\n') #寫入檔案內容，string的加法
    # 'abc' + '123' = 'abc123'
    # 'abc' * 3 = 'abcabcabc'
    #沒有改變，不用回傳return

def main(): #全部寫完後，定義一個main function
    #檢查檔案不用寫成函式，因為一行式很簡單
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('GOOD!!!~~~有找到檔案')
        #products = read_file('products.csv')
        products = read_file(filename)
    else:
        print('找不到檔案哦!!!')

    #products = read_file('products.csv') #呼叫出函式，才可以使用，放入參數filename，再存回products
    products = user_input(products)
    print_products(products)
    #write_file('products.csv', products)
    write_file(filename, products)


main()