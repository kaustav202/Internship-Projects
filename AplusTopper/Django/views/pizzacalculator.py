def pizzacalculator(request):
  if request.method=='POST':
    
    """ given data denotes the type of meat
        W is the entered weight to be cooked
    """

    if request.POST.get('C')!=None and request.POST.get('C')!='' :     
              inp=str(request.POST.get('C'))
              if inp.isdigit():
                  C=int(request.POST.get('C'))
              else:
                  C=float(request.POST.get('C'))
    else:
       C=None
    

    
    C1 = C
    

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True


    if form:
      
      
      A_op = request.POST.get('A_op')
      S_op = request.POST.get('S_op')
      Cs_op = request.POST.get('Cs_op')
      

      pizza =   round( C/2 ) + round ( C/5 )

      
      if A_op == 'b':
        pizza = round( pizza + (pizza * 0.4))
      elif A_op == 's':
        pizza = round ( pizza - (pizza * 0.2))

      if S_op == 'l':
        pizza = round(pizza - (pizza*0.5))
      elif S_op == 's':
        pizza = round(pizza + (pizza * 0.5))

      if Cs_op == 't':
        pizza = round( pizza + (pizza * 0.1))

      

      context={
          'C1' : C1,
          'id':1,
          'pizza':pizza,
          'A_op':A_op,
          'S_op':S_op,
          'Cs_op':Cs_op,
          'inp': 1
      }
      return render(request,'pizzacalculator.html',context)
      

    else:
     return render(request,'pizzacalculator.html',{
          'C1' : 5,
          'id':1,
          'pizza':4,
          'A_op': 'medium',
          'S_op': 'medium',
          'Cs_op': 'n',
          'inp' : 0
     })
    
  else:
    return render(request,'pizzacalculator.html',{
          'C1' : 5,
          'id':1,
          'pizza':4,
          'A_op': 'medium',
          'S_op': 'medium',
          'Cs_op': 'n',
          'inp': 0
    })
