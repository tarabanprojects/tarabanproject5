"""
projekt_1.py: první projekt -  PYTHON - vypocet slov v textu
  
author: Igor  Taraban
e-mail: taraban@centrum.cz
 
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

par_uzivatel={input("Enter your name, please: "):input("Enter your password, please:  ")}
par_vlozen={"bob":"123","ann":"pass123", "mike":"password123", "liz":"pass123"}
control = all((par_vlozen.get(key) ==  value for key, value in par_uzivatel.items()))

if control == False :
    print("$ python projekt1.py")
    print(f"username:",*par_uzivatel.keys())
    print(f"password:",*par_uzivatel.values())
    print("unregistered  user, terminating  the  program ..." )
    
else:
    print("$ python projekt1.py","\n"f"username: ", *par_uzivatel.keys(), "\n"f"password: ",   *par_uzivatel.values())
    print("------------------------------------------")
    print(f"Welcome to the app,", *par_uzivatel.keys(),"\nWe have 3 texts to be analyzed.")
    print("------------------------------------------")
    vyber_textu=int(input("Enter a number btw. 1 and 3 to select : "))
    print("------------------------------------------")
   
    delka=len(TEXTS)
    if vyber_textu in range (0,delka+1) :
        promenna=vyber_textu - 1
        hodnota_1=len(TEXTS[promenna].split())
        print(f"There are {hodnota_1} words in the selected text.") 
                
        hodnota = TEXTS[promenna].split()
        V = 0
        index = 0
        for hodnota_1 in hodnota : 
            hodnota_2=(hodnota[index]. istitle()) 
            if hodnota_2==True :
                V = V+1
                index+=1
            else:
                index+=1
        print(f"There are {V} titlecase words.")
                
        VELKA=0
        index_1=0
        for hodnota_3 in hodnota: 
            hodnota_4=(hodnota[index_1].isupper()) 
            if hodnota_4 is True :
                hodnota_y=(hodnota[index_1].isalpha())
                if hodnota_y is True :
                    VELKA = VELKA+1
                    index_1+=1
                else:                          
                    index_1+=1
            else:
                index_1+=1
                
        print(f"There are {VELKA} uppercase words.")
                
        mala = 0
        indexM = 0
        for hodnota_7 in TEXTS[promenna].split() : 
            hodnota_8=(TEXTS[0][indexM].islower()) 
            if hodnota_8 is True :
                mala = mala+1
                indexM+=1
            else:
                indexM+=1
        print(f"There are {mala} lowercase words.") 
                
        sum=0
        numer=0
        indexN=0
        for hodnota_9 in hodnota: 
            hodnota_10=(hodnota[indexN].isnumeric())
            if hodnota_10 is True :
                numer=numer+1
                y=int(hodnota_9)
                sum=sum+y
                indexN+=1
            else:
                indexN+=1
        print(f"There are {numer} numeric strings.") 
        print(f"There sum off all the numbers {sum}.")
              
        hodnota=TEXTS[promenna].split()
        pocet_1 = 0
        pocet_2 = 0
        pocet_3 = 0
        pocet_4 = 0
        pocet_5 = 0
        pocet_6 = 0
        pocet_7 = 0
        pocet_8 = 0
        pocet_9 = 0
        pocet_10 = 0
        pocet_11 = 0
        pocet_12 = 0
        pocet_13 = 0

        index = 0
        for hodnota_1 in hodnota : 
            hodnota_2=len(hodnota[index])
            if  hodnota_2 == 1 :
                pocet_1=pocet_1+1
                index+=1
            elif hodnota_2 == 2 :
                pocet_2=pocet_2+1
                index+=1
            elif hodnota_2 == 3 :
                pocet_3=pocet_3+1
                index+=1
            elif hodnota_2 == 4 :
                pocet_4=pocet_4+1
                index+=1
            elif hodnota_2 == 5 :
                pocet_5=pocet_5+1
                index+=1
            elif hodnota_2 == 6 :
                pocet_6=pocet_6+1
                index+=1
            elif hodnota_2 == 7 :
                pocet_7=pocet_7+1
                index+=1
            elif hodnota_2 == 8 :
                pocet_8=pocet_8+1
                index+=1
            elif hodnota_2 == 9 :
                pocet_9=pocet_9+1
                index+=1
            elif hodnota_2 == 10 :
                pocet_10=pocet_10+1
                index+=1
            elif hodnota_2 == 11 :
                pocet_11=pocet_11+1
                index+=1
            elif hodnota_2 == 12 :
                pocet_12=pocet_12+1
                index+=1
            elif hodnota_2 == 13 :
                pocet_13=pocet_13+1
                index+=1
            elif hodnota_2 == 14 :
                pocet_14=pocet_14+1
                index+=1
            elif hodnota_2 == 15 :
                pocet_15=pocet_15+1
                index+=1
            else:
                ("Vše  slova byli  již prozkoumani !!!")
        print("------------------------------------------")
        print("  LEN |   OCCURENCES      | No.")
        print("------------------------------------------")
        print("     1|" , "*" * pocet_1, " "*(16-pocet_1), "|",pocet_1, end="\n")  
        print("     2|" , "*" * pocet_2, " "*(16-pocet_2), "|",pocet_2, end="\n")
        print("     3|" , "*" * pocet_3, " "*(16-pocet_3), "|",pocet_3, end="\n")
        print("     4|" , "*" * pocet_4, " "*(16-pocet_4),"|",pocet_4, end="\n")
        print("     5|" , "*" * pocet_5, " "*(16-pocet_5),"|",pocet_5, end="\n")
        print("     6|" , "*" * pocet_6, " "*(16-pocet_6),"|",pocet_6, end="\n")
        print("     7|" , "*" * pocet_7, " "*(16-pocet_7),"|",pocet_7, end="\n")
        print("     8|" , "*" * pocet_8, " "*(16-pocet_8),"|",pocet_8, end="\n")
        print("     9|" , "*" * pocet_9, " "*(16-pocet_9),"|",pocet_9, end="\n")
        print("    10|" , "*" * pocet_10," "*(16-pocet_10),"|",pocet_10, end="\n")
        print("    11|" , "*" * pocet_11," "*(16-pocet_11),"|",pocet_11, end="\n")
        print("    12|" , "*" * pocet_12," "*(16-pocet_12),"|",pocet_12, end="\n")
        print("    13|" , "*" * pocet_13," "*(16-pocet_13),"|",pocet_13, end="\n")   
                
    else:
        print("$ python projekt1.py")
        print(f"username:",*par_uzivatel.keys())
        print(f"password:",*par_uzivatel.values()) 
        print("entered text number is wrong, terminating  the  program ..." )
