def beachpriceindexcalculator(request):
  if request.method=='POST':

    if request.POST.get('S')!=None and request.POST.get('S')!='' :     
              inp=str(request.POST.get('S'))
              if inp.isdigit():
                  S=int(request.POST.get('S'))
              else:
                  S=float(request.POST.get('S'))
    else:
       S=int(S)


    if request.POST.get('W')!=None and request.POST.get('W')!='' :     
              inp=str(request.POST.get('W'))
              if inp.isdigit():
                  W=int(request.POST.get('W'))
              else:
                  W=float(request.POST.get('W'))
    else:
       W=int(W)


    if request.POST.get('B')!=None and request.POST.get('B')!='' :     
              inp=str(request.POST.get('B'))
              if inp.isdigit():
                  B=int(request.POST.get('B'))
              else:
                  B=float(request.POST.get('B'))
    else:
       B=int(B)
    

    if request.POST.get('I')!=None and request.POST.get('I')!='' :     
              inp=str(request.POST.get('I'))
              if inp.isdigit():
                  I=int(request.POST.get('I'))
              else:
                  I=float(request.POST.get('I'))
    else:
       I=int(I)
    

    if request.POST.get('L')!=None and request.POST.get('L')!='' :     
              inp=str(request.POST.get('L'))
              if inp.isdigit():
                  L=int(request.POST.get('L'))
              else:
                  L=float(request.POST.get('L'))
    else:
       L=int(L)


    if request.POST.get('F')!=None and request.POST.get('F')!='' :     
              inp=str(request.POST.get('F'))
              if inp.isdigit():
                  F=int(request.POST.get('F'))
              else:
                  F=float(request.POST.get('F'))
    else:
       F=int(F)
    

    S1,S2 = S,S
    W1,W2 = W,W
    B1,B2 = B,B
    I1,I2 = I,I
    L1,L2 = L,L
    F1,F2 = F,F
    

    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True


    if form:
      

      W_op=request.POST.get('W_op')
      if W_op == 'r':
        W1/= 76.28
        W1 = round(W1,2)
      S_op = request.POST.get('S_op')
      if S_op == 'r':
        S1/= 76.28
        S1 = round(S1,2)
      B_op = request.POST.get('B_op')
      if B_op == 'r':
        B1/= 76.28
        B1 = round(B1,2)
      I_op = request.POST.get('I_op')
      if I_op == 'r':
        I1/= 76.28
        I1 = round(I1,2)
      L_op = request.POST.get('L_op')
      if L_op == 'r':
        L1/= 76.28
        L1 = round(L1,2)
      F_op = request.POST.get('F_op')
      if F_op == 'r':
        F1/= 76.28
        F1 = round(F1,2)
      


      valid = True 

      total = 30
      total = S1 + W1 + B1 + I1 + L1 + F1 

      price_index = {
        15.65 : 'Cua Dai Beach in Hoi An, Vietnam',
        16.85 : 'City Beach in Nha Trang, Vietnam',
        18.67 : 'Long Beach in Phu Quoc, Vietnam',
        20.73 : 'Mandrem Beach in Goa',
        22.71 : 'Soma Bay in South Hurghada, Egypt',
        23.59 : 'Dhanushkodi Beach in Pamban Island, India',
        24.72 : 'Bahia Balandra in La Paz, Mexico',
        25.92 : 'Nusa Lembongan in Bali, Indonesia',
        26.78 : 'Thong Nai Pan Noi in Surat Thani, Thailand',
        27.49 : 'Gulangyu in Xiamen, China',
        28.79 : 'Tela Bay in Atlántida, Honduras',
        30.93 : 'Monastir in Sahel, Tunisia',
        32.99 : 'Yoff in Dakar, Senegal',
        33.91 : 'Cap Skirring in Basse Casamance, Senegal',
        34.46 : 'Gurteen in Connemara, Ireland',
        34.56 : 'Deauville Beach in Normandy, France',
        35.99 : 'Ostende in West Flanders, Belgium',
        36.77 : "Hendry's Beach in California, United States",
        37.23 : 'Puerto Villamil in Isla Isabela, Ecuador',
        38.79 : 'El Golfo in Lanzarote, Canary Islands, Spain',
        40.97 : 'Pentle Bay in Isles of Scilly',
        41.38 : 'Silver Beach in Beihai, China ',
        42.99 : 'Grand Beach in Manitoba, Canada',
        44.72 : 'Blankenberge in West Flanders, Belgium',
        46.91 : 'Male Beach in Male, Maldives',
        46.95 : 'Long Beach in Kadavu, Fiji',
        47.68 : 'Muri Beach in Rarotonga, Cook Islands',
        48.5  : 'Kokrobite Beach in Greater Accra, Ghana',
        49.56 : 'Yasawa Island in Yasawa Island, Fiji',
        50.95 : 'Palombaggia Beach in Corsica, France',
        51.59 : 'Vlissingen in Zeeland, Netherlands',
        51.98 : 'Playa del Carmen in Quintana Roo, Mexico',
        52.81 : 'Terschelling in Friesland, Netherlands',
        53.71 : 'Tofta in Gotland, Sweden',
        53.98 : 'Naples Beaches in Florida, United States',
        54.49 : 'Sandhammaren in Ystad, Sweden',
        55.95 : 'Nishihama Beach in Okinawa, Japan',
        56.9 : 'Ålö storsand in Stockholm Archipelago, Sweden',
        57.48 : 'Plage de Santa Giulia in Corse-du-Sud, France',
        57.81 : 'Blokhus Beach in Jammerbugt, Denmark',
        58.38 : 'Böda in Öland, Sweden',
        58.86 : 'Anse Soleil Beach in Mahé, Seychelles',
        59.38 : 'Ribersborg in Malmö, Sweden',
        59.79 : 'Plage Saint-Clair in Cote d’Azur, France',
        60.11 : 'Gulf Shores in Alabama, United States',
        60.24 : 'Hamresanden in Kristiansand, Norway ',
        60.31 : 'Pereybere Beach in Grand Baie, Mauritius',
        60.59 : 'Côte des Basques in Biarritz, France',
        60.86 : 'Lannio in Salerno, Italy',
        70.52 : 'Seljesanden Beach in Selje, Norway',
        72.24 : 'Manly Beach in Sydney, New South Wales, Australia',
        73.89 : 'Plage de Pampelonne in Cote d’Azur, France',
        74.07 : 'Main Beach in New York, United States',
        74.79 : 'South Beach in Florida, United States ',
        75.52 : 'Waikiki in Hawaii, United States',
        76.23 : 'Solanas Cagliari in Sardinia, Italy',
        81.88 : 'Yonaha Maehama Beach in Okinawa, Japan',
        89.19 : 'Finale Ligure in Liguria, Italy',
        91.5  : 'Anse Vata in Noumea, New Caledonia'

      }
      
      minpair = (15.65 , 'Cua Dai Beach in Hoi An, Vietnam')
      maxpair = (91.5  , 'Anse Vata in Noumea, New Caledonia')

      key_list = []

      for key in sorted(price_index.keys()):
          key_list.append(key)


      (prev,next_,res,prev_key,next_key) = ('','','','','')

      if total > key_list[-1]:
        target = 'E'
      elif total < key_list[0]:
        target = 'C'
      else:
        for key in key_list:
                if key >= total :
                  target = key
                  prev_ind = key_list.index(key) - 1
                  next_ind = key_list.index(key) + 1
                  prev_key = key_list[prev_ind]
                  next_key = key_list[next_ind]
                  break
        prev = price_index[prev_key]
        next_ = price_index[next_key]
        res = price_index[target]


      res_key = target


      def quantify(t):
        if max(t,minpair[0]) == t:
          q1 = round(t/minpair[0],2)
          lab1 = 'expensive'
        else:
          q1 = round(minpair[0]/t,2)
          lab1 = 'cheaper'
        if max(t,maxpair[0]) == maxpair[0]:
          q2 = round(maxpair[0]/t,2)
          lab2 = 'cheaper'
        else:
          q2 = round(t/maxpair[0],2)
          lab2 = 'expensive'
        return [(q1,lab1),(q2,lab2)]
      
      l = quantify(total)



      context={
          'S1':S2,
          'W1':W2,
          'B1':B2,
          'I1':I2,
          'L1':L2,
          'F1':F2,
          'S_op':S_op,
          'W_op':W_op,
          'B_op':B_op,
          'I_op':I_op,
          'L_op':L_op,
          'F_op':F_op,
          'res_key':res_key,
          'res_val':res,
          'prev_key':prev_key,
          'prev_val':prev,
          'next_key': next_key,
          'next_val':next_,
          'q1': l[0][0],
          'lab1':l[0][1],
          'q2':l[1][0],
          'lab2':l[1][1],
          'id':1,
          'valid':valid
      }
      return render(request,'beachpriceindexcalculator.html',context)
      

    else:
     return render(request,'beachpriceindexcalculator.html',{
          'S1':4,
          'W1':1,
          'B1':2,
          'I1':2,
          'L1':5,
          'F1':2,
          'S_op':'d',
          'W_op':'d',
          'B_op':'d',
          'I_op':'d',
          'L_op':'d',
          'F_op':'d',
          'res_key':18.72,
          'res_val':'Cua Dai Beach in Hoi An, Vietnam',
          'prev_key':17.85,
          'prev_val':'City Beach in Nha Trang, Vietnam',
          'next_key': 19.21,
          'next_val': 'Long Beach in Phu Quoc, Vietnam',
          'q1':1.14,
          'lab1':'expensive',
          'q2':5.21,
          'lab2':'cheaper',
          'id':1,
          'valid':False
     })
    
  else:
    return render(request,'beachpriceindexcalculator.html',{
          'valid':False,
          'id':1,
          'S1':4,
          'W1':1,
          'B1':2,
          'I1':2,
          'L1':5,
          'F1':2,
          'S_op':'d',
          'W_op':'d',
          'B_op':'d',
          'I_op':'d',
          'L_op':'d',
          'F_op':'d',
          'res_key':18.72,
          'res_val':'Cua Dai Beach in Hoi An, Vietnam',
          'prev_key':17.85,
          'prev_val':'City Beach in Nha Trang, Vietnam',
          'next_key': 19.21,
          'next_val': 'Long Beach in Phu Quoc, Vietnam',
          'q1':1.14,
          'lab1':'expensive',
          'q2':5.21,
          'lab2':'cheaper',
    })
