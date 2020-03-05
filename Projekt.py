import matplotlib.pyplot as plot
import numpy as np

#kaardistan võimalikud kasutatavad failid
statistika_alus = {
    1: "hinnastatistika_2018.csv",
    2: "hinnastatistika_2017.csv",
    3: "hinnastatistika_2016.csv",
    4: "hinnastatistika_2015.csv"
    }
valitud_statistika_alused = []

#puhastan sisse loetud andmed, eemaldan ebavajalikud märgid.
#kasutades pop() operaatorit eemaldan esimese ja viimase rea
def puhasta_andmed(fail):
    andmed = []
    for rida in fail:
        andmed.append(rida.strip().split(","))
    if len(andmed) > 0:
        andmed.pop(0)
        andmed.pop(-1)
    return andmed

#alustan oma sõnastikku, kaardistan andmed. Iga rida on eraldi listi objekt.
#seega iga rida on list listis. Andmehulk on list mis kuulub listi algandmestik
def kaardista_andmed(algandmestik: list, indeks: int):
    kaardistus = {}
    # valin listis algandmestik andmerea ja selles väärtuse kohal indeks
    for andmerida in algandmestik: 
        rida = andmerida[indeks].strip('"').strip().replace('\xa0', '')
        #võtmeks valin maakonna nime, väärtuseks andmerea numbrilise väärtuse
        kaardistus[andmerida[0]] = float(rida) 
    return kaardistus

#joonistan graafiku sisendiks kaardistatud andmed. Kaasa muutuja pealkiri, mis oleneb operatsioonist
def joonista_graafik(andmekaardistus: dict, pealkiri):
    #loon legendi sisendi. Nimekiri alati üheliikmeline, valin ainsa liikme
    legend = valitud_statistika_alused[0]
    #puhastan sisestuse nii, et ainult aastanumber jääb alles
    legend = legend.replace("hinnastatistika_", "")
    legend = legend.replace(".csv", "")
    #horisontaalne bar chart, mille sisu on andmekaardistusest saadud väärtused
    plot.barh(range(len(andmekaardistus)), list(andmekaardistus.values()), align="center", label=legend)
    #igale reale vastavalt nimedeks andmekaardistusest võtmeväärtused
    plot.yticks(range(len(andmekaardistus)), list(andmekaardistus.keys()))
    plot.title(pealkiri)
    #legend ülemisse paremasse nurka
    plot.legend(loc="upper right")
    #tõmbame graafiku kitsamaks
    plot.tight_layout()
    plot.show()

def vordlus_graafik(andmekaardistus_first, andmekaardistus_second, pealkiri):
    #teen legendi. Seekord kaks sisendit
    legend = []
    #muudan statistikate nimekirjas väärtused legendi sobivaks
    for aasta in valitud_statistika_alused:
        aasta = aasta.replace("hinnastatistika_", "")
        aasta = aasta.replace(".csv", "")
        legend.append(aasta)
    #teen horisontaalse graafiku kahe andmekaardistusega kasutades numpy arange() operaatorit
    #saan anda ridadele laiused ja graafiku vaadeldavaks
    plot.barh(np.arange(len(andmekaardistus_first)),
              list(andmekaardistus_first.values()),
              0.4,
              align="center",
              color='blue',
              label=legend[0])
    #teen teise graafiku liikme, uue värviga, eelmise kõrvale
    plot.barh(np.arange(len(andmekaardistus_second)) + 0.4,
              list(andmekaardistus_second.values()),
              0.4,
              align="center",
              color='orange',
              label=legend[1])
    #mõlemal nimekirjal identsed maakonna nimed, esitan esimeselt nimetuse
    plot.yticks(range(len(andmekaardistus_first)), list(andmekaardistus_first.keys()))
    plot.tight_layout()
    plot.legend(loc="upper right")
    plot.title(pealkiri)
    plot.show()

#filtreerin andmestikust valitud maakonna ja esitan
def filtreeri_andmestik(andmekaardistus: dict, key):
    andmekaardistus.pop(key)
    return andmekaardistus

#valib välja kasutaja valitud maakonna ja näitab selle statistikat
def haara_maakond(andmekaardistus: dict, key):
    uks_maakond = {}
    #valitud maakonna andmetega sõnastik
    #andmekaardistusest valitud liikme kirjutamine sõnastikku
    uks_maakond[key] = andmekaardistus[key] 
    return uks_maakond

def alusta_joonistamist(algandmestik):
    print("Vali graafik:")
    print("1.Tehingute arv")
    print("2.Kinnistute kogupind (ha)")
    print("3.Tehingute koguväärtus (EUR)")
    sisend = int(input())
    
    pealkiri_lisa = ""
    if sisend ==1:
        pealkiri_lisa = "tehingute arv"
    if sisend == 2:
        pealkiri_lisa = "kinnistute kogupind"
    if sisend == 3:
        pealkiri_lisa = "tehingute koguväärtus"

    if 1 <= sisend <= 3:
        andmekaardistus = kaardista_andmed(algandmestik, sisend)
        joonista_graafik(andmekaardistus, "Maakondade võrdlus, " + pealkiri_lisa)
    else:
        print("Väärtus peab olema vahemikus 1-3")
        alusta_joonistamist(algandmestik)

def joonista_maakonna_graafik(algandmestik):
    maakonna_valik = []
    print("Vali maakond:")
    valik_num = 0
    for andmerida in algandmestik:
        valik_num += 1
        maakonna_valik.append(andmerida[0])
        print(str(valik_num) + ". " + str(andmerida[0]))

    sisend = int(input())

    if 0 <= sisend <= len(maakonna_valik):
        print("Vali graafik:")
        print("1.Tehingute arv")
        print("2.Kinnistute kogupind (ha)")
        print("3.Tehingute koguväärtus (EUR)")
        graafik_sisend = int(input())
        pealkiri_lisa = ""
        if graafik_sisend == 1:
            pealkiri_lisa = "tehingute arv"
        if graafik_sisend == 2:
            pealkiri_lisa = "kinnistute kogupind"
        if graafik_sisend == 3:
            pealkiri_lisa = "tehingute koguväärtus"

        if 1 <= graafik_sisend <= 3:
            andmekaardistus = kaardista_andmed(algandmestik, graafik_sisend)
            joonista_graafik(haara_maakond(andmekaardistus, maakonna_valik[sisend - 1]),
                             "Võrdlus maakonna tasandil, " + pealkiri_lisa)
        else:
            print("Väärtus peab olema vahemikus 1-3")
            joonista_maakonna_graafik(algandmestik)

def joonista_filtreeritud_maakondadega_graafik(algandmestik):
    maakonna_valik = []
    print("Vali maakond:")
    valik_num = 0
    for andmerida in algandmestik:
        valik_num += 1
        maakonna_valik.append(andmerida[0])
        print(str(valik_num) + ". " + str(andmerida[0]))

    sisend = int(input())

    if 0 <= sisend <= len(maakonna_valik):
        print("Vali graafik:")
        print("1.Tehingute arv")
        print("2.Kinnistute kogupind (ha)")
        print("3.Tehingute koguväärtus (EUR)")
        graafik_sisend = int(input())
        
        pealkiri_lisa = ""
        if graafik_sisend == 1:
            pealkiri_lisa = "tehingute arv"
        if graafik_sisend == 2:
            pealkiri_lisa = "kinnistute kogupind"
        if graafik_sisend == 3:
            pealkiri_lisa = "tehingute koguväärtus"

        if 1 <= graafik_sisend <= 3:
            andmekaardistus = kaardista_andmed(algandmestik, graafik_sisend)
            joonista_graafik(filtreeri_andmestik(andmekaardistus, maakonna_valik[sisend - 1]),
                             "Maakondade võrdlus v.a. valitud, " + pealkiri_lisa)
        else:
            print("Väärtus peab olema vahemikus 1-3")
            joonista_maakonna_graafik(algandmestik)

def alusta_vordlusgraafikut(algandmestikud: list):
    print("Vali graafik:")
    print("1.Tehingute arv")
    print("2.Kinnistute kogupind (ha)")
    print("3.Tehingute koguväärtus (EUR)")
    sisend = int(input())
    andmekaardistused = []
    
    pealkiri_lisa = ""
    if sisend == 1:
        pealkiri_lisa = "tehingute arv"
    if sisend == 2:
        pealkiri_lisa = "kinnistute kogupind"
    if sisend == 3:
        pealkiri_lisa = "tehingute koguväärtus"

    if 1 <= sisend <= 3:
        for algandmed in algandmestikud:
            andmekaardistused.append(kaardista_andmed(algandmed, sisend))
        vordlus_graafik(andmekaardistused[0], andmekaardistused[1], "Maakondade võrdlus, " + pealkiri_lisa)
    else:
        print("Väärtus peab olema vahemikus 1-3")
        alusta_vordlusgraafikut(algandmestikud)

def alusta_ainsa_reaga_vordlusgraafikut(algandmestikud):
    maakonna_valik = []
    print("Vali maakond:")
    valik_num = 0
    for andmerida in algandmestikud[0]:
        valik_num += 1
        maakonna_valik.append(andmerida[0])
        print(str(valik_num) + ". " + str(andmerida[0]))

    sisend = int(input())

    if 0 <= sisend <= len(maakonna_valik):
        print("Vali graafik:")
        print("1.Tehingute arv")
        print("2.Kinnistute kogupind (ha)")
        print("3.Tehingute koguväärtus (EUR)")
        graafik_sisend = int(input())
        
        pealkiri_lisa = ""
        if graafik_sisend == 1:
            pealkiri_lisa = "tehingute arv"
        if graafik_sisend == 2:
            pealkiri_lisa = "kinnistute kogupind"
        if graafik_sisend == 3:
            pealkiri_lisa = "tehingute koguväärtus"
            
        if 1 <= graafik_sisend <= 3:
            andmekaardistus = []
            for andmestik in algandmestikud:
                andmekaardistus.append(haara_maakond(kaardista_andmed(andmestik, graafik_sisend),
                                                        maakonna_valik[sisend - 1]))
            vordlus_graafik(andmekaardistus[0],andmekaardistus[1], "Maakonna põhjal võrdlus, " + pealkiri_lisa)
        else:
            print("Väärtus peab olema vahemikus 1-3")
            alusta_ainsa_reaga_vordlusgraafikut(algandmestikud)

#filtreeritud andmestikuga võrddlus
def alusta_filtreeritud_vordlusgraafikut(algandmestikud):
    maakonna_valik = []
    print("Vali maakond:")
    valik_num = 0
    # küsin kasutajalt, millist andmestikku soovib välja filtreerida. Nimekiri olemas listis algandmestik
    for andmerida in algandmestikud[0]:
        valik_num += 1
        #lisan ette numbrilise väärtuse
        maakonna_valik.append(andmerida[0])
        print(str(valik_num) + ". " + str(andmerida[0]))

    sisend = int(input())
    
    if 0 <= sisend <= len(maakonna_valik):
        print("Vali graafik:")
        print("1.Tehingute arv")
        print("2.Kinnistute kogupind (ha)")
        print("3.Tehingute koguväärtus (EUR)")
        graafik_sisend = int(input())
        pealkiri_lisa = ""
        if graafik_sisend == 1:
            pealkiri_lisa = "tehingute arv"
        if graafik_sisend == 2:
            pealkiri_lisa = "kinnistute kogupind"
        if graafik_sisend == 3:
            pealkiri_lisa = "tehingute koguväärtus"
            
        if 1 <= graafik_sisend <= 3:
            andmekaardistus = []
            for andmestik in algandmestikud:
                andmekaardistus.append(filtreeri_andmestik(kaardista_andmed(andmestik, graafik_sisend), maakonna_valik[sisend - 1]))
            vordlus_graafik(andmekaardistus[0],andmekaardistus[1], "Maakonna põhjal võrdlus, " + pealkiri_lisa)
        else:
            print("Väärtus peab olema vahemikus 1-3")
            alusta_filtreeritud_vordlusgraafikut(algandmestikud)

#pakun võrdlusandmestiku juures samu võimalusi, mis ühe maakonna juures
def esita_edasised_vordlus_tegevused(algandmestikud: list):
    print("Esita valik:")
    print("1. Joonista võrdlusgraafik")
    print("2. Vali maakond mille põhjal võrdlusgraafik joonistada")
    print("3. Eemalda rida võrdlusgraafiku joonistamisest")
    
    sisend = int(input())
    if sisend == 1:
        alusta_vordlusgraafikut(algandmestikud)
    elif sisend == 2:
        alusta_ainsa_reaga_vordlusgraafikut(algandmestikud)
    elif sisend == 3:
        alusta_filtreeritud_vordlusgraafikut(algandmestikud)
    else:
        print("Proovi uuesti")
        esita_edasised_vordlus_tegevused(algandmestikud)

# lisan võrdlusandmed
def lisa_vordlusandmestik(algandmestik):
    print("Vali statistika:")
    for key, value in statistika_alus.items():
        value = value.replace('_', ' ')
        value = value.replace('.csv', '')
        value = value.capitalize()
        print(str(key) + ". " + str(value))
    sisend = int(input())
    vordlus_andmestikud = [algandmestik]

    if sisend in statistika_alus.keys():
        #käin läbi sama protsessi, mis esimese andmestiku valimisel, seekord peab tekitama massiivi
        #kus saan hoida mõlemat andmestikku mälus
        vordlus_fail = open(statistika_alus[sisend], "r", encoding="UTF-8")
        #lisan loetud faili statistika aluste listi
        valitud_statistika_alused.append(statistika_alus[sisend])
        #lisan võrdlusfaili
        vordlus_andmestikud.append(puhasta_andmed(vordlus_fail))
        #eemaldan võrdlusfaili statistika aluste sõnastikust
        statistika_alus.pop(sisend)
        vordlus_fail.close()
        #liigume edasi kaardistamise sammule
        esita_edasised_vordlus_tegevused(vordlus_andmestikud)
    else:
        print("Vali väärtus vahemikus 1-" + str(len(statistika_alus)))
        lisa_vordlusandmestik(algandmestik)

# edasised tegevused, sisend ja valik
def esita_edasised_tegevused(algandmestik):
    print("Mida soovite edasi teha?")
    print("1. Joonista graafik")
    print("2. Vali maakond mille põhjal graafik joonistada")
    print("3. Eemalda rida graafiku joonistamisest")
    print("4. Lisada võrdluseks andmestik")
    
    sisend = int(input())
#harutan sisendi lahti
    if sisend == 1:
        alusta_joonistamist(algandmestik)
    elif sisend == 2:
        joonista_maakonna_graafik(algandmestik)
    elif sisend == 3:
        joonista_filtreeritud_maakondadega_graafik(algandmestik)
    elif sisend == 4:
        lisa_vordlusandmestik(algandmestik)
    else:
        print("Palun valige valik 1-4 vahel")
        esita_edasised_tegevused(algandmestik)
    
        
# alustan sisendite küsimist
def ava_valik():
    print("Vali statistika:")
    for key, value in statistika_alus.items():
        #võtan faili nimetuse statistika aluste sõnastikust ja muudan nime esitamiseks ilusamaks
        value = value.replace('_', ' ')
        value = value.replace('.csv', '')
        value = value.capitalize()
        print(str(key) + ". " + str(value))
    sisend = int(input())
    algandmestik = []
    if sisend in statistika_alus.keys():
        fail = open(statistika_alus[sisend], "r", encoding="UTF-8")
        algandmestik = puhasta_andmed(fail)
        valitud_statistika_alused.append(statistika_alus[sisend])
        statistika_alus.pop(sisend)
        fail.close()
    else:
        print("Vali väärtus vahemikus 1-5")
        ava_valik()
    esita_edasised_tegevused(algandmestik)

# käivitan programmi
ava_valik()
