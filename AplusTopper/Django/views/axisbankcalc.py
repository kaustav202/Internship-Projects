def axisbankcalculator(request):
  if request.method=='POST':

    if request.POST.get('C')!=None and request.POST.get('C')!='' :     
              inp=str(request.POST.get('C'))
              if inp.isdigit():
                  C=int(request.POST.get('C'))
              else:
                  C=float(request.POST.get('C'))
    else:
       C=None
    
    if request.POST.get('I')!=None and request.POST.get('I')!='' :     
              inp=str(request.POST.get('I'))
              if inp.isdigit():
                  I=int(request.POST.get('I'))
              else:
                  I=float(request.POST.get('I'))
    else:
       I=None

    if request.POST.get('P')!=None and request.POST.get('P')!='' :     
              inp=str(request.POST.get('P'))
              if inp.isdigit():
                  P=int(request.POST.get('P'))
              else:
                  P=float(request.POST.get('P'))
    else:
       P=None
    

    C1 = C
    I1 = I
    P1 = P
    

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True


    if form:
      
      P_op = request.POST.get('P_op')
      
      if P_op == 'a':
        P = P*12
      
      i = I/1200
      
      numerator = ( i * ( (1+i)**(P) ) )
      denominator = ( (1+i)**(P) ) - 1

      emi = C * (numerator/denominator)

      total = emi * P

      emi = round(emi)

      total = round(total)

      Pt = P1
      if P_op == 'm':
        Pt = P1/12
      

      list_of_dict = []

      st = "Year"

      recsum = 0

      for i in range(1,Pt+1):
        d = []
        yr = st + str(i)
        d.append(yr)
        d.append(emi*12*i)
        recsum += emi*12
        rem = total - recsum
        if rem <0:
          rem = 0
        d.append(rem)
        list_of_dict.append(d)


      context={
          'C1' : C1,
          'I1' : I1,
          'P1' : P1,
          'P_op':P_op,
          'inp': 1,
          'valid': True,
          'id':1,
          'emi' : emi,
          'total' : total,
          'li' : list_of_dict
      }
      return render(request,'axisbankcalculator.html',context)
      

    else:
     return render(request,'axisbankcalculator.html',{
          'C1' : 5000,
          'I1' : 7,
          'P1' : 21,
          'P_op':'m',
          'inp': 0,
          'valid': False,
          'id':1,
          'total' : 600000,
          'emi': 6837
     })
    
  else:
    return render(request,'axisbankcalculator.html',{
          'C1' : 5000,
          'I1' : 7,
          'P1' : 21,
          'P_op':'m',
          'inp': 0,
          'valid': False,
          'id':1,
          'total' : 600000,
          'emi': 6837
    })
