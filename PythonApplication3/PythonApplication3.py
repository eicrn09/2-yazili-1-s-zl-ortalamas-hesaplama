yazili1=float(input('1.Yazili: '))
yazili2=float(input('2. yazili '))
sozlu=float(input('sozlu notu: '))
ort=float((yazili1+yazili2+sozlu)/3)
if ort<=24:
    print("Ortalamaniz "+str(ort)+' '+'not degeriniz:0')
if ort>24 and ort<=44:
     print("Ortalamaniz "+str(ort)+' '+'not degeriniz:1')
if ort>44 and ort<=54:
     print("Ortalamaniz "+str(ort)+' '+'not degeriniz:2')
if ort>54 and ort<=69:
    print("Ortalamaniz "+str(ort)+' '+'not degeriniz:3')
if ort>69 and ort<=84:
    print("Ortalamaniz "+str(ort)+' '+'not degeriniz:4')
if ort>84 and ort<=100:
     print("Ortalamaniz "+str(ort)+' '+'not degeriniz:5')
if ort>100 or ort<0:
    print('Girdiginiz notlar hatali kontrol ediniz.')