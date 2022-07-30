medida = float(input("Digite uma medida em metros para ser convertida: "))
km = medida * 1000
hm = medida * 100
dam = medida * 10
mm = medida / 1000
cm = medida / 100
dm = medida / 10

print("{} metros equivale a {:.0f} Quilômetros {:.0f} Hectômetros {:.0f} Decâmetros "
"{} Milímetros {} Centímetros {} Decímetros".format(medida, km, hm, dam, mm, cm, dm))

