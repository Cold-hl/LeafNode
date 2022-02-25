from py2neo import Node, Relationship, Graph

# 可以通过Node或Relationship对象创建
a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
r = Relationship(a, 'KNOWS', b)
print(a, b, r)
# Node和Relationship都继承了PropertyDict类，它可以赋值很多属性，类似于字典的形式
a['age'] = 20
b['age'] = 21
r['time'] = '2017/08/31'
print(a, b, r)
# 使用setdefault()可设置默认属性
a.setdefault('location', '北京')
print(a)
data = {'name': 'Amy', 'age': 21}
a.update(data)
print(a)

del a
del b
del r

# Subgraph，子图，是Node和Relationship的集合，最简单的构造子图的方式是通过关系运算符，实例如下
a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
r = Relationship(a, 'KNOWS', b)
a['age'] = 20
b['age'] = 21
print(a, b, r)
s = a | b | r
print(s)

a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
c = Node('Person', name='Mike')
ab = Relationship(a, 'KNOWS', b)
ac = Relationship(a, 'KNOWS', c)
w = ab + Relationship(b, 'LIKES', c) + ac
print(w)
# graph_1 = Graph()
# graph_2 = Graph(host="localhost")
# graph_3 = Graph("http://localhost:7474/db/data/")
graph = Graph("http://neo4j:123456@127.0.0.1:7474/")
graph.create(w)


def deleteNode(thisNodeID):
    graph.run("MATCH (n) where id(n) = $nodeID DETACH DELETE n",
              parameters={"nodeID": thisNodeID})

