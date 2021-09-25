while 1: 
  def start() :
      print ("Welcome to the weight converter toolkit made by Ayodeji. please enter your weight to begin")
  start()

  def converter():
      Weight = float (input("WEIGHT: "))
      Unit = input ("K(g) or L(bs) (Type K for Kg or L for lbs): ")
      if Unit.upper() == 'L':
        Pound =  float(1 * Weight)/ 2.204
        a = Pound
        print (str(a) + ' Kg')
      elif Unit.upper() == 'K':
          Kg = float(2.204 * Weight)/ 1
          b= Kg
          print (str(b)+(" lbs"))
      else:
        start()
        converter()
  converter()
