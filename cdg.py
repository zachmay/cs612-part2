import networkx as nx

edges = \
    [ ("B1", "B0")
    , ("B2", "B1")
    , ("B3", "B1")
    , ("B4", "B3")
    , ("B4", "B2")
    , ("B5", "B4")
    , ("B5", "B2")
    , ("B6", "B1")
    , ("B7", "B6")
    , ("B7", "B5")
    , ("B8", "B7")
    , ("B8", "B5")
    , ("B9", "B1")
    , ("B10", "B9")
    , ("B10", "B8")
    , ("B11", "B10")
    , ("B11", "B8")
    , ("B12", "B1")
    , ("B13", "B12")
    , ("B13", "B11")
    , ("B14", "B1")
    , ("B15", "B1")
    , ("B16", "B15")
    , ("B16", "B14")
    , ("B17", "B15")
    , ("B17", "B16")
    , ("B18", "B15")
    , ("B18", "B17")
    , ("B19", "B18")
    , ("B19", "B13")
    , ("B20", "B19")
    , ("B21", "B20")
    , ("B21", "B19")
    , ("B22", "B21")
    , ("B23", "B22")
    , ("B23", "B21")
    , ("B24", "B23")
    , ("B25", "B24")
    , ("B25", "B23")
    , ("B26", "B1")
    , ("B27", "B26")
    , ("B27", "B25")
    , ("B28", "B26")
    , ("B28", "B27")
    , ("B29", "B26")
    , ("B29", "B28")
    ]

# edges = \
#     [ (0, 1)
#     , (1, 2)
#     , (2, 3)
#     , (2, 4)
#     , (3, 5)
#     , (4, 5)
#     , (5, 6)
#     ]

entry = "B0" # The exit node, but it's the entry of the inverted CFG.

def dependencies(g, entry):
    dominators = nx.immediate_dominators(inv_cfg, entry)
    deps = []
    for n in inv_cfg.nodes():
        for m in inv_cfg.nodes():
            ifdom = dominators[m]
            if any([ifdom not in path for path in nx.all_simple_paths(inv_cfg, n, m)]):
                deps.append((m, n))

    return deps

def transitive_reduction(g):
    result = g.copy()
    for x in result.nodes():
        for y in result.nodes():
            for z in result.nodes():
                if (x, y) in result.edges() and (y, z) in result.edges() and (x, z) != (x, y) and (x, z) != (y, z):
                    result.remove_edge(x, y)
    return result

inv_cfg = nx.DiGraph(map(lambda (x,y): (y,x), edges))
deps = dependencies(inv_cfg, entry)
cdg = nx.DiGraph(deps)

nx.drawing.nx_pydot.write_dot(cdg, 'tritype.dot')
