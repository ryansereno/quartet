import csv
import sys
product_choice = input("Choose a product: ")
effect_choice = input("What effect do you want?: ")

csv_file = open("test_data3.csv", "r")
csv_reader = csv.DictReader(csv_file, delimiter=",")

product_choice_line = {}
for line in csv_reader:
    if line["Product"] == product_choice:        #Dictionary variable set to line of product choice data
        product_choice_line = line
csv_file.seek(0)                                 #Must re-loop to begining of data file; csv reader reads through list only once by default, loop must be repeated

# define dynamic threshold variables based upon user response data
# define parameter multipliers to establish hierarchy and work along with user response data

next(csv_reader)                #must skip header (string) line to float values without error

if effect_choice == "Sedation":      #reject impossible product/effect entries
    for row in product_choice_line:
        if CBN_choice > 5 and Pinene_choice < 2:
            pass                            # Can also be inverted to 'if not' CBN_EMC > 5 'then' etc..
        if Myrcene_choice > 1 and Pinene_choice < 2:
            pass
        if Linalool_choice > 2 and Pinene_choice < 2:
            pass
        else:
            print("It is not possible to achieve your selected effect with the product you chose:(")
            sys.exit()

if effect_choice == "Sedation":
    for row in csv_reader:

#               H o w  T o  P a c k a g e  T h e s e  V a r i a b l e s  I n t o  D i s c r e e t  G r o u p s ?

        Product = "" if not row["Product"] else row["Product"]
        Product_type= "" if not row["Product Type"] else row["Product Type"]
        CBN = 0.0 if not row["CBN"] else float(row["CBN"]) #negates errors when trying to float blank string element, and floats numerical strings
        THC = 0.0 if not row["THC"] else float(row["THC"])
        Myrcene = 0.0 if not row["Myrcene"] else float(row["Myrcene"])
        Linalool = 0.0 if not row["Linalool"] else float(row["Linalool"])
        Limonene = 0.0 if not row["Limonene"] else float(row["Limonene"])
        Pinene = 0.0 if not row["Pinene"] else float(row["Pinene"])
        CBN_choice = 0.0 if not product_choice_line["CBN"] else float(product_choice_line["CBN"])
        Product_selection_parameter = product_choice_line["Product"]
        CBN_EMC = CBN - CBN_choice
        Myrcene_choice = 0.0 if not product_choice_line["Myrcene"] else float(product_choice_line["Myrcene"])
        myrcene_EMC = Myrcene - Myrcene_choice
        Linalool_choice = 0.0 if not product_choice_line["Linalool"] else float(product_choice_line["Linalool"])
        linalool_EMC = Linalool - Linalool_choice
        #def Product_type_parameter:
            #if product_choice["Product type"] = "Flower"
                #Product_type_parameter() != "Flower" and Product_type_parameter != "Cartridge"
    # float(row["Cannabinoid/ Terpenoid Value"] - product_choice_line["Cannabinoid/ Terpenoid Value"] --> Take difference of effect_choice and values of product_choice

        if Product_selection_parameter != row["Product"]:
            if product_choice_line["Product Type"] == "Edible":
                if row["Product Type"] != "Tincture" and row["Prodct Type"] != "Edible":
                    if CBN_EMC > 5 and Pinene < 2:
                        print("CBN Parameter: ", Product, ",", Product_type, "\n")
                    if myrcene_EMC > 1 and Pinene < 2:
                        print("Myrcene Parameter: ", Product, ",", Product_type, "\n")
                    if linalool_EMC > 2 and Pinene < 2:  # Multiple "if" statements used, to return product recommendations
                        #                                           multiple times so that they can be later counted. Product with the
                        #                                           greatest number of instances is passed through as a recommendation.
                        print("Linalool Parameter: ", Product, ",", Product_type, "\n")
            if product_choice_line["Product Type"] == "Cartridge":
                if row["Product Type"] != "Flower" and row["Prodct Type"] != "Cartridge":
                    if CBN_EMC > 5 and Pinene < 2:
                        print("CBN Parameter: ", Product, ",", Product_type, "\n")
                    if myrcene_EMC > 1 and Pinene < 2:
                        print("Myrcene Parameter: ", Product, ",", Product_type, "\n")
                    if linalool_EMC > 2 and Pinene < 2:
                        print("Linalool Parameter: ", Product, ",", Product_type, "\n")
            if product_choice_line["Product Type"] == "Tincture":
                if row["Product Type"] != "Tincture" and row["Prodct Type"] != "Edible":
                    if CBN_EMC > 5 and Pinene < 2:
                        print("CBN Parameter: ", Product, ",", Product_type, "\n")
                    if myrcene_EMC > 1 and Pinene < 2:
                        print("Myrcene Parameter: ", Product, ",", Product_type, "\n")
                    if linalool_EMC > 2 and Pinene < 2:
                        print("Linalool Parameter: ", Product, ",", Product_type, "\n")
            if product_choice_line["Product Type"] == "Flower":
                if row["Product Type"] != "Flower" and row["Prodct Type"] != "Cartridge":
                    if CBN_EMC > 5 and Pinene < 2:
                        print("CBN Parameter: ", Product, ",", Product_type, "\n")
                    if myrcene_EMC > 1 and Pinene < 2:
                        print("Myrcene Parameter: ", Product, ",", Product_type, "\n")
                    if linalool_EMC > 2 and Pinene < 2:
                        print("Linalool Parameter: ", Product, ",", Product_type, "\n")
            if product_choice_line["Product Type"] == "Topical":
                if row["Product Type"] != "Topical":
                    if CBN_EMC > 5 and Pinene < 2:
                        print("CBN Parameter: ", Product, ",", Product_type, "\n")
                    if myrcene_EMC > 1 and Pinene < 2:
                        print("Myrcene Parameter: ", Product, ",", Product_type, "\n")
                    if linalool_EMC > 2 and Pinene < 2:
                        print("Linalool Parameter: ", Product, ",", Product_type, "\n")

elif effect_choice == "Focus":
    for row in csv_reader:
        Product = "" if not row["Product"] else row["Product"]
        Product_type= "" if not row["Product Type"] else row["Product Type"]
        CBN = 0.0 if not row["CBN"] else float(row["CBN"])
        THC = 0.0 if not row["THC"] else float(row["THC"])
        THCV = 0.0 if not row["THCV"] else float(row["THCV"])
        Myrcene = 0.0 if not row["Myrcene"] else float(row["Myrcene"])
        Linalool = 0.0 if not row["Linalool"] else float(row["Linalool"])
        Limonene = 0.0 if not row["Limonene"] else float(row["Limonene"])
        Pinene = 0.0 if not row["Pinene"] else float(row["Pinene"])
        Humulene = 0.0 if not row["Humulene"] else float(row["Humulene"])
        CBN_choice = 0.0 if not product_choice_line["CBN"] else float(product_choice_line["CBN"])
        Product_selection_parameter = product_choice_line["Product"]
        THCV_choice = 0.0 if not product_choice_line["THCV"] else float(product_choice_line["THCV"])
        THCV_EMC = THCV - THCV_choice

        if Product_selection_parameter != row["Product"]:
            if THCV_EMC >= 5 and CBN < 2:
                print("THCV Parameter: ", Product, ",", Product_type, "\n")
            if Pinene >= 1 and CBN < 2:
                print("Pinene Parameter: ", Product, ",", Product_type, "\n")
            if Limonene >= 2 and CBN < 2:
                print("Limonene Parameter: ", Product, ",", Product_type, "\n")
            if Humulene >= 3 and CBN < 2:
                print("Humulene Parameter: ", Product, ",", Product_type, "\n")

elif effect_choice == "Pain management":
    for row in csv_reader:
        Product = "" if not row["Product"] else row["Product"]
        Product_type= "" if not row["Product Type"] else row["Product Type"]
        CBDa = 0.0 if not row["CBDa"] else float(row["CBDa"])
        CBD = 0.0 if not row["CBD"] else float(row["CBD"])
        THCa = 0.0 if not row["THCa"] else float(row["THCa"])
        THC = 0.0 if not row["THC"] else float(row["THC"])
        Myrcene = 0.0 if not row["Myrcene"] else float(row["Myrcene"])
        Linalool = 0.0 if not row["Linalool"] else float(row["Linalool"])
        Limonene = 0.0 if not row["Limonene"] else float(row["Limonene"])
        Pinene = 0.0 if not row["Pinene"] else float(row["Pinene"])
        Humulene = 0.0 if not row["Humulene"] else float(row["Humulene"])
        Caryophyllene = 0.0 if not row["Caryophyllene"] else float(row["Caryophyllene"])
        Product_selection_parameter = product_choice_line["Product"]
        Pinene_choice = 0.0 if not product_choice_line["Pinene"] else float(product_choice_line["Pinene"])
        pinene_EMC = Pinene - Pinene_choice
        THC_choice = 0.0 if not product_choice_line["THC"] else float(product_choice_line["THC"])
        THC_EMC = THC - THC_choice
        THCa_choice = 0.0 if not product_choice_line["THCa"] else float(product_choice_line["THCa"])
        THCa_EMC = THCa - THCa_choice

        if Product_selection_parameter != row["Product"]:
            if product_choice_line["Product Type"] == "Cartridge":
                if row["Product Type"] != "Flower" and row["Prodct Type"] != "Cartridge":
                    if CBD + CBDa >= 6:
                        print("CBD Parameter: ", Product, ",", Product_type, "\n")
                    if THC_EMC >= 10 or THCa >= 10:
                        print("THC Parameter: ", Product, ",", Product_type, "\n")
                    if pinene_EMC >= 2:
                        print("Pinene Parameter: ", Product, ",", Product_type, "\n")
                    if THCa_EMC >= 10 and Product_type != "Flower" and Product_type != "Cartridge":
                        print("THCa Parameter: ", Product, ",", Product_type, "\n")
            if product_choice_line["Product Type"] == "Edible":                   # Specific parameters can be set for particular produc types;
                                                                                  # In this case, elevated acidic cannabinoids can be searched for
                                                                                  # within non-heated products like edibles
                if row["Product Type"] != "Edible" and row["Product Type"] != "Tincture":
                    if CBD + CBDa >= 6:
                        print("CBD Parameter: ", Product, ",", Product_type, "\n")
                    if THC_EMC >= 10 or THCa >= 10:
                        print("THC Parameter: ", Product, ",", Product_type, "\n")
                    if pinene_EMC >= 2:
                        print("Pinene Parameter: ", Product, ",", Product_type, "\n")
                    if THCa_EMC >= 10 and Product_type != "Flower" and Product_type != "Cartridge":
                        print("THCa Parameter: ", Product, ",", Product_type, "\n")



elif effect_choice == "Energy":
    for row in csv_reader:
        Product = "" if not row["Product"] else row["Product"]
        Product_type= "" if not row["Product Type"] else row["Product Type"]
        CBN = 0.0 if not row["CBN"] else float(row["CBN"])
        THC = 0.0 if not row["THC"] else float(row["THC"])
        THCa = 0.0 if not row["THCa"] else float(row["THCa"])
        Myrcene = 0.0 if not row["Myrcene"] else float(row["Myrcene"])
        Linalool = 0.0 if not row["Linalool"] else float(row["Linalool"])
        Limonene = 0.0 if not row["Limonene"] else float(row["Limonene"])
        Pinene = 0.0 if not row["Pinene"] else float(row["Pinene"])
        Caryophyllene = 0.0 if not row["Caryophyllene"] else float(row["Caryophyllene"])
        Product_selection_parameter = product_choice_line["Product"]


        if Product_selection_parameter != row["Product"]:
            if THC + THCa >= 10 and CBN < 1 and Myrcene < 0.5:
                print("Low Myrcene Parameter: ", Product, ",", Product_type, "\n")
            if THC + THCa >= 10 and CBN < 1 and Caryophyllene < 1 and Myrcene < 0.5:
                print("Caryophyllene Parameter: ", Product, ",", Product_type, "\n")

elif effect_choice == "Stress reduction":
    for row in csv_reader:
        Product = "" if not row["Product"] else row["Product"]
        Product_type= "" if not row["Product Type"] else row["Product Type"]
        CBD = 0.0 if not row["CBD"] else float(row["CBD"])
        CBDa = 0.0 if not row["CBDa"] else float(row["CBDa"])
        THC = 0.0 if not row["THC"] else float(row["THC"])
        THCV = 0.0 if not row["THCV"] else float(row["THCV"])
        Myrcene = 0.0 if not row["Myrcene"] else float(row["Myrcene"])
        Linalool = 0.0 if not row["Linalool"] else float(row["Linalool"])
        Limonene = 0.0 if not row["Limonene"] else float(row["Limonene"])
        Pinene = 0.0 if not row["Pinene"] else float(row["Pinene"])
        Product_selection_parameter = product_choice_line["Product"]

        if Product_selection_parameter != row["Product"]:
            if Linalool >= 1:  # if product row is not null, print line; can be run as AND or OR
                print("Linalool Parameter: ", Product, ",", Product_type, "\n")
            if CBD + CBDa >= 10:
                print("CBD Parameter: ", Product, ",", Product_type, "\n")
            if Limonene >= 2:
                print("Limonene Parameter: ", Product, ",", Product_type, "\n")

else:
    print("Not a valid effect choice :(")
