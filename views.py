from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
import pyrebase

config = {
    "apiKey": "AIzaSyBcDnaaaYy6Uad3VajrY_79WXHY4DdPz2k",
    "authDomain": "license-plate-bba1e.firebaseapp.com",
    "databaseURL": "https://license-plate-bba1e-default-rtdb.firebaseio.com",
    "projectId": "license-plate-bba1e",
    "storageBucket": "license-plate-bba1e.appspot.com",
    "messagingSenderId": "823387556064",
    "appId": "1:823387556064:web:7814d8777e2839f4f16885",
    "measurementId": "G-XD20H1K3LG"
  };
firebase = pyrebase.initialize_app(config)
database = firebase.database()

def button(request):
    return render(request, 'home.html')

def output(request):
    data=requests.get("test2.py")
    print(data.text)
    data=data.text
    return render(request,'home.html' ,{'data':data})
def external(request):
    out=run([sys.executable,'/home//pi//templates//buttonpython//test2.py'],shell=False,universal_newlines=True,stdout=PIPE)
    print(out)
    return render(request,'home.html',{'data1':out.stdout})

def check(request):
          if request.method == 'GET':
            search = request.GET.get('inn')
            search = search.upper()
            print(search)
            datas = database.child('details').shallow().get().val()
            reg_id=[]
            for i in datas:

                reggl = database.child('details').child(i).child('reg').get().val()
                reggl = str(reggl)+"$"+str(i)
                reg_id.append(reggl)

            matching=[str(string) for string in reg_id if search in string.upper()]

            s_reg=[]
            s_id=[]

            for i in matching:

                reg,id=i.split("$")
                s_reg.append(reg)
                s_id.append(id)
                print(s_reg)
                print(s_id)

            address=[]
            for i in s_id:

                 aree=database.child('details').child(i).child('address').get().val()
                 address.append(aree)



            cla=[]
            for i in s_id:

                 cla_lis=database.child('details').child(i).child('class').get().val()
                 cla.append(cla_lis)



            fue=[]
            for i in s_id:

                 fue_lis=database.child('details').child(i).child('fuel').get().val()
                 fue.append(fue_lis)



            model=[]
            for i in s_id:

                 modelj=database.child('details').child(i).child('model').get().val()
                 model.append(modelj)



            owner=[]
            for i in s_id:

                 ownee=database.child('details').child(i).child('owner').get().val()
                 owner.append(ownee)

            reg=[]
            for i in s_id:

                 reggl=database.child('details').child(i).child('reg').get().val()
                 reg.append(reggl)



            refmfg=[]
            for i in s_id:

                 reff=database.child('details').child(i).child('refmfg').get().val()
                 refmfg.append(reff)



            reglocation=[]
            for i in s_id:

                 regg=database.child('details').child(i).child('reglocation').get().val()
                 reglocation.append(regg)


            validity=[]
            for i in s_id:

                 valii=database.child('details').child(i).child('validity').get().val()
                 validity.append(valii)



            comb_lis = zip(s_id,s_reg,address,cla,fue,model,owner,refmfg,validity)
            return render(request, 'home.html' ,{'comb_lis':comb_lis})
          else:
                datas = database.child('details').shallow().get().val()
                lis_dat=[]
                for i in datas:

                    lis_dat.append(i)

                lis_dat.sort(reverse=True)


                address=[]
                for i in lis_dat:

                     aree=database.child('details').child(i).child('address').get().val()
                     address.append(aree)



                cla=[]
                for i in lis_dat:

                     cla_lis=database.child('details').child(i).child('class').get().val()
                     cla.append(cla_lis)



                fue=[]
                for i in lis_dat:

                     fue_lis=database.child('details').child(i).child('fuel').get().val()
                     fue.append(fue_lis)



                model=[]
                for i in lis_dat:

                     modelj=database.child('details').child(i).child('model').get().val()
                     model.append(modelj)



                owner=[]
                for i in lis_dat:

                     ownee=database.child('details').child(i).child('owner').get().val()
                     owner.append(ownee)

                reg=[]
                for i in lis_dat:

                     reggl=database.child('details').child(i).child('reg').get().val()
                     reg.append(reggl)



                refmfg=[]
                for i in lis_dat:

                     reff=database.child('details').child(i).child('refmfg').get().val()
                     refmfg.append(reff)



                reglocation=[]
                for i in lis_dat:

                     regg=database.child('details').child(i).child('reglocation').get().val()
                     reglocation.append(regg)



                reg=[]
                for i in lis_dat:

                     reggl=database.child('details').child(i).child('reg').get().val()
                     reg.append(reggl)



                validity=[]
                for i in lis_dat:

                     valii=database.child('details').child(i).child('validity').get().val()
                     validity.append(valii)



                comb_lis = zip(lis_dat,address,cla,fue,model,owner,refmfg,reg,reglocation,validity)


                return render(request, 'home.html' ,{'comb_lis':comb_lis})
