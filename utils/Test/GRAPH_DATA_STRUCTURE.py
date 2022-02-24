# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：胡子涵
# 开发时间：2022/1/13 10:43
# 文件名称：GRAPH_DATA_STRUCTURE
# 开发工具：PyCharm
import copy

# import requests, json, time
from py2neo import Graph


# 节点结构
class Graph_Node:
    node_id = None  # id
    node_label = None  # 标题
    node_class = None  # 类型
    node_data = None  # 内容

    def __init__(self, node_id=None, node_label=None, node_class=None, node_data=None):
        self.node_id = node_id
        self.node_label = node_label
        self.node_class = node_class
        self.node_data = node_data

    def check_data(self):
        return [self.node_id, self.node_label, self.node_class, self.node_data]


# 边结构
class Graph_Edges:
    edges_source = None  # 来源
    edges_target = None  # 目标
    edges_label = None  # 内容
    edges_type = None  # 类型（如：自环）

    def __init__(self, edges_source=None, edges_target=None, edges_label=None, edges_type=None):
        self.edges_source = edges_source  # 来源
        self.edges_target = edges_target  # 目标
        self.edges_label = edges_label  # 内容
        self.edges_type = edges_type  # 类型（如：自环）


# 构建图类型
class Graph_List:
    def __init__(self, Node=None, Edges=None, Next=None):
        self.Node = []  # 节点内容
        self.Edges = []  # 节点边内容
        self.Next = Next  # 次节点


# # 元素信息抽取
# def extract_data_node(all_data):
#     node_id = ""
#     node_N = ""
#     node_D = ""
#     extract_type = 0
#     for x in all_data:
#         if x == ":" and extract_type == 0:
#             node_id = int(node_id)
#             extract_type = 1
#         elif x == "{" and extract_type == 1:
#             node_D = node_D + x + '"'
#             extract_type = 2
#         elif extract_type == 2:
#             node_D = node_D + x
#         elif extract_type == 1:
#             node_N = node_N + x
#         elif extract_type == 0:
#             node_id = str(node_id) + str(x)
#     print(node_D.replace(":", '":').replace(", ", ', "'))
#
#     node_D = json.loads(node_D.replace(":", '":').replace(", ", ', "'))
#     # print(node_id, node_N, node_D)
#     return node_id, node_N, node_D

# for i in nodes_data:
#     print(i['a'],i['b'],i['x'])
#     str(i['a'])
def extract_data_node(all_data):
    node_id = str(all_data.identity)
    node_D = {}
    # print(len(all_data))
    for i in all_data:
        node_D[i] = all_data[i].replace("\"", "`")

    node_N = all_data["名称"].replace("\"", "`")

    return node_id, node_N, node_D


# 边信息抽取
def extract_data_edges(all_data):
    edges_source = ""
    edges_target = ""
    edges_label = ""
    extract_type = 0
    for x in all_data:
        if x == ")" and extract_type == 0:
            edges_source = int(edges_source)
            extract_type = 1
        elif x == ":" and extract_type == 1:
            extract_type = 2
        elif x == "{" and extract_type == 2:
            pass
        elif x == "(" and extract_type == 2:
            extract_type = 3
        elif x == "_" and extract_type == 3:
            extract_type = 4
        elif x == ")" and extract_type == 4:
            extract_type = 5
        elif extract_type == 4:
            edges_target = edges_target + x
        elif extract_type == 3:
            extract_type = 2
        elif extract_type == 2:
            edges_label = edges_label + x
        elif extract_type == 1:
            pass
        elif extract_type == 0:
            edges_source = str(edges_source) + str(x)

    if str(edges_target) == str(edges_source):
        edges_type = "loop"
    else:
        edges_type = ""
        # curveOffset: -80
    # node_D = json.loads(node_D.replace(":", '":').replace(", ", ', "'))
    return str(edges_source), str(edges_target), edges_label[:-5], edges_type
    # return node_id, node_N, node_D


def Make_Graph(data_name, data=None):
    # graph = Graph("http://127.0.0.1:7474/", username="neo4j", password="123456")
    # graph = Graph("http://127.0.0.1:7474/", auth=("neo4j", "123456"))

    graph = Graph("http://neo4j:123456@127.0.0.1:7474/")
    check_all = "MATCH (a{名称:'" + data_name + "'})-[x]->(b) RETURN * LIMIT 25"
    print(check_all)
    # 构建图类型对象，存储获取的neo4j数据
    # data = Graph_List()

    # 提取数据
    nodes_data = graph.run(check_all).data()
    # print(nodes_data)
    # nodes_data = reversed(nodes_data)

    if data is None:
        # 构建图类型对象，存储获取的neo4j数据
        data = Graph_List()
        node_id, node_N, node_D = extract_data_node(nodes_data[1]['a'])
        data.Node.append(Graph_Node(node_id, node_N, 0, node_D))
        nodes_date_long = len(nodes_data) - 1
    else:
        nodes_date_long = len(nodes_data) - 2

    for i in range(nodes_date_long, -1, -1):
        # test = str([i]['b'])[2:-1].replace("'", '"')
        # print(nodes_data[i])
        node_id, node_N, node_D = extract_data_node(nodes_data[i]['b'])
        data.Node.append(Graph_Node(node_id, node_N, 0, node_D))
        test = str(nodes_data[i]['x'])[2:-1]
        edges_source, edges_target, edges_label, edges_type = extract_data_edges(test)
        data.Edges.append(Graph_Edges(edges_source, edges_target, edges_label, edges_type))
        # data.Edges.append(Graph_Edges(node_id, node_N, 0, node_D))
    return data


def Loop_Make_Graph(data_name):
    data = Make_Graph(data_name)
    data_loop = copy.deepcopy(data)
    print(id(data_loop), id(data))
    first = 1
    x = 0
    for i in data.Node:
        if first == 1:
            first = 0
            continue
        else:
            x += 1
            time.sleep(1)
            data_loop = Make_Graph(str(i.node_data["名称"]), data_loop)
    return data_loop


def Make_json(data):
    # 组合json
    make_json = '{"nodes":['
    for i in data.Node:
        # make_json = make_json + '{"id":"' + str(i.node_id) + '","label":"' + str(i.node_label) + '","class":"' + str(
        make_json = make_json + '{"id":"' + str(i.node_id) + '","label":"' + str(
            i.node_data['名称']) + '","class":"' + str(
            i.node_class) + '","data":' + str(i.node_data).replace("'", '"') + '},'
    make_json = make_json[:-1] + '],"edges": ['

    for i in data.Edges:
        if i.edges_type:
            make_json = make_json + '{"source":"' + str(i.edges_source) + '","target":"' + str(
                i.edges_target) + '","label":"' + str(
                i.edges_label) + '","type":"' + str(i.edges_type) + '"},'
        else:
            make_json = make_json + '{"source":"' + str(i.edges_source) + '","target":"' + str(
                i.edges_target) + '","label":"' + str(
                i.edges_label) + '"},'
    make_json = make_json[:-1] + ']}'
    print(make_json)


if __name__ == '__main__':
    # Make_Graph("苏/俄")
    Make_json(Loop_Make_Graph("“西北风”(Mistral)级两栖攻击舰／多用途两柄舰"))
