from PIL import Image ,ImageFilter ,ImageEnhance
import pytesseract

im =Image.open('BILL.png' )
text = pytesseract.image_to_string(im ,lang='eng')
p=[{} for i in range(5)]
q=[{} for i in range(5)]
z=[{} for i in range(5)]
text = (text).split()
print(text)
n=len(text)
print(n)
j=7
for i in range(0,(n-7)//3):
    print(i)
    p[i]=text[j]
    j=j+1
    q[i]=text[j]
    j=j+1
    z[i]=text[j]
    j=j+1
print("products")
for m in range( 0,i):
    print(m+1,p[m])
print("rate")
for m in range( 0,i):
    print(m+1,q[m])
print("rate of total")
for m in range( 0,i):
    print(m+1,z[m])
print("total price",z[m+1])

