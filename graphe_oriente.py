class way:
    def __init__(self, sometListe, length):
        self.sometListe = sometListe
        self.length = length

def plusCourtChemin(matrix,listeSommet,depart,ariver):
    indiceDepart = compare_with_list(depart, listeSommet)
    indiceAriver = compare_with_list(ariver, listeSommet)
    temp = way([listeSommet[indiceDepart]],0)
    liste = []
    liste.append(temp)
    resolve(matrix,listeSommet,indiceAriver,liste)
    newListe = []
    for el in liste:
        
        if el.sometListe[-1] == listeSommet[indiceAriver]:
            newListe.append(el)
            print(el.sometListe)
            print(el.length)
    return newListe
    

def resolve(matrix,listeSommet,indiceAriver,liste):
    for el in liste:
        indiceDepart = compare_with_list(el.sometListe[-1], listeSommet)
        ligneDepart = matrix[indiceDepart]
        for i in range(len(ligneDepart)):
            if ligneDepart[i]!=0 and compare_with_list(listeSommet[i],el.sometListe)<0:
                newliste = list(el.sometListe)
                newliste.append(listeSommet[i])
                temp = way(newliste,el.length+ligneDepart[i])
                liste.append(temp)


    

def defineDepartArive(matrix,listeSommet,depart,ariver,liste,listeSometUtiliser = []):
    indiceDepart = compare_with_list(depart, listeSommet)
    indiceAriver = compare_with_list(ariver, listeSommet)
    
    
    if compare_with_list(listeSommet[indiceDepart], listeSometUtiliser)<0:
        listeSometUtiliser.append(listeSommet[indiceDepart])
    
    temp = way([listeSommet[indiceDepart]],0)
    for i in range(len(listeSommet)):
        for i in range(len(matrix[indiceDepart])):
            if matrix[indiceDepart][i] != 0 and compare_with_list(listeSommet[i],temp.sometListe)<0:
                
                temp.sometListe.append(listeSommet[i])
                temp.length += matrix[indiceDepart][i]
                if i == indiceAriver:
                    liste.append(temp)
                    
                else:
                    defineDepartArive(matrix,listeSommet,listeSommet[i],ariver,liste,listeSometUtiliser)
            


def compare_with_list(element, my_list):
    
    for i in range(0,len(my_list)):
        if element == my_list[i]:
            return i
    return -1

def listeToMatrix(listeArrete,listeSommet):
    liste = []
    for sommet in listeSommet:
        ligne = [0 for _ in range(len(listeSommet))]
        for arrete in listeArrete:
            place = compare_with_list(sommet, arrete)
            if place==0:
                indice = compare_with_list(arrete[1],listeSommet)
                ligne[indice] = arrete[2]
        liste.append(ligne)
    
    return liste



def compare_with_list(element, my_list):
    
    for i in range(0,len(my_list)):
        if element == my_list[i]:
            return i
    return -1

def get_min(list):
    min = list[0]
    for el in list:
        if(el.length < min.length):
            min = el
    return min


liSommet = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','A']
liArete = [
    ['c1','c6',7],
    ['c1','c4',5],
    ['c1','c2',10],
    ['c4','c2',6],
    ['c6','c2',2],
    ['c2','c5',8],
    ['c2','c3',6],
    ['c2','c7',2],
    ['c7','c5',4],
    ['c7','c3',3],
    ['c5','A',12],
    ['c3','A',11],
]


liste = []
matrix = [[0, 10, 0, 5, 0, 7, 0, 0, 0, 0],
[0, 0, 6, 0, 8, 0, 2, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
[0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 12],
[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 0, 4, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
ls = plusCourtChemin(matrix, liSommet,'c1','A')
mini = get_min(ls)
print("=========== Minimum ===========")
print(mini.sometListe)
print(mini.length)


