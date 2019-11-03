def completed():
    print("---------------------------------------Do you want to order more?---------------------------------------")
    Ans =input('Enter Yes or No :')
    
    if Ans == "Yes" or Ans == "yes" or Ans == "YES" or Ans == "y":
        website()
        
    elif Ans == "No" or Ans == "NO" or Ans == "no" or Ans == "n":
        print("----------Thanks for using foodies store----------")
        print("--------"*10)
        
    else:
        print("-"*80)
        print("sorry!!!You have choosed invalid input")
        print("-"*80)
        print("Please choose again")
        print("------------------------------------------------------------------------------")
        completed()
        
def Addcart():
    cart = input("Select Option:").upper()
    print(" ")

    if cart == "1":
        print("--------"*10)
        print("Food added to cart")
        print("--------"*10)
        print(" ")
        completed()
    if cart == "2":
        print("--------"*10)
        print("Food added to cart")
        print("--------"*10)
        print(" ")
        completed()

    if cart == "3":
        print("Food added to cart")
        print("--------"*10)
        print(" ")
        completed()
        print("--------"*10)
        print(" ")
        completed()
        
    if cart == "4":
        print("--------"*10)
        print("Food added to cart")
        print("--------"*10)
        print(" ")
        completed()
        
    if cart == "5":
        print("--------"*10)
        print("Food added to cart")
        print("--------"*10)

        completed()  
        

    else:
        print("food cant be added to cart!!!!!!")
        print("--------"*10)
        completed()




def website():
    import loginpass
    print("-----------------------------welcome to foodies store.-----------------------------")
    print("Select the food type you crave for!")
    print("1.Fast food")
    print("2.Heavy meal")
    print("3.Light meal")
    print("4.Main course")
    print("5.Desserts")
    print("-"*80)
    num = int(input("Choose any one of the option:"))

    print("-"*80)


    if num==1:
        print(" You have selected Fast food")
        print("1.pizza\tRs.99")
        print("2.burger\tRs.55")
        print("3.French fries\tRs.110")
        print("4.Garlic bread\tRs.75(5pcs)")
        print("5.Franky\tRs.45")
        print("6.Sandwich\tRs.30")
        

        print("-"*80)

        Addcart()
    elif num==2:
        print("Heavy meal")
        print("1.Pav bhaji\tRs.120")
        print("2.veg schezwan fried rice\tRs.150(F)")
        print("3.Noodles\tRs.125(F)")
        print("4.Briyani\tRs.200")
        print("5.dosas\tRs.40")
        

        print("-"*80)

        Addcart()



    elif num==3:
          print("Light meal")
          print("1.dal khichidi\tRs.100")
          print("2.steamed rice\tRs.50")
          print("3.curry rice\tRs.150")
          print("4.Dal tadka\tRs.180")
          print("5.Dal fry\tRs.210")
          
          
          print("-"*80)

          Addcart()
    elif num==4:
          print("Main course")
          print("1.veg amritsari \t\t Rs. 200")
          print("2.malai kofta \t\t Rs.280")
          print("3.panner makanwala \t Rs.180")
          print("4.mix vegetables \t\t Rs.200")
          print("5.paneer kadai \t\t Rs.250")
          

          print("-"*80)

          Addcart()

    elif num==5: 
          print("Desserts")
          print("1.khulfi falooda\tRs.150")
          print("2.Gulab jamun\tRs.55(2pcs)")
          print("3.Elaichi/kesar shrikhand\tRs.250(1kg)")
          print("4.Vanilla/chocolate ice cream\tRs.60(1scoop)")
          print("5.Fruit salad\tRs.25")
          
          print("-"*80)

          Addcart()    



    else:
        print("-"*80)
        print("You have selected an invalid term,SELECT AGAIN!!")
        print("-"*80)
        website()



website()





