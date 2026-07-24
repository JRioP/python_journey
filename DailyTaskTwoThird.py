class ListOfTrees:
    def __init__(self):
        self.trees = []

    def add_tree(self, tree):
        self.trees.append(tree)

    def check_duplicates(self):
        unique_trees = []

        for tree in self.trees:
            if tree not in unique_trees:
                unique_trees.append(tree)
                count = self.trees.count(tree)
                if count > 1:
                    number_of_duplicates = count - 1
                print(f"Duplicate Found: {tree} (appears {number_of_duplicates} times)")

        self.trees = unique_trees

    def sort_tree_list(self):
        self.trees.sort()

lt = ListOfTrees()
lt.add_tree("Oak")
lt.add_tree("pine")
lt.add_tree("Oak")
lt.add_tree("Oak")
lt.add_tree("Oak")
lt.add_tree("pine")

lt.check_duplicates()
lt.sort_tree_list()
print(f"Final list: {lt.trees}")