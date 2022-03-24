def torquecalculator(request):
  if request.method=='POST':
    
    if request.POST.get('V')!=None and request.POST.get('V')!='' :     
              inp=str(request.POST.get('V'))
              if inp.isdigit():
                  V=int(request.POST.get('V'))
              else:
                  V=float(request.POST.get('V'))
    else:
       V=None
    
    V1 = V

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True

    if form:
      
      i_op = request.POST.get('i_op')
      o_op = request.POST.get('o_op')

      conv_in = {
        'ozf.in' : 0.00706,
        'lbf.in' : 0.113,
        'lbf.ft' : 1.36,
        'mN.m' : 0.001,
        'cN.m' : 0.01,
        'gf.cm' : 0.0001,
        'kgf.cm' : 0.0981,
        'kgf.m' : 9.81
      }

      conv_out = {
        'ozf.in' : 142,
        'lbf.in' : 8.85,
        'lbf.ft' : 0.738,
        'mN.m' : 1000,
        'cN.m' : 100,
        'gf.cm' : 10200,
        'kgf.cm' : 10.2,
        'kgf.m' : 0.102
      }

      temp = V
      conv_fact = 1

      if i_op != 'N.m':
        temp = round(conv_in[i_op] * V , 4)
        conv_fact =  conv_in[i_op]


      if o_op != 'N.m':
        val = round(temp * conv_out[o_op] , 4)
        conv_fact *= conv_out[o_op]
      else:
        val = temp

      context={
          'V1':V1,
          'id':1,
          'i_op': i_op,
          'o_op':o_op,
          'val' : val,
          'valid' : 1,
          'conv_fact' : conv_fact
      }
      return render(request,'torquecalculator.html',context)
      
    else:
     return render(request,'torquecalculator.html',{
          'V1':12,
          'id':1,
          'i_op': 'N.m',
          'o_op': 'N.m',
          'val' : 12,
          'valid' : 0,
          'conv_fact' : 1
     })
    
  else:
    return render(request,'torquecalculator.html',{
          'V1':12,
          'id':1,
          'i_op': 'N.m',
          'o_op': 'N.m',
          'val' : 12,
          'valid' : 0,
          'conv_fact' : 1
    })
