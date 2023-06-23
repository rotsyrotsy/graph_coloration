class Vertice:
    def __init__(self, name:str, adjacent:list):
        self.name = name
        self.adjacent = adjacent
        self.color=None
    
    def set_color(self, color):
        self.color = color


def graph_coloring(my_list):
    sorted_list = sorted(my_list, key=lambda x: len(x.adjacent), reverse=True)
    init_color="color"
    result = []
    i=1
    color = init_color
    while len(sorted_list)>0:
        temp = sorted_list[0]
        temp.set_color(color)
        result.append(temp)

        if len(sorted_list)==1:
            sorted_list.remove(temp)

        same_color=[]
        for item in sorted_list:
            if item != temp:
                if temp.name not in item.adjacent:
                    if item.color is None:
                        item.set_color(color)
                        result.append(item)
                        same_color.append(item)
        
        index2=0
        while index2<len(same_color):
            temp2 = same_color[index2]
            for item in same_color:
                if item != temp2:
                    if temp2.name in item.adjacent:
                        item.set_color(None)
                        same_color.remove(item)
                        result.remove(item)
            index2+=1

        for item in same_color:
            if item in sorted_list:
                sorted_list.remove(item)

        if temp in sorted_list:
            sorted_list.remove(temp)

        color = init_color+str(i)
        i+=1

    return result