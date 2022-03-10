def pizzatipcalculator(request):
  if request.method=='POST':
    
    """ given data denotes the type of meat
        W is the entered weight to be cooked
    """
    if request.POST.get('A')!=None and request.POST.get('A')!='' :     
              inp=str(request.POST.get('A'))
              if inp.isdigit():
                  A=int(request.POST.get('A'))
              else:
                  A=float(request.POST.get('A'))
    else:
       A=None

    if request.POST.get('C')!=None and request.POST.get('C')!='' :     
              inp=str(request.POST.get('C'))
              if inp.isdigit():
                  C=int(request.POST.get('C'))
              else:
                  C=float(request.POST.get('C'))
    else:
       C=None
    

    A1 = A
    C1 = C
    

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True


    if form:
      
      
      W_op=request.POST.get('W_op')
      S_op = request.POST.get('S_op')
      D_op = request.POST.get('D_op')



      factor = 0

      tip = 50

      if S_op == 'p':
        tip = 0
      elif A > 1500:
          factor = 0.1
          if S_op == 'e':
            factor += 0.02
          if D_op == 'm':
            factor += 0.02
          elif D_op == 'h':
            factor += 0.04
          if W_op == 'y':
            factor += 0.04
          tip = A * factor
      

      
      tip = tip - (0.2*tip)

      tip_pp = tip/C
      tip_pp = round(tip_pp)

      tip = round(tip)

      context={
         'A1' : A1,
          'C1' : C1,
          'id':1,
          'tip':tip,
          'factor':factor,
          'tip_pp':tip_pp,
          'W_op':W_op,
          'D_op':D_op,
          'S_op':S_op
      }
      return render(request,'pizzatipcalculator.html',context)
      

    else:
     return render(request,'pizzatipcalculator.html',{
          'A1' : 1500,
          'C1' : 4,
          'id':1,
          'tip':200,
          'factor':4,
          'tip_pp':50
     })
    
  else:
    return render(request,'pizzatipcalculator.html',{
          'A1' : 1500,
          'C1' : 4,
          'id':1,
          'tip':200,
          'factor':4,
          'tip_pp':50
    })
