from py2neo import Node, Relationship, Graph
import copy

NODE_ALL_LIST = {}
NODE_LIST = {}
EDGES_LIST = {}


# 节点注册
def node_list_add_node(node_type=None):
    if node_type is None:
        return None
    else:
        global NODE_LIST
        global NODE_ALL_LIST
        if node_type.name in NODE_ALL_LIST:
            print("节点已注册")
            return NODE_ALL_LIST[node_type.name]
        else:

            NODE_LIST[node_type.name] = copy.deepcopy(node_type)
            NODE_ALL_LIST[node_type.name] = copy.deepcopy(node_type)
            print(node_type.mod)
            return NODE_ALL_LIST[node_type.name]


# 节点删除
def node_list_del_node(node_type=None):
    if node_type is None:
        return None
    else:
        global NODE_LIST
        if node_type.name in NODE_LIST:
            del NODE_LIST[node_type.name]
        else:
            print("节点已删除")
            return None


# 边注册
def edges_list_add_node(edges_type=None):
    if edges_type is None:
        return None
    else:
        global EDGES_LIST
        EDGES_LIST[edges_type.start_node.name + '-' + edges_type.over_node.name] = edges_type


# 边删除
def edges_list_del_node(edges_type=None):
    if edges_type is None:
        return None
    else:
        global EDGES_LIST
        if edges_type.name in EDGES_LIST:
            del EDGES_LIST[edges_type.name]
        else:
            print("边已删除")
            return None


def make():
    neo4j = []
    print(NODE_LIST)
    for i in NODE_LIST:
        print(i,NODE_LIST[i].mod)
        # x = Node(NODE_LIST[i].mod, name=NODE_LIST[i].name)
        x = 'CREATE (a :' + NODE_LIST[i].mod + ' {name:' + i + '})'
        neo4j.append(copy.deepcopy(x))
    print(neo4j)

# 节点类
class NodeType:
    def __new__(cls, name=None, mod='other', value=None):
        if name is None:
            print('实例化失败')
            return None
        else:
            cls.name = copy.deepcopy(name)
            cls.mod = copy.deepcopy(mod)
            cls.value = copy.deepcopy(value)
            state = node_list_add_node(copy.deepcopy(cls))
            return copy.deepcopy(state)


# 边
class EdgesType:
    def __init__(self, start_node=None, value=None, over_node=None):
        if start_node is None or over_node is None:
            print('边创建失败')
            pass
        else:
            self.start_node = start_node
            self.value = value
            self.over_node = over_node
            node_list_del_node(start_node)
            node_list_del_node(over_node)
            edges_list_add_node(self)


z = copy.deepcopy(NodeType("test", 'name'))
x = copy.deepcopy(NodeType("test1", 'name1'))
make()
