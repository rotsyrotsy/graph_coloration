from coloration import graph_coloring
from coloration import Vertice

if __name__ == '__main__':
    adjacent=[]
    # adjacent.append(Vertice('A',['B','C','D','G']))
    # adjacent.append(Vertice('B',['A','C','D','E','G']))
    # adjacent.append(Vertice('C',['A','B','D','F','G']))
    # adjacent.append(Vertice('D',['A','B','C','E','F']))
    # adjacent.append(Vertice('E',['B','D','F','G']))
    # adjacent.append(Vertice('F',['C','D','E','G']))
    # adjacent.append(Vertice('G',['A','B','C','E','F']))

    
    # adjacent.append(Vertice('P1',['P2','P3','P4']))
    # adjacent.append(Vertice('P2',['P1','P3','P5']))
    # adjacent.append(Vertice('P3',['P1','P2','P4']))
    # adjacent.append(Vertice('P4',['P1','P3']))
    # adjacent.append(Vertice('P5',['P2','P6']))
    # adjacent.append(Vertice('P6',['P5']))

    
    adjacent.append(Vertice('A',['B','C','D']))
    adjacent.append(Vertice('B',['A','E','G']))
    adjacent.append(Vertice('C',['A','D','F']))
    adjacent.append(Vertice('D',['A','C','F']))
    adjacent.append(Vertice('E',['B','G']))
    adjacent.append(Vertice('F',['C','D','G']))
    adjacent.append(Vertice('G',['B','E','F']))

    adjacent = graph_coloring(adjacent)

    for item in adjacent :
        print(item.name,"=>",item.color)