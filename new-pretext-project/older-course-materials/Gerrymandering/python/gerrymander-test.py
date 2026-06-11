from gerrychain import Graph, Partition
from gerrychain.updaters import Tally, cut_edges


# Load the graph in from the provided json file
graph = Graph.from_json("./PA_VTDs.json")

# Set up the initial partition object
initial_partition = Partition(
    graph,
    assignment="2011_PLA_1",
    updaters={
        "population": Tally("TOT_POP", alias="population"),
        "cut_edges": cut_edges,
    }
)
