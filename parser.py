import json

class Parser:

    def atomize(self, tokens):
        atoms = []

        for token in tokens:
            try:
                atoms.append(int(token))
            except ValueError:
                try:
                    atoms.append(float(token))
                except ValueError:
                    atoms.append(token)
                
        return atoms


    def build_ast(self, tokens):
        tree = Node([])
        current_node = tree

        for token in tokens:
            if token == "(":
                    new_node = Node([])
                    current_node.data.append(new_node)
                    new_node.parent = current_node
                    current_node = new_node
            elif token == ")":
                current_node = current_node.parent
            else:
                current_node.data.append(token)

        return self.__unwrap_node(tree)[0]


    def __unwrap_node(self, node):
        unwrapped = []

        for token in node.data:
            if isinstance(token, Node):
                unwrapped.append(self.__unwrap_node(token))
            else:
                unwrapped.append(token)

        return unwrapped


class Node:

    def __init__(self, data):
        self.data = data
        self.parent = None
