#Truth Table Generator - www.101computing.net/truth-table-generator/

def truthTable(expression,inputs=2):
  print("Boolean Expression:")
  print("  X = " + expression.upper())
  expression = expression.lower()
  
  #replace Boolean Operators with bitwise operators
  expression = expression.replace("and","&")
  expression = expression.replace("xor","^")
  expression = expression.replace("or","|")
  expression = expression.replace("not","~")
  
  print("\nTruth Table:")
  if inputs==2:
    print("  -------------")
    print("  | P | Q | X |")
    print("  -------------")
    
    for a in range(0,2):
      for b in range(0,2):
        x = eval(expression)
        print("  | " + str(a) + " | " + str(b) + " | " + str(x) + " |" )
        print("  -------------")
        
  elif inputs==3:
    print("  -----------------")
    print("  | P | Q | R | X |")
    print("  -----------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          x = eval(expression)
          print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " |" )
          print("  -----------------")
    
  elif inputs==4:
    print("  ---------------------")
    print("  | P | Q | R | S | X |")
    print("  ---------------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          for d in range(0,2):
            x = eval(expression)
            print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(d) + " | " + str(x) + " |" )
            print("  ---------------------")

  elif inputs==5:
    print("  ---------------------")
    print("  | P | Q | R | S | X |")
    print("  ---------------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          for d in range(0,2):
            for e in range(0,2):
                x = eval(expression)
                print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(d) + " | " + str(e) + " | " + str(x) + " |" )
                print("  ---------------------")

##############################################

expression = "A AND NOT (B XOR C)"
truthTable(expression,3)

