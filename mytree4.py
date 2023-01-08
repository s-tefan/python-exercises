class MyTree4:
    _add_method = {
        list: list.append,
        set: set.add,
        dict: lambda s, x: dict.update(s, {x[0]: x[1]}),  # x = (key, value)
    }
    _update_method = {list: list.__iadd__, set: set.update, dict: dict.update}

    def __init__(self, data=None, children_struct=list):
        self.data = data
        self.children = children_struct()

    def set_children(self, children):
        self.children = children

    def add_child(self, child):
        self._add_method[type(self.children)](self.children, child)

    def update_children(self, children):
        self._update_method[type(self.children)](self.children, children)

    def depth_first(self):
        yield self
        children = (
            self.children.values() if isinstance(self.children, dict) else self.children
        )
        for c in children:
            for k in c.depth_first():
                yield k

    def not_breadth_first(self, suppress=False):
        if not suppress:
            yield self
        for c in self.children:
            yield c
        for c in self.children:
            for k in c.mixed_breadth_first(suppress=True):
                yield k

    def breadth_first(self):
        q = [self]
        while q:
            a = q.pop(0)
            q += list(
                a.children.values() if isinstance(a.children, dict) else a.children
            )
            yield a

    def encoding_dict(self):
        q = [self]
        enc = {self.data: []}
        while q:
            a = q.pop(0)
            print(a)
            q += list(a.children.values())
            for key, c in a.children.items():
                enc[c.data] = enc[a.data] + [key]
        return enc

    def update_parents(self, parent=None):
        self.parent = parent
        q = [self]
        while q:
            a = q.pop(0)
            for c in a.children:
                c.parent = a
            q += list(a.children)

    def decode_word(self, word):
        node = self
        for k in word:
            if node.children:
                node = node.children[k]
            else:
                raise Exception("Non-existing code")
        return node.data

    def decode_stream(self, stream):
        """generator: yields data from leaf only"""
        node = self
        for k in stream:
            if node.children:
                node = node.children[k]
            else:
                yield node.data
                node = self.children[k]

    def decode_stream2(self, word):
        """generator: yields data when non-existing key occurs"""
        node = self
        for k in word:
            if node.children:
                if k in node.children.keys():
                    node = node.children[k]
                else:
                    yield node.data
                    node = self
            else:
                yield node.data
                node = self
                # raise Exception('Non-existing code')
        yield node.data


a = MyTree4("A")
b = MyTree4("B")
a.add_child(b)
c = MyTree4("C")
a.add_child(c)
d = MyTree4("D")
e = MyTree4("E")
b.add_child(d)
c.add_child(e)
f = MyTree4("F")
d.add_child(f)

a.update_parents()

for k in [a, b, c, d, e, f]:
    print(k, k.data, k.children, k.parent)

for k in a.depth_first():
    print(k.data)
for k in a.breadth_first():
    print(k.data)


morse = MyTree4()
# 1
morse.set_children({".": MyTree4("E"), "_": MyTree4("T")})
# 2
morse.children["."].set_children({".": MyTree4("I"), "_": MyTree4("A")})
morse.children["_"].set_children({".": MyTree4("N"), "_": MyTree4("M")})
# 3
morse.children["."].children["."].set_children({".": MyTree4("S"), "_": MyTree4("U")})
morse.children["."].children["_"].set_children({".": MyTree4("R"), "_": MyTree4("W")})
morse.children["_"].children["."].set_children({".": MyTree4("D"), "_": MyTree4("K")})
morse.children["_"].children["_"].set_children({".": MyTree4("G"), "_": MyTree4("O")})
# 4
morse.children["."].children["."].children["."].set_children(
    {".": MyTree4("H"), "_": MyTree4("V")}
)
morse.children["."].children["."].children["_"].set_children(
    {".": MyTree4("F"), "_": MyTree4("Û")}
)
morse.children["."].children["_"].children["."].set_children(
    {".": MyTree4("L"), "_": MyTree4("Ä")}
)
morse.children["."].children["_"].children["_"].set_children(
    {".": MyTree4("P"), "_": MyTree4("J")}
)
morse.children["_"].children["."].children["."].set_children(
    {".": MyTree4("B"), "_": MyTree4("X")}
)
morse.children["_"].children["."].children["_"].set_children(
    {".": MyTree4("C"), "_": MyTree4("Y")}
)
morse.children["_"].children["_"].children["."].set_children(
    {".": MyTree4("Z"), "_": MyTree4("Q")}
)
morse.children["_"].children["_"].children["_"].set_children(
    {".": MyTree4("Ö"), "_": MyTree4("Ch")}
)
# TBC

# Fix leaves that have the default empty list as children
for k in morse.depth_first():
    if k.children == []:
        k.children = {}

"""
morse_s = MyTree4
node = morse_s
for k in morse.depth_first():
    new_node = MyTree4()
    for c in k.children:
        new_node.
"""


for k in (".", "_", "..", "._", "_.", "__", "...", "___."):
    print(k, morse.decode_word(k))


for k in morse.decode_stream("._...___.___.____...__"):
    print(k)

for k in morse.decode_stream2("... ___ ...  ... ___ ...    "):
    print(k)

d = morse.encoding_dict()
print(d)
print({a: "".join(b) for a, b in d.items()})


text = "THE QUICK BROWN FOX"
mo = " ".join("".join(d[c]) if c in d else c for c in text)
dec_text = morse.decode_stream2(mo)
print(text)
print(mo)
print("".join(k if k else " " for k in dec_text))
