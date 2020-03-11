
# use it to calculate Tank farm 2000-01
#Create by Man Jirayu

def mainMenu():
    print("---------------------------------------------------")
    print("-------------   TF2000-01  V.1.5     --------------")
    print("          Faster than calculater edition           ")
    print("---------------   for Panorient   -----------------")
    print("---------------------------------------------------")
    print("               -- Step to use --                   ")
    print("       1.Type the last of water volume")
    print("       2.Type volume Load out & Load in")
    print("      *If No have some of volume type 0")
    print("                   --------")
    print("---------------------------------------------------")
    print("use to calculate Farm tank at DD production ")
    print("Develop by Man Jirayu.")
    print("---------------------------------------------------")

    while True:
        try:
            selection=int(input("Type 1 to use & 2 to Exit: "))

            if selection == 1:
                cal_tf2000()
                thx()

            elif selection == 2:
                break
            else:
                print("Please type  a number of somthing !")
                mainMenu()
                mainMenu()
            
        except ValueError:
                print("Please type  a number of somthing !")

def cal_tf2000():

    def_vol = float(input(" put the last of water volume (bbls): "))

    loadout = float(input(" Put water of loadout (bbls): "))
    vol_dd1 = float(input(" DD-1 water load in (bbls): "))
    vol_dd2 = float(input(" DD-2 water load in (bbls): "))
    vol_dd3 = float(input(" DD-3 water load in (bbls): "))
    vol_dd4 = float(input(" DD-4 water load in (bbls): "))

    def_cm = def_vol / 4.1404
    tt_def_cm = def_cm -491

    tt_lo = def_vol + loadout 
    tt_b_dd1 = tt_lo + vol_dd1
    tt_b_dd2 = tt_b_dd1 + vol_dd2
    tt_b_dd3 = tt_b_dd2 + vol_dd3
    tt_b_dd4 = tt_b_dd3 + vol_dd4

    cm_li_wt = tt_lo / 4.1404 - 491
    cm_li_dd1 = tt_b_dd1 / 4.1404 - 491
    cm_li_dd2 = tt_b_dd2 / 4.1404 - 491
    cm_li_dd3 = tt_b_dd3 / 4.1404 - 491
    cm_li_dd4 = tt_b_dd4 / 4.1404 - 491

    a = "---- Loat out     --- {0:,.2f} Cm   -- {1:,.2f} bbls".format(cm_li_wt, tt_lo)
    b = "---- Load in DD-1 --- {0:,.2f} Cm   -- {1:,.2f} bbls".format(cm_li_dd1, tt_b_dd1)
    c = "---- Load in DD-2 --- {0:,.2f} Cm   -- {1:,.2f} bbls".format(cm_li_dd2, tt_b_dd2)
    d = "---- Load in DD-3 --- {0:,.2f} Cm   -- {1:,.2f} bbls".format(cm_li_dd3, tt_b_dd3)
    e = "---- Load in DD-4 --- {0:,.2f} Cm   -- {1:,.2f} bbls".format(cm_li_dd4, tt_b_dd4)
#--------------------------------------------------------------------------------------------
    #loadout
    if loadout == 0:
        a = "-------------------------- No have water loadout !"
    else:
        loadout >= 0
        pass   

    #dd1
    if vol_dd1 == 0:
        b = "-------------------------- No have DD-1 load In !"
    else:
        vol_dd1 >= 0
        pass   

    #dd2
    if vol_dd2 == 0:
        c = "-------------------------- No have DD-2 load In !"
    else:
        vol_dd2 >= 0
        pass  

    #dd3
    if vol_dd3 == 0:
        d = "-------------------------- No have DD-3 load In !"
    else:
        vol_dd3 >= 0
        pass  

    #dd4
    if vol_dd4 == 0:
        e = "-------------------------- No have DD-4 load In !"
    else:
        vol_dd4 >= 0
        pass  
#--------------------------------------------------------------------------------------------
    print("###################################################")
    print(f"             SUMMARY of TF-2000-01                ")
    print("###################################################")
    print("---- Defult       --- {0:,.2f} Cm  -- {1:,.2f} bbls".format(tt_def_cm, def_vol))
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print("###################################################")
    print(f"               Volume of load in                  ")
    print(f"---- load out {loadout} bbls")
    print(f"---- DD-1 {vol_dd1} bbls ")
    print(f"---- DD-2 {vol_dd2} bbls ")
    print(f"---- DD-3 {vol_dd3} bbls ")
    print(f"---- DD-4 {vol_dd4} bbls ")

def thx():
    print("###################################################")
    print("#######         Have a great day         ##########")
    print("###################################################")
           

mainMenu()




    