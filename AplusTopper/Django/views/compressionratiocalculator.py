
def compressionratiocalculator(request):
  if request.method=='POST':
    
    # B is the bore diameter
    # S is the piston stroke
    # T is the head gasket thickness
    # G is the gasket bore
    # C is the deck clearance
    # Vc is the chamber volume
    # Vp is the piston volume 

    #Obtaining the B
    if request.POST.get('B')!=None and request.POST.get('B')!='' :     
              inp=str(request.POST.get('B'))
              if inp.isdigit():
                  B=int(request.POST.get('B'))
              else:
                  B=float(request.POST.get('B'))
    else:
       B=None
    
    #Obtaining the S
    if request.POST.get('S')!=None and request.POST.get('S')!='' :     
              inp=str(request.POST.get('S'))
              if inp.isdigit():
                  S=int(request.POST.get('S'))
              else:
                  S=float(request.POST.get('S'))
    else:
       S=None

   #Obtaining the T
    if request.POST.get('T')!=None and request.POST.get('T')!='' :     
              inp=str(request.POST.get('T'))
              if inp.isdigit():
                  T=int(request.POST.get('T'))
              else:
                  T=float(request.POST.get('T'))
    else:
       T=None

    #Obtaining the G
    if request.POST.get('G')!=None and request.POST.get('G')!='' :     
              inp=str(request.POST.get('G'))
              if inp.isdigit():
                  G=int(request.POST.get('G'))
              else:
                  G=float(request.POST.get('G'))
    else:
       G=None

    #Obtaining the C
    if request.POST.get('C')!=None and request.POST.get('C')!='' :     
              inp=str(request.POST.get('C'))
              if inp.isdigit():
                  C=int(request.POST.get('C'))
              else:
                  C=float(request.POST.get('C'))
    else:
       C=None

    #Obtaining the Vc
    if request.POST.get('Vc')!=None and request.POST.get('Vc')!='' :     
              inp=str(request.POST.get('Vc'))
              if inp.isdigit():
                  Vc=int(request.POST.get('Vc'))
              else:
                  Vc=float(request.POST.get('Vc'))
    else:
       Vc=None


    if request.POST.get('Vp')!=None and request.POST.get('Vp')!='' :     
              inp=str(request.POST.get('Vp'))
              if inp.isdigit():
                  Vp=int(request.POST.get('Vp'))
              else:
                  Vp=float(request.POST.get('Vp'))
    else:
       Vp=None
       
    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True
  
    if form:
      
      #FETCHING THE UNITS
      B_op=request.POST.get('B_op')
      S_op=request.POST.get('S_op')
      T_op=request.POST.get('T_op')
      G_op=request.POST.get('G_op')
      C_op=request.POST.get('C_op')
      Vc_op=request.POST.get('Vc_op')
      Vp_op=request.POST.get('Vp_op')

      #COPYING OF THE VARIABLES
      B1 = B
      S1 = S
      T1 = T
      G1 = G
      C1 = C
      Vc1 = Vc
      Vp1 = Vp

      #Conversion of units here
      
      if B_op != 'in':
        B=B*39.37

      if S_op != 'in':
        S=S*39.37

      if T_op != 'in':
        T=T*39.37
      
      if G_op != 'in':
        G=G*39.37
      
      if C_op != 'in':
        C=C*39.37
      
      #Calculation
      t1 = (B**2)*S*3.14159
      t2 = Vc + Vp + ((G**2)*T*3.14159) + ((B**2)*T*3.14159)
      val = (t1 + t2)/t2
            
         

      context={

         'id':1,
         'val' : val,
         'B' : B,
         'S' : S,
         'T' : T,
         'G' : G,
         'C' : C,
         'Vc' : Vc,
         'Vp' : Vp,
        'B1' : B1,
        'S1' : S1,
        'T1' : T1,
        'G1' : G1,
        'C1' : C1,
        'Vc1' : Vc1,
        'Vp1' : Vp1,
         'B_op':B_op,
         'S_op':S_op,
         'T_op':T_op,
         'G_op':G_op,
         'C_op':C_op,
         'Vc_op':Vc_op,
         'Vp_op':Vp_op,

      }
      return render(request,'compressionratiocalculator.html',context)

    else:
     return render(request,'compressionratiocalculator.html',{'id': 0, 'B1':7 , 'S1': 2.5 , 'T1' : 0.5 , 'G1' : 4 , 'C1' : 3 , 'Vc1' : 5 ,'Vp1' : 4})
    
  else:
    return render(request,'compressionratiocalculator.html',{'id' : 0, 'B1':7 , 'S1': 2.5 , 'T1' : 0.5 , 'G1' : 4 , 'C1' : 3 , 'Vc1' : 5 ,'Vp1' : 4})
