def meatcookingtimecalculator(request):
  if request.method=='POST':
    given_data=request.POST.get('given_data')
    
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
    
    

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True

    meat_lookup = {
      'form1' : 'Lamb',
      'form2' : 'Beef',
      'form3' : 'Chicken',
      'form4' : 'Turkey',
      'form5' : 'Fish'
    }



    if form:
      
      #FETCHING THE UNITS
      W_op=request.POST.get('W_op')
      

      #COPYING OF THE VARIABLES
      W1 = W

      #Conversion of units here



      conversion_factors = {
        'p':453.592,
        'kg':1000,
        'o':28.349,
      }
      
      W_c=""
      if W_op != 'g':
        cf = conversion_factors[W_op]
        W=W*cf #convert into grams
        W_c+=f" * {cf} "

      est_time = ""

      meat_cooking_times = {
        "Chicken" : ["25-35 mins","30-40 mins","1:15 - 1:30 hrs","1:30 - 1:45 hrs","1:50 - 2:10 hrs","2:45 - 3:10 hrs"],
        "Turkey" : ["20-30 mins","30-45 mins","1:00 - 1:10 hrs","1:15 - 1:30 hrs","1:35 - 2:10 hrs","2:30 - 3:15 hrs"],
        "Beef" : ["< 20 mins","< 30 mins","1:10 - 1:30 hrs","1:30 - 1:45 hrs","2:00 - 2:15 hrs","2:15 - 2:45 hrs"],
        "Lamb" : ["< 15 mins", "< 15 mins" , "15-20 mins","15-20 mins","25-30 mins","40-45 mins"],
        "Fish" : ["< 10 mins","< 15 mins", "15 - 20 mins","25 - 30 mins","30 - 45 mins","1:15 - 1:30 mins"]
      }

      ind = -1

      if W<=400 and W >10:
        ind = 0
      elif W>400 and W <=700:
        ind = 1
      elif W>700 and W <=1300:
        ind = 2
      elif W>1300 and W<=1800:
        ind = 3
      elif W>1800 and W<=2700:
        ind = 4
      elif W>2700 and W<4500:
        ind = 5

      
  
      meat_type = meat_lookup[given_data]

      est_time = meat_cooking_times[meat_type][ind]

      
         

      context={
         'given_data':given_data,
         'id':1,
         'W':W,
         'W1':W1,
         'W_op':W_op,
         'W_c':W_c,
         'type':meat_type,
         'time':est_time
      }
      return render(request,'meatcookingtimecalculator.html',context)
      

    else:
     return render(request,'meatcookingtimecalculator.html',{
       'given_data':given_data,
         'id':1,
         'W':720,
         'W1':720,
         'W_op':"g",
         'W_c':"NA",
         'type':"Chicken",
         'time':"NA"
     })
    
  else:
    return render(request,'meatcookingtimecalculator.html',{
      'given_data':"form3",
         'id':1,
         'W':720,
         'W1':720,
         'W_op':"g",
         'W_c':"NA",
         'type':"Chicken",
         'time':"NA"
    })
