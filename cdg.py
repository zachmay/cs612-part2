from networkx import DiGraph
import subprocess
import ast

def rename_edges(edge):
    (a, b) = edge
    return ('B' + str(a), 'B' + str(b))

def get_fdt_edges(filename):
    return map(rename_edges, map(ast.literal_eval, subprocess.check_output(["./dump-dom", filename]).splitlines()[1:-1]))






