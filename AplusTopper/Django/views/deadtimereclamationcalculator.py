def deadtimereclamationcalculator(request):
  if request.method=='POST':
    if request.POST.get('T')!=None and request.POST.get('T')!='' :     
              inp=str(request.POST.get('T'))
              if inp.isdigit():
                  T=int(request.POST.get('T'))
              else:
                  T=float(request.POST.get('T'))
    else:
       T=int(T)


    if request.POST.get('H')!=None and request.POST.get('H')!='' :     
              inp=str(request.POST.get('H'))
              if inp.isdigit():
                  H=int(request.POST.get('H'))
              else:
                  H=float(request.POST.get('H'))
    else:
       H=int(H)



    if request.POST.get('E')!=None and request.POST.get('E')!='' :     
              inp=str(request.POST.get('E'))
              if inp.isdigit():
                  E=int(request.POST.get('E'))
              else:
                  E=float(request.POST.get('E'))
    else:
       E=int(E)


    if request.POST.get('O')!=None and request.POST.get('O')!='' :     
              inp=str(request.POST.get('O'))
              if inp.isdigit():
                  O=int(request.POST.get('O'))
              else:
                  O=float(request.POST.get('O'))
    else:
       O=int(O)
    

    if request.POST.get('P')!=None and request.POST.get('P')!='' :     
              inp=str(request.POST.get('P'))
              if inp.isdigit():
                  P=int(request.POST.get('P'))
              else:
                  P=float(request.POST.get('P'))
    else:
       P=int(P)


    if request.POST.get('L')!=None and request.POST.get('L')!='' :     
              inp=str(request.POST.get('L'))
              if inp.isdigit():
                  L=int(request.POST.get('L'))
              else:
                  L=float(request.POST.get('L'))
    else:
       L=int(L)

    if request.POST.get('S')!=None and request.POST.get('S')!='' :     
              inp=str(request.POST.get('S'))
              if inp.isdigit():
                  S=int(request.POST.get('S'))
              else:
                  S=float(request.POST.get('S'))
    else:
       S=int(S)
    

    T1 = T
    H1 = H
    E1 = E
    O1 = O
    P1 = P
    L1 = L
    S1 = S
    

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True


    if form:


      T_op=request.POST.get('T_op')
      if T_op == 'h':
        T*= 60
        T = round(T,2)


      H_op = request.POST.get('H_op')
      if H_op == 'h':
        H*= 60
        H = round(H,2)


      E_op = request.POST.get('E_op')
      if E_op == 'h':
        E*= 60
        E = round(E,2)


      O_op = request.POST.get('O_op')
      if O_op == 'h':
        O *= 60 
        O = round(O,2)


      P_op = request.POST.get('P_op')
      if P_op == 'm':
        P /= 60
        P = round(P,2)


      valid = True 


      total = T + H + E + O
      total = round(total,2)


      total_hr = int(total/60)
      total_wk = int(total_hr * 5.5)
      total_mn = total_wk * 4
      total_yr = total_mn * 12


      eff_time = (L/100) * total_wk
      eff_time *= S


      episodes =  int(eff_time/P)
      episodes_wk = episodes
      episodes_mn = episodes_wk * 4
      episodes_yr = episodes_mn * 12



      context={
          'T1':T1,
          'H1':H1,
          'E1':E1,
          'O1':O1,
          'P1':P1,
          'L1':L1,
          'S1':S1,
          'T_op':T_op,
          'H_op':H_op,
          'E_op':E_op,
          'O_op':O_op,
          'P_op':P_op,
          'dt_wk': total_wk,
          'dt_mn': total_mn,
          'dt_yr': total_yr,
          'ep_wk' : episodes_wk,
          'ep_mn' : episodes_mn,
          'ep_yr' : episodes_yr,
          'id':1,
          'valid':valid
      }
      return render(request,'deadtimereclamationcalculator.html',context)
      

    else:
     return render(request,'deadtimereclamationcalculator.html',{
         'T1':30,
          'H1':0,
          'E1':10,
          'O1':60,
          'P1':45,
          'L1':95,
          'S1':1,
          'T_op':'m',
          'H_op':'m',
          'E_op':'m',
          'O_op':'m',
          'P_op':'m',
          'dt_wk': 7,
          'dt_mn': 30,
          'dt_yr': 380,
          'ep_wk' : 9,
          'ep_mn' : 40,
          'ep_yr' : 450,
          'id':1,
          'valid':False
     })
    
  else:
    return render(request,'deadtimereclamationcalculator.html',{
          'T1':30,
          'H1':0,
          'E1':10,
          'O1':60,
          'P1':45,
          'L1':95,
          'S1':1,
          'T_op':'m',
          'H_op':'m',
          'E_op':'m',
          'O_op':'m',
          'P_op':'m',
          'dt_wk': 7,
          'dt_mn': 30,
          'dt_yr': 380,
          'ep_wk' : 9,
          'ep_mn' : 40,
          'ep_yr' : 450,
          'id':1,
          'valid':False
    })
