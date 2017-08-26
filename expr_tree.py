class ExpressionTree(object):
  
    def __init__(self, expr_string=[]):
        expr_string = expr_string.replace(' ', '')
        self.expr_tree = self.parse(expr_string)

    def deep_len(self, lst):
        return sum(self.deep_len(el) + 2 if isinstance(el, list) else 1 for el in lst)
    
    def parse(self, expr_string):
        expr_tree = []
        i = 0
        while i < len(expr_string):
            char = expr_string[i]
            if char.isalpha():
                expr_tree.append(char)
                i += 1
            elif char == '(':
                sub_expr = self.parse(expr_string[i + 1:])
                expr_tree.append(sub_expr)
                i += self.deep_len(sub_expr) + 2
            elif char == ')':
                return expr_tree
        return expr_tree

    def to_string(expr_tree):
        expr_tree_str = ''
        for el in expr_tree:
            if isinstance(el, list):
                expr_tree_str += '(' + ExpressionTree.to_string(el) + ')'
            else:
                expr_tree_str += el
        return expr_tree_str
    
    def __repr__(self):
        return ExpressionTree.to_string(self.expr_tree)

    def apply(self, operation):
        if operation == 'S':
            self.expr_tree = simplify(self.expr_tree)
        elif operation == 'R':
            self.expr_tree = reverse(self.expr_tree)

def simplify(expr_tree):
    if len(expr_tree) < 1:
        return
    for i, el in enumerate(expr_tree):
        if isinstance(el, list):
            expr_tree[i] = simplify(el)
    if not isinstance(expr_tree[0], list):
        new_expr_tree = expr_tree
    else:
        new_expr_tree = expr_tree[0] + expr_tree[1:]
    return new_expr_tree

def reverse(expr_tree):
    expr_tree.reverse()
    for el in expr_tree:
        if isinstance(el, list):
            reverse(el)
    return expr_tree

if __name__ == "__main__":
    t = ExpressionTree("A B (C D (E) (FG) )")
    # print(t)

    t = ExpressionTree("A B (C D (E F))")
    # print(t)

    t = ExpressionTree("(AB) C ((DE) F)")
    print(t.expr_tree)

    t.apply('S')
    print(t.expr_tree)

    t.apply('R')
    print(t.expr_tree)
