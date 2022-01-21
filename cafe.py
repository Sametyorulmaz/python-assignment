para1 = float(input("Lütfen para atiniz: "))

print("Merhaba hosgeldiniz. Güncel bakiyeniz: ", para1)



if para1 >= 1.50:
  soru = input("Cay mi istersiniz kahve mi?").lower().strip()
  
  if soru == "cay":
    print("Cayiniz hazirlaniyor. Buyrun para üstünüz:", para1 - 1, "Euro")

  elif soru == "kahve":
    print("Kahveniz hazirlaniyor. Buyrun para üstünüz:", para1 - 1.50, "Euro")

  else:
    print("Üzgünüz buyrun para üstünüz:", para1, "Euro")







elif 1 <= para1 < 1.50:
  soru = input("Bakiyeniz ile sadece cay alabilirsiniz. Cay ister misiniz?").lower()

  if soru == "evet":
    print("Cayiniz hazirlaniyor. Buyrun para üstünüz:", para1 - 1, "Euro")

  elif soru == "hayir":
    print("Tesekkür ederiz buyrun para üstünüz:", para1, "Euro")

  else:
    print("Üzgünüz buyrun para üstünüz:", para1, "Euro")






elif para1 < 1:
  soru = input("Para eklemek istermisiniz bakiyeniz yetersiz ?").lower()

  if soru == "hayir":
    print("Tesekkür ederiz buyrun para üstünüz:", para1, "Euro")

  elif soru == "evet":
    para2 = float(input("Lütfen para ilave ediniz:"))

    if para1 + para2 >= 1.50:
      soru = input("Cay mi istersiniz kahve mi?").lower().strip()
      
      if soru == "kahve":
        print("Kahveniz hazirlaniyor. Buyrun para üstünüz:", para1 + para2 - 1.50, "Euro")

      elif soru == "cay":
        print("Cayiniz hazirlaniyor. Buyrun para üstünüz:", para1 + para2 - 1, "Euro")

      else:
        print("Üzgünüz buyrun para üstünüz:", para1 + para2, "Euro")

    elif para1 + para2 < 1:
      print("Üzgünüz buyrun para üstünüz:", para1 + para2, "Euro")

    elif 1 <= para1 + para2 < 1.50:
      soru = input("Parani ile sadece cay alabilirisniz. Cay ister misiniz?? ").lower()

      if soru == "hayir":
        print("Tesekkürler buyrun para üstünüz:", para1 + para2, "Euro")

      elif soru == "evet":
        print("Cayiniz hazirlaniyor. Buyrun para üstünüz:", para1 + para2 - 1, "Euro")

      else:
        print("Üzgünüz buyrun para üstünüz:", para1 + para2, "Euro")

  else:
    print("Üzgünüz buyrun para üstünüz:", para1, "Euro")

else:
  print("Üzgünüz buyrun para üstünüz:", para1, "Euro")     
