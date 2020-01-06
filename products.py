import os #operating system

#檢查檔案是否存在
def check_file(filename):
    products = []
    if os.path.isfile(filename):
        #讀取檔案
        with open(filename, 'r', encoding = 'utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name, price])
    else:
        with open('products.csv', 'w', encoding = 'utf-8') as f:
            f.write(products)
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    products = check_file(filename)
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()