def shoesizecalculator(request):
  if request.method=='POST':
    
    if request.POST.get('B')!=None and request.POST.get('B')!='' :     
              inp=str(request.POST.get('B'))
              if inp.isdigit():
                  B=int(request.POST.get('B'))
              else:
                  B=float(request.POST.get('B'))
    else:
       B=None
    

    B1 = B

    
    country_map = {

      "eu" :  [ 35, 35.5,	36,	37,	37.5,	38,	38.5,	39,	40,	41,	42,	43,	44,	45,	46.5,	48.5 ],

      "ukm" : [ 3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8,	8.5,	10,	11,	12,	13.5],

      "ukf" : [2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8,	9.5,	10.5,	11.5,	13],

      "usm" :  [3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8,	8.5,	9,	10.5,	11.5,	12.5,	14],

      "usf" : [5,	5.5,	6,	6.5,	7,	7.5,	8,	8.5,	9,	9.5,	10,	10.5,	12,	13,	14,	15.5],

      "jpm" :  [21.5,	22,	22.5,	23,	23.5,	24,	24.5,	25,	25.5,	26,	26.5,	27.5,	28.5,	29.5,	30.5,	31.5],

      "jpf" :  [21,	21.5,	22,	22.5,	23,	23.5,	24,	24.5,	25,	25.5,	26,	27,	28,	29,	30,	31],

      "mex" :  [0,	0,	0,	0,	0,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	9,	10,	11,	12.5],

      "bra" :  [33,	33,	34,	35,	35,	36,	36,	37,	38,	39,	40,	41,	42,	43,	44,	46],

      "aum" :  [3,	3.5,	4,	4.5,	5,	5.5,	6, 6.5,	7,	7.5,	8,	8.5,	10,	11,	12,	13.5],

      "auf" :  [5,	5.5,	6, 6.5,	7,	7.5,	8,	8.5,	9,	9.5,	10,	10.5,	12,	13,	14,	15.5],

      "cm" :  [22.8,	23.1,	23.5,	23.8,	24.1,	24.5,	24.8,	25.1,	25.4,	25.7,	26,	26.7,	27.3,	27.9,	28.6,	29.2],

      "in" :  [9,	9.1,	9.4,	9.4,	9.5,	9.6,	9.8,	9.9,	10,	10.1,	10.3,	10.5,	10.8,	11,	11.8,	11.5]

    }



    # ctr = 0
    # for i in range(28,47,2):
    #   f = i*ctr
    #   t = {}
    #   for j in range(10):
    #     curr = base + f
    #     sf = 2*j
    #     for k in range(3):
    #       t[curr+k+1+sf] = l[j]
    #   size_map[i] = t
    #   ctr+=1


    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True

    if form:
      
      c_op = request.POST.get('c_op')
      r_op = request.POST.get('r_op')

      valid = True

      flag = 0

      print(c_op)
      print(B)

      index = -1

      if B < country_map[c_op][0] or B > country_map[c_op][-1]:
        flag = 1

      for i in range(0,16):
        if country_map[c_op][i] > B:
          index = i
          break
      
      if flag == 0:
        s = country_map[r_op][index]
      else:
        s = "Invalid"


      l2 = []

      for key in list(country_map.keys()):
        val = country_map[key]
        l1 = [key] + val
        l2.append(l1)

      context={
          'valid':valid,
          'id':1,
          'B1':B1,
          'c_op': c_op,
          'r_op': r_op,
          's':s,
          'sub': True,
          'flag' : flag,
          'index' : index,
          'cmap' : country_map,
          'l2' : l2
      }

      return render(request,'shoesizecalculator.html',context)
      

    else:
     return render(request,'shoesizecalculator.html',{
          'valid':False,
          'id':1,
          'B1':28,
          'c_op':'cm',
          'r_op': 'cm',
          's':'28',
          'sub': False,
          'flag': 0
     })
    
  else:
    return render(request,'shoesizecalculator.html',{
          'valid':False,
          'id':1,
          'B1':28,
          'c_op':'cm',
          's':'28D',
          'sub': False,
          'flag': 0,
    })
