#Date:05/09/2024
#Topic:
#Author:Shokhnur
    
# a=float(input('Juft son kiriting:'))
# if a%2==0:
#     print('Rahmat!')
# else:
#     print('Bu juft son emas!')
# a=float(input('Yoshiz nechida:'))
# if a<=4 or a>=60:
#     narx=0
# elif a<=18:
#     narx=10000
# elif a>18:
#     narx=20000
# print(f'Siz uchun kirish narhi {narx} so\'m')
# for c in range(1):
#     a=float(input(f'{c+1}-sonni kiriting:'))
#     b=float(input(f'{c+2}-sonni kiriting:'))
# if a<b:
#     print(f'{a} kichik {b} dan')
# elif a>b:
#     print(f'{a} katta {b} dan')
# else:
#     print(f'{a} va {b} bir biriga teng!')
# mahsulotlar=['olma','nok','un','yog\'','uzum','makron','guruch','sabzi','piyoz','kartoshka']
# savat=[]
# for a in range(5):
#     c=input(f'{a+1}-mahsulotni kiriting\n')
#     savat.append(c)
# for b in range(5):
#     if savat[b] in mahsulotlar:
#         print(f'Bizda {savat[b]} mahsulotidan bor')
#     else:
#         print(f'Uzr bizda {savat[b]} mahsulotidan mavjud emas')
mahsulotlar=['olma','nok','un','yog\'','uzum','makron','guruch','sabzi','piyoz','kartoshka']
mavjud_mahsulotlar=[]
mavjud_emas=[]
for a in range(5):
    c=input(f'{a+1}-mahsulotni kiriting\n')
    if c in mahsulotlar:
        mavjud_mahsulotlar.append(c)
    else:
        mavjud_emas.append(c)
if mavjud_emas==0:
    print('Siz so\'ragan barcha mahsulotlar mavjud bizda!')
else:
    for a in range(5):
     print('Bizda',mavjud_emas[a],'mahsulotlar mavjud emas')