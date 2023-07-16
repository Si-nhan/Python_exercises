'''
numbers_list = input('Enter numbers: ').split()
odd_numbers = 0

for number in numbers_list:
    odd_numbers += int(number) % 2
    
even_numbers = len(numbers_list) - odd_numbers
print(f'The number of even numbers is {even_numbers}')
'''

'''
Digit  = input('Enter a number: ')
print(Digit.isdigit())
'''

#Đảo ngược câu trong đoạn văn bản
'''
string = input()
list = string.split()
new_list = list[::-1]
print(' '.join(new_list))
'''

#In ra "Learn_Python_is_Easy"
''''
raw_string = "###Learn Python is Easy!!!"
left_erase = raw_string.lstrip('#')
right_erase = left_erase.rstrip('!')
list = right_erase.split()
print('_'.join(list))
'''

#Hóa đơn siêu thị
'''
name1 = 'orange'
price1 = 150
unit1 = 2

name2 = 'grape'
price2 = 130
unit2 = 23

tprice = price1 + price2
discount=15
fprice = tprice - discount

print("{0}      {1}            {2}   {3}".format("S.no", "Product", "Unit", "Price"))
print("{0}      {1}            {2}   {3}".format(0, name1, unit1, price1))
print("{0}      {1}            {2}   {3}".format(1, name2, unit2, price2))
print("{0}                           {1}".format("Discount", discount))
print("{0}                           {1}".format("Total", fprice))
'''

#Tổng của các phần tử lẻ trong danh sách
'''
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_odd = []
tong = 0 
for i in arr:
    if i % 2 == 1:
        arr_odd.append(i)
print("tổng =", sum(arr_odd))
'''

#Tìm từ dài nhất trong câu
'''
string = input()
list = string.split()
max = len(list[0])
chosen_word = list[0]

for word in list:
    if max < len(word):
        max = len(word)
        chosen_word = word
print("The longest string is", "\""+chosen_word+"\"", "with", max, "characters")
'''

#Đếm số từ trong đoạn văn
'''
string_raw = input()
list = string_raw.split()
number_of_words = len(list)
print("Số từ có trong câu là:", number_of_words)
'''

#Mã Caesar
'''
text = input() #Nhận đoạn văn bản rõ
k = int(input()) # Nhận khóa nhập vào từ bàn phím, ép kiểu về số nguyên
list = []
for letter in text:
    if 65 <= ord(letter) <= 90:
        code = (ord(letter) - 65 + k) % 26
        list.append(chr(code + 65))
    elif 97 <= ord(letter) <= 122:
        code = (ord(letter) - 97 + k) % 26
        list.append(chr(code + 97))
print(''.join(list))
'''

#Tìm ước của một số
'''
n = int(input())
count = 0
list = []
for i in range(1, n+1):
  if n % i == 0:
    count += 1
    list.append(str(i))
list.append('!')
print(n, "have", count, "divisors")
print("They are", ' '.join(list))
'''

#Tìm ước chung lớn nhất
'''
a = int(input())
b = int(input())
for i in range(a if a<b else b, 0, -1):
  if (a % i == 0) and (b % i == 0):
    print("The Greatest Common Divisor of", a, "and", b, "is:", i)
    break
'''

#Đếm số nguyên tố không lớn hơn n
'''
n = int(input())
count = 1
for i in range(3, n+1):
  for k in range(2, i):
    if i % k == 0:
      break
  else:
    count += 1
print(count)
'''

#Kiểm tra các số đầu vào:
'''
a = int(input("Nhập số a: "))
tong = a
while a > 0:
    a = int(input("Nhập số a: "))
    tong += a if a > 0 else 0
print("Tổng của các số dương đã nhập vào là:", tong)
'''

#Tìm số Armstrong:
'''
def check_Armstrong(a):
    digits_number = len(str(a))
    sum = 0
    for digit in str(a):
        sum += int(digit)**digits_number
    if sum == a:
        return True 
    else:
        return False
    
n = int(input("Nhập số n: "))
list = []
for i in range(1, n+1):
    if check_Armstrong(i) == True:
        list.append(i)
print('Dãy số Armstrong trong đoạn từ 1 đến', n, 'là', list)
'''

#Số hoàn hảo:
'''
def so_hoan_hao(a, b):
    list = []
    for so_bi_chia in range(a, b+1):
        tong = 0
        for so_chia in range(1, so_bi_chia):
            if so_bi_chia % so_chia == 0:
                tong += so_chia
        if tong == so_bi_chia:
            list.append(str(so_bi_chia))
    print(', '.join(list))
    
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print("Dãy các số hoàn hảo trong đoạn từ", a, "đến", b, "là:")
so_hoan_hao(a, b)
'''

#Khoảng cách Manhattan
'''
x=[1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9]
y=[9.8, 8.7, 7.6, 8.5, 5.4, 4.3, 3.2, 2.1]

def manhattan(x, y):
    tong = 0
    for i in range(len(x)):
        tong += abs(x[i] - y[i])
    return tong

print(manhattan(x, y))
'''

#Đọc chữ số
'''
sample_list = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", 'chín']
made_list = []

def docso(num):
    while num/10 > 0:
        made_list.append(sample_list[num % 10])
        num = int(num/10)
    number_is_read = ' '.join(made_list[::-1])
    print(number_is_read)

num = int(input("Nhập số cần đọc: "))
docso(num)
'''


#Kiểm tra email hợp lệ
'''
email=input('Enter an email: ')

def check_email(email):
    after_symbol = email.index('@') + 1
    email_domain = email[after_symbol:]
    ending_char = email[-1]
    if not email[0].isalpha():
        return False
    elif '@' not in email:
        return False
    elif email_domain.count('.') != 1:
        return False
    elif ending_char == '.':
        return False
    else:
        return True
    
if check_email(email) == True:
    print('Valid email')
else:
    print('Invalid email')
'''


#Hàm với tham số mặc định
'''
def duplicate(word, num=1):
    result = word*num
    result += '!!!'
    return result

#call function with default argument
no_num = duplicate("TEK4.VN ")
#call function with variable argument
with_num = duplicate("TEK4.VN ", 5)

#print result
print(no_num)
print(with_num)
'''

#Hàm với nhiều tham số mặc định
'''
def duplicate(word, num = 1, upper = False):
    dup_word = word*num
    if upper is True:
        result = dup_word.upper() + '!!!'
    else:
        result = dup_word + '!!!'
    return result

#call function with default argument
with_one_argument = duplicate("tek4.vn")
#call function with two argument
with_two_argument = duplicate("tek4.vn", 4)
#call function with full argument
with_full_argument = duplicate("tek4.vn", 4, True)

#print result
print(with_one_argument)
print(with_two_argument)
print(with_full_argument)
'''

#Hàm với số lượng đối số tùy ý
'''
def printf(*args):
    str=''
    count=0
    for word in args:
        str += word
        count+=1
    print(str)
    return count

one_word = printf("learn")
print(one_word)

many_words = printf("learn","python", "with","tek4.vn")
print(many_words)
'''

#Dãy Fibonacci
'''
def fibonacci(n):
   if n <= 1:
       return 1
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

n=int(input('Nhập số n: '))
list=[]
for i in range(n):
    list.append(fibonacci(i))
print(list)
'''

#Tỉ lệ vàng
'''
def fibonacci(n):
    f0=f1=1
    for i in range(3, n+1):
        fn=f0+f1
        f0=f1
        f1=fn
    return fn

n=int(input())
golden_rate=fibonacci(n+1)/fibonacci(n)
print('Golden_rate =', golden_rate)
'''

#Dùng hàm lamda để tạo câu từ danh sách
'''
string_join = lambda s: " ".join(s)

list = ["learn", "python", "with", "tek4.vn"]
print(string_join(list))
'''

#Dùng hàm map kết hợp hàm lambda tính tổng các hàng ma trận
'''
matrix = [
    [1.2,2.5,1.8],
    [2.1,1.2,4.5],
    [5.2,3.3,3.3],
    [4.2,3.2,2.3]
    ]

result = map(lambda a: sum(a), matrix)
print(list(result))
'''

#Dùng hàm filter kết hợp hàm lambda lọc độ tuổi
'''
age=[18,21,11,2,-2,190,34,17,25,38,26,-21,200,-28,28,19]
result = filter(lambda age: age>=15 and age<=130, age)
result_list= list(result)
print(result_list)
'''

#Tìm tuple với tất cả các phần tử chia hết cho số K
'''
K = int(input('Nhập số K: '))
test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
list = []
for tuple in test_list:
    for i in tuple:
        if i % K != 0:
            break
    else:
        list.append(tuple)
if list!=[]:
    print('Các tuple với tất cả phần tử chia hết cho', K, 'là', list)
else:
    print('Không có tuple nào có tất cả phần tử chia hết cho', K)
'''
 
#Tìm kiếm vị trí xuất hiện của phần tử
'''
list = input().split()
tuple = tuple(list)
print(tuple)
if tuple.count('30') == 0:
    print('Không tìm thấy số 30!')
elif tuple.count('30') == 1:
    print('Tìm tháy số 30 1 lần ở vị trí số', tuple.index('30')+1)
else:
    print('Tìm thấy số 30', tuple.count('30'), 'lần ở vị trí đầu tiên là', tuple.index('30')+1, 'và ở vị trí cuối cùng là', tuple.index('30',-1,)+1)
'''

#Dùng unpacking để đổi chỗ
'''
my_list1 = [1,2,5,4,3,6,7,9,8]
my_list2 = [1,2,4,5,3,6,9,7,8]
my_list1, my_list2 = my_list2, my_list1
print(my_list1)
print(my_list2)
my_list2[2], my_list2[3] = my_list2[3], my_list2[2]
print(my_list1)
print(my_list2)
'''

#Thao tác trên set
'''
my_list = [1,2,3,1,2,3,4,1,3,5,6,7,1,3,4,7,8,9,4,6,7,9]
my_list2 = [11,22,33,44,55,66,11,33,55]
sample_set = set(my_list)
print(sample_set)
sample_set.update(my_list2)
sample_set.remove(max(sample_set))
sample_set.remove(min(sample_set))
print(sample_set)
'''

#Unpacking trong vòng for
'''
points=[(1.2,1.5),(-3.1,5.6),(4.5,2.6),(1.4,6.8),(2.1,-8.4)] 
x, y= points[0]
max= x+y
for x, y in points:
    if max<abs(x)+abs(y):
        max=abs(x)+abs(y)
print("Điểm (", x,",",y,") có khoảng cách lớn nhất tới gốc tọa độ:", max)
'''

#Unpacking trong hàm
'''
list=input().split()
print(list)
def statistic(list):
    sum=0
    for i in list:
        sum+=float(i)
    mean=sum/len(list)
    a=0
    for k in list:
        a+=(mean-float(k))**2
    return mean, a/len(list)

a, b=statistic(list)
print('Mean:', a)
print('Variance:', b)
'''
    
