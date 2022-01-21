
girdi1 = float(input("Lütfen matematik notunuzu giriniz: "))
girdi2 = float(input("Lütfen ingilizce notunuzu giriniz: "))
girdi3 = float(input("Lütfen cografya notunuzu giriniz: "))
girdi4 = float(input("Lütfen fizik notunuzu giriniz: "))
girdi5 = float(input("Lütfen kimya notunuzu giriniz: "))

notort = ((girdi1 + girdi2 + girdi3 + girdi4 + girdi5) / 5)

if notort >= 90 \
  and (girdi1 >= 85 and girdi2 >= 85 and girdi3 >= 85 and girdi4 >= 85 and girdi5 >= 85):

  print("Tebrikler Not Ortalamaniz: ", notort, "AA", " ve Onur belgesine hak kazandiniz")

elif notort >= 90 \
  and (girdi1 < 85 or girdi2 < 85 or girdi3 < 85 or girdi4 < 85 or girdi5 < 85):
  print("Tebrikler Not Ortalamaniz: ", notort, "AA", " Ancak Onur belgesine hak kazanamadiniz")

elif 80 <= notort < 90:
  if girdi1 >= 75 and girdi2 >= 75 and girdi3 >= 75 and girdi4 >= 75 and girdi5 >= 75:
    print("Tebrikler Not Ortalamaniz: ", notort, "AB", " 1000 Euro hediye ceki kazandiniz")

  else:
    print("Tebrikler Not Ortalamaniz: ", notort, "AB")
    
elif 70 <= notort <= 80:
  if girdi1 >= 70 and girdi2 >= 70 and girdi3 >= 70 and girdi4 >= 70 and girdi5 >= 70:
    print("Tebrikler Not Ortalamaniz: ", notort, "BB", " 500 Euro hediye ceki kazandiniz")

  else:
    print("Tebrikler Not Ortalamaniz: ", notort, "BB")

elif 60 <= notort < 70:
  print("Not ortalamaniz:", notort, "BC")

elif 50 <= notort < 60:
  print("Not ortalamaniz:", notort, "CC")

elif 40 <= notort < 50:
  print("Not ortalamaniz:", notort, "DD")

elif notort < 40 \
  or (girdi1 < 40 or girdi2 < 40 or girdi3 < 40 or girdi4 < 40 or girdi5 < 40):
  print("Üzgünüz not Ortalamaniz: ", notort, "FF", "Sinif tekrari") 
