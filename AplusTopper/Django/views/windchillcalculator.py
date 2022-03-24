def windchillcalculator(request):
  if request.method=='POST':
 
    if request.POST.get('V')!=None and request.POST.get('V')!='' :     
              inp=str(request.POST.get('V'))
              if inp.isdigit():
                  V=int(request.POST.get('V'))
              else:
                  V=float(request.POST.get('V'))
    else:
       V=None

    if request.POST.get('T')!=None and request.POST.get('T')!='' :     
              inp=str(request.POST.get('T'))
              if inp.isdigit():
                  T=int(request.POST.get('T'))
              else:
                  T=float(request.POST.get('T'))
    else:
       T=None
    

    V1 = V
    T1 = T
    
    speed_conv = {
      'kph': 0.62137119,
      'mps': 2.23693629,
      'kts': 1.15077945,
      'fps': 0.68181818
    }



    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True

    if form:
      
      T_op = request.POST.get('T_op')
      V_op = request.POST.get('V_op')

      if V_op != 'mph':
        V = V*speed_conv[V_op]


      if T_op == "K":
        T = ( ( T - 273.15 ) * 1.8 ) + 32
        T = round(T)
      elif T_op == "C":
        T = (1.8 * T) + 32
        T = round(T)

      valid = True

      
      val = 35.74 + ( 0.6215 * T ) - (35.75 * (V**0.16)) + ( 0.4275 * T * (V**(0.16)) )




      context={
          'valid':valid,
          'id': 1,
          'V1': V1,
          'T1': T1,
          'T_op': T_op,
          'V_op': V_op,
          'val': val
      }
      return render(request,'windchillcalculator.html',context)
      

    else:
     return render(request,'windchillcalculator.html',{
          'valid':False,
          'id': 1,
          'V1': 27,
          'T1': 0,
          'T_op': 'F',
          'V_op': 'mph',
          'val': -24
     })
  else:
    return render(request,'windchillcalculator.html',{
          'valid':False,
          'id': 1,
          'V1': 27,
          'T1': 0,
          'T_op': 'F',
          'V_op': 'mph',
          'val': -24
    })
