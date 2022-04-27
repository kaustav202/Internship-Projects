def drakeequationcalculator(request):
  if request.method=='POST':
    if request.POST.get('A')!=None and request.POST.get('A')!='' :     
              inp=str(request.POST.get('A'))
              if inp.isdigit():
                  A=int(request.POST.get('A'))
              else:
                  A=float(request.POST.get('A'))
    else:
       A=int(A)


    if request.POST.get('S')!=None and request.POST.get('S')!='' :     
              inp=str(request.POST.get('S'))
              if inp.isdigit():
                  S=int(request.POST.get('S'))
              else:
                  S=float(request.POST.get('S'))
    else:
       S=int(S)



    if request.POST.get('Amin')!=None and request.POST.get('Amin')!='' :     
              inp=str(request.POST.get('Amin'))
              if inp.isdigit():
                  Amin=int(request.POST.get('Amin'))
              else:
                  Amin=float(request.POST.get('Amin'))
    else:
       Amin=int(Amin)


    if request.POST.get('Amax')!=None and request.POST.get('Amax')!='' :     
              inp=str(request.POST.get('Amax'))
              if inp.isdigit():
                  Amax=int(request.POST.get('Amax'))
              else:
                  Amax=float(request.POST.get('Amax'))
    else:
       Amax=int(Amax)
    

    if request.POST.get('P')!=None and request.POST.get('P')!='' :     
              inp=str(request.POST.get('P'))
              if inp.isdigit():
                  P=int(request.POST.get('P'))
              else:
                  P=float(request.POST.get('P'))
    else:
       P=int(P)
    

    

    A1 = A
    S1 = S
    Amin1 = Amin
    Amax1 = Amax
    P1 = P
    

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True


    if form:
      
      
      G_op=request.POST.get('G_op')
      
      U_op = request.POST.get('U_op')
      
      age_map = {
        19 : 2.7,
        20 : 1.4 ,
        21 : 1.4,
        22 : 1.4,
        23 : 1.4,
        24 : 1.4,
        25 : 1.27,
        26 : 1.27,
        27 : 1.27,
        28 : 1.27,
        29 : 1.27,
        30 : 1.27,
        31 : 1.27,
        32 : 1.27,
        33 : 1.27,
        34 : 1.27,
        35 : 1.27,
        36 : 1.27,
        37 : 1.27,
        38 : 1.27,
        39 : 1.27,
        40 : 1.27,
        41 : 1.27,
        42 : 1.27,
        43 : 1.27,
        44 : 1.27,
        45 : 0.67,
        46 : 0.67,
        47 : 0.67,
        48 : 1.27,
        49 : 0.67,
        50 : 0.67,
        51 : 0.67,
        52 : 1.27,
        53 : 0.67,
        54 : 0.67,
        55 : 0.67,
      }

      atr_f = A/5
      soc_f = S/5

      age_per = 1

      for i in range(Amin,Amax):
        age_per += age_map[i]
    
      age_f = age_per / 100

      if G_op == 'f':
        g_f = 0.47
      else:
        g_f = 0.51
      
      if U_op == 'y':
        u_f = 0.23
      else:
        U_op == 1
      
      mat_f = P/100

      loc_f = 0.0178

      pop = 1028610328

      o_f = 0.1

      matches =  pop * atr_f * soc_f * age_f * g_f * u_f * loc_f  * mat_f * o_f

      matches = int(matches)

      
      valid = True 
      
      
      context={
          'fa': atr_f,
          'fs': soc_f,
          'fage': age_f,
          'fpar': mat_f,
          'floc': loc_f,
          'fo' : o_f,
          'A1':A1,
          'S1':S1,
          'Amin1':Amin1,
          'Amax1':Amax1,
          'P1':P1,
          'match':matches,
          'G_op':G_op,
          'U_op':U_op,
          'id':1,
          'valid':valid
      }
      return render(request,'drakeequationcalculator.html',context)
      

    else:
     return render(request,'drakeequationcalculator.html',{
          'fa': 0.5,
          'fs': 0.7,
          'fage': 0.01,
          'fpar': 0.48,
          'floc': 0.017,
          'fo' : 0.12,
          'A1':3,
          'S1':3,
          'Amin1':22,
          'Amax1':24,
          'P1':75,
          'match':1217,
          'G_op':'f',
          'U_op':'y',
          'id':1,
          'valid':False
     })
    
  else:
    return render(request,'drakeequationcalculator.html',{
          'fa': 0.5,
          'fs': 0.7,
          'fage': 0.01,
          'fpar': 0.48,
          'floc': 0.017,
          'fo' : 0.12,
          'A1':3,
          'S1':3,
          'Amin1':22,
          'Amax1':24,
          'P1':75,
          'match':1217,
          'G_op':'f',
          'U_op':'y',
          'id':1,
          'valid':False
    })

