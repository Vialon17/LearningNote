
#使用大O表示法给出下述各种情形的运行时间。
Names = ['Alyx', 'Python', 'BigO', 'Lucy', 'Max', 'Martin', 'Arthur', 'Ciri', 'Jane', 'John', 'Mary', 'Michael', 'Davia', 'Thomas', 'Lisa', 'Seven', 'Anna', 'Jack', 'Alice', 'Rose', 'Fran', 'Leo', 'William', 'Maya', 'Victoria', 'Ailee', 'Alex', 'Gianna', 'Weston', 'Jose', 'August', 'Richard', 'Nico', 'Elian', 'Otto', 'Taylor', 'Tommy', 'Violet']
Phones = ['+8617382120012', '+14844731143', '+15853042442', '+16102458163', '+16102458163', '+15853042386', '+18777405932', '+18665445994', '+436703080042', '+436703080013', '+436703080051', '+447441429277', '+447520644202', '+447441429227', '+441245969018', '+442037699224', '+442038850794', '']
#1.3 在电话簿中根据名字查找电话号码。
def set_1():
    name = input('Please inpuut the name:')
    find = False
    for i in Names:
        if i == name:
            find = True
            print('Found! Total counts {} frequency.'.format(i))
            break
    if not find:
        print('Invalue Name.')
#1.4 在电话簿中根据电话号码找人。（提示：你必须查找整个电话簿。)
#1.5 阅读电话簿中每个人的电话号码。
#1.6 阅读电话簿中姓名以A打头的人的电话号码。这个问题比较棘手，它涉及第4章的概念。答案可能让你感到惊讶！

#About Dijkstra's Algorithm
def dikstra(vertex_dict: dict):
    target_path = {}
    for key in vertex_dict:
        target_path[key] = None

def main():
    vertex = {'score': {'record': 5, 'poster': 0},
            'record': {'guitar': 15, 'drum_kit': 20},
            'poster': {'guitar': 30, 'drum_kit': 35},
            'drum_kit': {'piano': 10},
            'guitar': {'piano': 20},
            'piano': None}

# Dijkstra's algorithm
# Graph:
#       -> A (5)    -> C (4)    ->(3)
# start (B->A 8)  (A->D 2)(C ->D 6)  End
#       -> B (2)    -> D (7)    ->(1)
class Graph:
    '''
    Params: Graph -> dict, vertexs -> list 
    '''
    def __init__(self, graph : dict, vertexs : list):
        self.graph = graph
        self.vertexs = vertexs

    @property
    def show(self):
        return self.graph
    
    def addvertex(self, vertex: str) -> int:
        if not isinstance(vertex, str):
            raise TypeError('Need str type.')
        self.vertexs.append(vertex)
        self.graph[vertex] = {}
        return self.vertexs.index(vertex)
    
    def addpath(self, start_vertex, end_vertex, value : int) -> int:
        if start_vertex not in self.vertexs:
            raise Exception('Start Vertex not in this Graph, Please Check!')
        self.graph[start_vertex][end_vertex] = int(value)
        if end_vertex not in self.vertexs:
            self.vertexs.append(end_vertex)
        return value

    def value(self, start_vertex : str, end_vertex : str) -> int:
        if start_vertex not in self.graph or end_vertex not in self.graph[start_vertex]:
            raise Exception('Path Error!')
        return self.graph[start_vertex][end_vertex]
    
def dijk():
    Dijk = Graph(
        {'start':{'A': 5, 'B': 2}, 
         'A':{'C': 4, 'D': 2},
         'B':{'A': 8, 'D': 7},
         'C':{'D': 6, 'end': 3},
         'D':{'end': 1},
         'end':{}
         }, 
        ['start', 'A', 'B', 'C', 'D', 'end']
        )
    cost = {'end': 1000}
    path = {}

if __name__ == '__main__':
    main()