import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#mpl.rcParams['agg.path.chunksize'] = 1_000_000_000
#plt.rcParams['path.simplify_threshold'] = 0.0001



with open("C:/Users/Lenovo/Desktop/Excel/S_8.csv", "r") as f:
    icerik_2 = f.readlines() #readlines komutu listeye donusturuyor
    #for satir_2 in icerik_2:
        #print(satir_2, end=(""))
icerik_2 = np.array(icerik_2)
icerik_2 = icerik_2.astype(float)

#print("\n")
#print(icerik_2[0], type(icerik_2[0]))

def onlyAC_800():
    with open("C:/Users/Lenovo/Desktop/Excel/20210420_150303_800_ OnlyAC.csv", "r") as f:
        icerik = f.readlines()
    
    print("\n")
    icerik = np.array(icerik)
    icerik = icerik.astype(float)
    #print("\n")
    #print(icerik[0], type(icerik[0]))  
    max_value = max(icerik)
    min_value = min(icerik)
    V_pp = max_value + abs(min_value)
    print("AC Vmin değeri= " + str(min_value))
    print("AC Vmax değeri= " + str(max_value))
    print("AC Vpp değeri= " + str(V_pp))
   
    
    
    plt.plot(icerik_2, icerik, label='Gerilim')
    plt.xlabel('x 10**4 mikrosaniye')
    plt.ylabel('Genlik(V)')
    plt.title('AC')
    plt.legend()
    plt.show()


def onlyDC_080():
    with open("C:/Users/Lenovo/Desktop/Excel/20210330_175549_080_onlyDC.csv", "r") as f:
        icerik = f.readlines()
    
    print("\n")
    icerik = np.array(icerik)
    icerik = icerik.astype(float)
    #print("\n")
    #print(icerik[0], type(icerik[0]))
    max_value = max(icerik)
    min_value = min(icerik)
    V_pp = max_value + abs(min_value)
    print("DC Vmin değeri= " + str(min_value))
    print("DC Vmax değeri= " + str(max_value))
    print("DC Vpp değeri= " + str(V_pp))
    
    plt.plot(icerik_2, icerik, label='Gerilim')
    plt.xlabel('x 10**2 mikrosaniye')
    plt.ylabel('Genlik(V)')
    plt.title('DC')
    plt.legend()
    plt.show()

print("\n")
def only_eksiDC_110():
    with open("C:/Users/Lenovo/Desktop/Excel/S_16.csv", "r") as f:
        icerik_3 = f.readlines()
    
    print("\n")
    icerik_3 = np.array(icerik_2)
    icerik_3 = icerik_2.astype(float)
    
    with open("C:/Users/Lenovo/Desktop/Excel/20210420_153926_110_EksiDC.csv", "r") as f:
        icerik = f.readlines()
      
    icerik = np.array(icerik)
    icerik = icerik.astype(float)
    #print("\n")
    #print(icerik[0], type(icerik[0]))
    max_value = max(icerik)
    min_value = min(icerik)
    V_pp = max_value + abs(min_value)
    print("-DC Vmin değeri=" + str(min_value))
    print("-DC Vmax değeri=" + str(max_value))
    print("-DC Vpp değeri=" + str(V_pp))
   
    plt.plot(icerik_3, icerik, label='Gerilim')
    plt.xlabel('x 10**3 mikrosaniye')
    plt.ylabel('Genlik(V)')
    plt.title('-DC')
    plt.legend()
    plt.show() 
print("\n")
def AC_artı6KV_DC():
    with open("C:/Users/Lenovo/Desktop/Excel/20210420_150303_300_AC_artı_6kVDC.csv", "r") as f:
        icerik = f.readlines()
    
    print("\n")
    icerik = np.array(icerik)
    icerik = icerik.astype(float)
    #print("\n")
    #print(icerik[0], type(icerik[0]))
    max_value = max(icerik)
    min_value = min(icerik)
    V_pp = max_value + abs(min_value)
    print("AC+6kV_DC Vmin değeri= " + str(min_value))
    print("AC+6kV_DC Vmax değeri= " + str(max_value))
    print("AC+6kV_DC Vpp değeri= " + str(V_pp))
    
    plt.plot(icerik_2, icerik, label='Gerilim')
    plt.xlabel('x 10**5 mikrosaniye')
    plt.ylabel('Genlik(V)')
    plt.title('AC +6kV DC')
    plt.legend()
    plt.show()    
print("\n")
def AC_artı6KV_DC_800():
    with open("C:/Users/Lenovo/Desktop/Excel/20210420_150432_800_AC_artı_6kVDC.csv", "r") as f:
        icerik = f.readlines()
    
    print("\n")
    icerik = np.array(icerik)
    icerik = icerik.astype(float)
    #print("\n")
    #print(icerik[0], type(icerik[0]))
    max_value = max(icerik)
    min_value = min(icerik)
    V_pp = max_value + abs(min_value)
    print("AC+6kV_DC_2 Vmin değeri= " + str(min_value))
    print("AC+6kV_DC_2 Vmax değeri= " + str(max_value))
    print("AC+6kV_DC_2 Vpp değeri= " + str(V_pp))
    
    plt.plot(icerik_2, icerik, label='Gerilim')
    plt.xlabel('x 10**4 mikrosaniye')
    plt.ylabel('Genlik(V)')
    plt.title('AC +6kV DC_2')
    plt.legend()
    plt.show()  
print("\n")   
def AC_eksi6KV_DC():   
    with open("C:/Users/Lenovo/Desktop/Excel/20210420_163107_040_AC_eksi_6kVDC.csv", "r") as f:
        icerik = f.readlines()
    
    print("\n")
    icerik = np.array(icerik)
    icerik = icerik.astype(float)
    #print("\n")
    #print(icerik[0], type(icerik[0]))
    max_value = max(icerik)
    min_value = min(icerik)
    V_pp = max_value + abs(min_value)
    print("AC-6kV_DC Vmin değeri= " + str(min_value))
    print("AC-6kV_DC Vmax değeri= " + str(max_value))
    print("AC-6kV_DC Vpp değeri= " + str(V_pp))
    
    plt.plot(icerik_2, icerik, label='Gerilim')
    plt.xlabel('x 10**5 mikrosaniye')
    plt.ylabel('Genlik(V)')
    plt.title('AC -6kV DC')
    plt.legend()
    plt.show()  
print("\n")
def AC_eksi6KV_DC_200():   
    with open("C:/Users/Lenovo/Desktop/Excel/20210420_163319_200_AC_eksi_6kVDC.csv", "r") as f:
        icerik = f.readlines()
    
    print("\n")
    icerik = np.array(icerik)
    icerik = icerik.astype(float)
    #print("\n")
    #print(icerik[0], type(icerik[0]))
    max_value = max(icerik)
    min_value = min(icerik)
    V_pp = max_value + abs(min_value)
    print("AC-6kV_DC_2 Vmin değeri= " + str(min_value))
    print("AC-6kV_DC_2 Vmax değeri= " + str(max_value))
    print("AC-6kV_DC_2 Vpp değeri= " + str(V_pp))
    
    plt.plot(icerik_2, icerik, label='Gerilim')
    plt.xlabel('x 10**5 mikrosaniye')
    plt.ylabel('Genlik(V)')
    plt.title('AC -6kV DC_2')
    plt.legend()
    plt.show()    

form = tk.Tk()
form.title("5cm çaplı Küre-Küre elektrot sistemi,1 cm açıklık")
form.geometry("700x450+820+30")

label = tk.Label(form, text="Dalga Şekli İzleme Ekranı", fg='red', font="Verdana 13 bold")
label.pack()

buton = tk.Button(form, text="          AC          ", fg='black', bg="orange",font="Verdana 13 bold", command=onlyAC_800)
buton.pack(ipadx=25, ipady=10)  # buton.place(relx=0.5,rely=0.5)

buton2 = tk.Button(form, text="          DC          ",fg='black',bg="white",font="Verdana 13 bold",command=onlyDC_080)
buton2.pack(ipadx=25, ipady=10)

buton3 =tk.Button(form, text="          -DC         ",fg='black',bg="white",font="Verdana 13 bold",command=only_eksiDC_110)
buton3.pack(ipadx=25, ipady=10)

buton4 =tk.Button(form, text="    AC + 6kV_DC"  ,fg='black', bg="orange",font="Verdana 13 bold", command=AC_artı6KV_DC)
buton4.pack(ipadx=25, ipady=10)

buton5 =tk.Button(form, text="AC + 6kV_DC_2",fg='black', bg="orange",font="Verdana 13 bold", command=AC_artı6KV_DC_800)
buton5.pack(ipadx=25, ipady=10)

buton6 =tk.Button(form, text="   AC - 6kV_DC  ",fg='gold', bg="purple",font="Verdana 13 bold", command=AC_eksi6KV_DC)
buton6.pack(ipadx=25, ipady=10)

buton7 =tk.Button(form, text=" AC - 6kV_DC_2",fg='gold', bg="purple",font="Verdana 13 bold", command=AC_eksi6KV_DC_200)
buton7.pack(ipadx=25, ipady=10)

form.mainloop()
