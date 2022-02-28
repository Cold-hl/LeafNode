# from py2neo import Node, Relationship, Graph
# import copy

NODELIST = {}
EDGESLIST = []


# 节点类
class NodeType:
    def __init__(self, name=None, mode='other', value=None):
        if mode == "":
            mode = 'other'
        self.name = name
        self.mode = mode
        self.value = value

        logs = "`" + self.name + "`:`" + self.mode + "`{`name`:'" + self.name + "',"
        if type(self.value) != dict:
            print("属性值异常")
        else:
            for label in value:
                logs = logs + "`" + str(label) + "`:'" + str(value[str(label)]) + "',"

        self.logs = logs[:-1] + "}"

    def add_node(self):
        """添加节点"""
        logs = "CREATE(" + self.logs + ")"
        print(logs)
        return logs

    def del_node(self):
        """删除节点"""
        logs = "MATCH (" + self.logs + ") delete `" + self.name + "`"
        print(logs)
        return logs

    def del_node_s(self):
        logs = "MATCH (" + self.logs + ")-[r]->() delete r,`" + self.name + "`"
        print(logs)
        return logs


# 边
class EdgesType:
    def __init__(self, start_node=None, value=None, end_node=None):
        self.start_node = start_node
        self.value = value
        self.end_node = end_node

        # self.logs = "(" + start_node.logs + ")-[" + value + "]->(" + over_node.logs + ")"
        logs = "(" + start_node.logs + ")-[r:`" + value + "`]->(" + end_node.logs + ")"
        self.logs = logs
        # print(self.logs)

    def add_edges(self):
        logs = "match (" + self.start_node.logs + "),(" + self.end_node.logs + ") create  "
        logs = logs + "(`" + self.start_node.name + "`)-[r:`" + self.value + "`]->(`" + self.end_node.name + "`)"
        print(logs)
        return logs

    def del_edges(self):
        logs = "match" + self.logs + " delete r "
        print(logs)
        return logs

#
# c = NodeType("test", "", {"1": 12, "2": 22, "3": 32, })
# d = NodeType("test1", "t1", {"1": 1, "2": 2, "3": 3, })
# c.add_node()
# d.add_node()
# n = EdgesType(c, "test", d)
# n.add_edges()
# n.del_edges()
# c.del_node_s()
