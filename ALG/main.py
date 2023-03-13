class Node:
    def __init__(self, name):
        self.name = name
        self.k = 0
        self.nodes = []

    def __str__(self):
        return f"{self.name} {self.k}"

    def __repr__(self) -> str:
        return repr(f"{self.name}")


class Tree:
    def __init__(self, root, nlist, keyn):
        self.root = root
        self.nlist = nlist
        self.keyn = keyn
        self.total_weight = 0

    def form_key_tree(self):
        node = self.root
        if len(node.nodes) > 0:
            for i in range(len(node.nodes)):
                x = self.rec_form_key_tree(node.nodes[i][0], node)

                if x == 0:
                    node.nodes[i] = (0, 0)

    def rec_form_key_tree(self, node, prevnode):
        # print(node)
        # print(len(node.nodes))
        x_total = 0
        if len(node.nodes) > 0:
            for i in range(len(node.nodes)):
                if node.nodes[i][0] != prevnode:
                    x = self.rec_form_key_tree(node.nodes[i][0], node)
                    x_total += x
                    if x == 0:
                        node.nodes[i] = (0, 0)
            return x_total + node.k
        else:
            return 0 + node.k

    def count_edges(self, node, prevnode):
        if len(node.nodes) > 0:
            for i in range(len(node.nodes)):
                if node.nodes[i][0] != prevnode and node.nodes[i][0] != 0:
                    self.total_weight += (node.nodes[i][1] * 2)
                    self.count_edges(node.nodes[i][0], node)
            return
        else:
            return


if __name__ == '__main__':
    n, k = map(int, input().split(' '))
    key_servers = list(map(int, input().split(' ')))
    rootkey = min(key_servers)
    nodeslist = []
    # Initializing Nodes
    for i in range(n-1):
        nodeslist.append(Node('Node'+str(i)))

    nodeslist.append(Node('Node'+str(n-1)))

    for i in range(n-1):
        edge_input = list(map(int, input().strip().split(' ')))
        # print(edge_input)
        nodeslist[edge_input[0]].nodes.append(
            (nodeslist[edge_input[1]],   edge_input[2]))
        nodeslist[edge_input[1]].nodes.append(
            (nodeslist[edge_input[0]],   edge_input[2]))

    for i in key_servers:
        nodeslist[i].k = 1

    Tree1 = Tree(nodeslist[rootkey], nodeslist, key_servers)
    Tree1.form_key_tree()
    Tree1.count_edges(Tree1.root, Tree1.root)
    print(Tree1.total_weight)

    '''
    for i in nodeslist[3].nodes:
        print(i)

    for i in nodeslist[12].nodes:
        print(i)
    
    for i in nodeslist:
        print(i)
    '''
