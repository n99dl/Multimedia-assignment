from collections import defaultdict

class TreeNode(object):
    def __init__(self):
        self.children = defaultdict()
        self.data = None

class PrefixCodeTree:
    def __init__(self):
        self.treeRoot = TreeNode()

    def insert(self, word, data):
        node = self.treeRoot
        for code in word:
            code = int(code)
            if code not in node.children:
                node.children[code] = TreeNode()
            node = node.children[code]
        node.data = data

    def decode(self, encoded_data, data_length):
        node = self.treeRoot
        bits = 0
        raw_data = []
        for i_byte in encoded_data:
            bit_lv = 7
            while bit_lv >= 0:
                bits += 1
                if bits > data_length:
                    break
                current_bit = 1 if i_byte&(1<<bit_lv)>0 else 0
                bit_lv -= 1
                if current_bit not in node.children:
                    return None
                node = node.children[current_bit]
                if node.data is not None:
                    raw_data.append(node.data)
                    node = self.treeRoot
        return ''.join(raw_data)

if __name__ == '__main__':
    codebook = {
        'x1': [0],
        'x2': [1, 0, 0],
        'x3': [1, 0, 1],
        'x4': [1, 1]
    }
    codeTree = PrefixCodeTree()
    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)
    message = codeTree.decode(b'\xd2\x9f\x20', 21)
    print(message)