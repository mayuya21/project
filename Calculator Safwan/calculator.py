def Welcome():
    print('''
サフワンの計算機へようこそ
''')

def calculate():
    operation = input('''
完了したい数値演算を入力してください:
+ = 足し算
- = 引き算
* = 掛け算
/ = 割り算
''')

    number_1 = int(input('1番目の番号を入力してください: '))
    number_2 = int(input('2番目の番号を入力してください: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
  
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('有効な演算子を入力していない場合は、プログラムをもう一度実行してください.')

    again ()
    
def again():
    calc_again = input('''
もう一度計算しますか？
「はい」の場合は「Y]、「いいえ」の場合は「N]を入力してください！
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('じゃあまたね ^_^')
    else:
        again()

Welcome ()
calculate()
