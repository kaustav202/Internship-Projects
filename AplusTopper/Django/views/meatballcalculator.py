def meatballcalculator(request):
  if request.method=='POST':
    
    """ given data denotes the type of meat
        W is the entered weight to be cooked
    """
    #Obtaining the Ia
    if request.POST.get('W')!=None and request.POST.get('W')!='' :     
              inp=str(request.POST.get('W'))
              if inp.isdigit():
                  W=int(request.POST.get('W'))
              else:
                  W=float(request.POST.get('W'))
    else:
       W=None

    if request.POST.get('D')!=None and request.POST.get('D')!='' :     
              inp=str(request.POST.get('D'))
              if inp.isdigit():
                  D=int(request.POST.get('D'))
              else:
                  D=float(request.POST.get('D'))
    else:
       D=None


    if request.POST.get('L')!=None and request.POST.get('L')!='' :     
              inp=str(request.POST.get('L'))
              if inp.isdigit():
                  L=int(request.POST.get('L'))
              else:
                  L=float(request.POST.get('L'))
    else:
       L=None


    if request.POST.get('B')!=None and request.POST.get('B')!='' :     
              inp=str(request.POST.get('B'))
              if inp.isdigit():
                  B=int(request.POST.get('B'))
              else:
                  B=float(request.POST.get('B'))
    else:
       B=None


    if request.POST.get('E')!=None and request.POST.get('E')!='' :     
              inp=str(request.POST.get('E'))
              if inp.isdigit():
                  E=int(request.POST.get('E'))
              else:
                  E=float(request.POST.get('E'))
    else:
       E=None


    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True


    if form:

      #FETCHING THE UNITS
      W_op=request.POST.get('W_op')
      D_op = request.POST.get('D_op')
      L_op = request.POST.get('L_op')
      B_op = request.POST.get('B_op')
      E_op = request.POST.get('E_op')


      #COPYING OF THE VARIABLES
      W1 = W
      D1 = D
      L1 = L
      B1 = B
      E1 = E

      #Conversion of units here



      weight_factors = {
        'o':0.0625,
        'kg':2.2046,
        'g':0.0022,
      }

      length_factors = {
        'mm' : 0.0393
      }

      quantity_factors = {
        'tab': 0.0625
      }


      
      if W_op != 'p':
        cf = weight_factors[W_op]
        W=W*cf #convert into grams
      
      if D_op != 'in':
        cf = length_factors[D_op]
        D=D*cf
      
      if L_op != 'cup':
        cf = quantity_factors[L_op]
        L = L*cf
      
      if B_op != 'cup':
        cf = quantity_factors[B_op]
        B = B*cf
      
      if E_op != 'cup':
        cf = quantity_factors[E_op]
        E = E*cf
      

      vol = (4/3) * 3.14159265 * ((D/2)**3)
      vol =  (1/vol)

      contr = {
        'W': 27,
        'L': 13,
        'B': 9,
        'E': 14,
      }

      meatball = W*(contr['W']) + L*(contr['L']) + B*(contr['B']) +E*(contr['E'])

      meatball = meatball * vol

      meatball = round(meatball)

      W = round(W,3)
      D = round(D,3)

      context={
         'id':1,
         'W': W,
         'D': D,
         'W1':W1,
         'D1': D1,
         'L1': L1,
         'B1' : B1,
         'E1' : E1,
         'W_op': W_op,
         'D_op': D_op,
         'L_op': L_op,
         'B_op' : B_op,
         'E_op' : E_op,
         'meatball' : meatball
      }
      return render(request,'meatballcalculator.html',context)
      
  
    else:
     return render(request,'meatballcalculator.html',{
         'id':1,
         'W1':7,
         'D1': 5,
         'L1': 3,
         'B1' : 10,
         'E1' : 22,
         'W_op':'p',
         'D_op':"in",
         'L_op': "cup",
         'B_op' : "cup",
         'E_op' : "cup",
         'meatball' : 10
     })
    
  else:
    return render(request,'meatballcalculator.html',{
         'id':1,
         'W1':7,
         'D1': 5,
         'L1': 3,
         'B1' : 10,
         'E1' : 22,
         'W_op':'p',
         'D_op':"in",
         'L_op': "cup",
         'B_op' : "cup",
         'E_op' : "cup",
         'meatball' : 10
    })
