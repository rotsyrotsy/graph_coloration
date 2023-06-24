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

    
    # adjacent.append(Vertice('A',['B','C','D']))
    # adjacent.append(Vertice('B',['A','E','G']))
    # adjacent.append(Vertice('C',['A','D','F']))
    # adjacent.append(Vertice('D',['A','C','F']))
    # adjacent.append(Vertice('E',['B','G']))
    # adjacent.append(Vertice('F',['C','D','G']))
    # adjacent.append(Vertice('G',['B','E','F']))

    adjacent.append(Vertice('C1',['C2','C4','C5','C6','C7','C8','C9']))
    adjacent.append(Vertice('C2',['C1','C3','C5','C6','C8','C9','C10']))
    adjacent.append(Vertice('C3',['C2','C4','C5','C6','C7','C8','C9']))
    adjacent.append(Vertice('C4',['C1','C3','C5','C6','C8','C9','C10']))
    adjacent.append(Vertice('C5',['C1','C2','C3','C4','C6','C7','C10']))
    adjacent.append(Vertice('C6',['C1','C2','C3','C4','C5','C7','C8','C9','C10']))
    adjacent.append(Vertice('C7',['C1','C3','C5','C6','C8','C9','C10']))
    adjacent.append(Vertice('C8',['C1','C2','C3','C4','C6','C7','C10']))
    adjacent.append(Vertice('C9',['C1','C2','C3','C4','C6','C7','C10']))
    adjacent.append(Vertice('C10',['C2','C4','C5','C6','C7','C8','C9']))

    adjacent = graph_coloring(adjacent)

    for item in adjacent :
        print(item.name,"=>",item.color)