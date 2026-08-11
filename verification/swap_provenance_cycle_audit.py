"""Graph diagnostics for LEMMA-228/229 and NG-168."""


def cycle_rank(vertices, edges, components=1):
    return len(edges) - len(vertices) + components


for left_internal in range(1, 9):
    for right_internal in range(1, 9):
        vertices = {"h", "k"}
        left = [f"l{i}" for i in range(left_internal)]
        right = [f"r{i}" for i in range(right_internal)]
        vertices.update(left)
        vertices.update(right)
        left_path = ["h", *left, "k"]
        right_path = ["h", *right, "k"]
        edges = {
            tuple(sorted((path[i], path[i + 1])))
            for path in (left_path, right_path)
            for i in range(len(path) - 1)
        }
        assert cycle_rank(vertices, edges) == 1
        # Contracting any internal path vertex removes one edge and one vertex.
        contracted_v = len(vertices) - (left_internal + right_internal)
        contracted_e = len(edges) - (left_internal + right_internal)
        assert contracted_e - contracted_v + 1 == 1


tree_vertices = {"hp", "hq", "p", "q", "k"}
tree_edges = {("hp", "p"), ("p", "k"), ("hq", "q"), ("q", "k")}
assert cycle_rank(tree_vertices, tree_edges) == 0

print(
    "swap-provenance cycle audit passed: 64 common-origin path pairs rank one "
    "under contraction; distinct-origin tree rank zero"
)
