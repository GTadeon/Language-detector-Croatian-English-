def frek_distr(sekvenca):
    rjecnik = {}
    for dogadaj in sekvenca:
        rjecnik[dogadaj]=rjecnik.get(dogadaj, 0)+ 1
    return rjecnik


def sortiraj_distr(rjecnik):
    return sorted(rjecnik.items(), key=lambda x:-x[1])


def opojavnici(niz_znakova):
    import re
    return re.findall(r'\w+', niz_znakova, re.UNICODE)


def vjer_distr(frek_distr):
  broj_dogadjaja=float(sum(frek_distr.values()))
  for dogadjaj in frek_distr:
    frek_distr[dogadjaj]/=broj_dogadjaja
  return frek_distr


def vjerojatnost_sekvence(sekvenca,vjer_distr):
  from math import log
  vjerojatnost=0.0
  for dogadjaj in sekvenca:
    if dogadjaj in vjer_distr:
      vjerojatnost+=log(vjer_distr[dogadjaj])
  return vjerojatnost


def zagladi(model):
    svi_dogadjaji=set()
    for klasa in model:
        for dogadjaj in model[klasa]:
            svi_dogadjaji.add(dogadjaj)
    for klasa in model:
        for dogadjaj in svi_dogadjaji:
            model[klasa][dogadjaj]=model[klasa].get(dogadjaj,0)+1
        model[klasa]=vjer_distr(model[klasa])
    return model


def klasificiraj(sekvenca,model):
    vjer={}
    for klasa in model:
        vjer[klasa]=vjerojatnost_sekvence(sekvenca,model[klasa])
    return sortiraj_distr(vjer)[0][0]

