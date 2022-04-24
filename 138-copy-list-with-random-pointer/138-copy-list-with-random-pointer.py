class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None
        
        # Kind of like a graph bfs problem, so we need to track the next nodes to visit and copy.
        next_nodes_to_copy = [head]
        
        # Need a dictionary of { original_node: copied_node } of each node created
        copied_map = { head: Node(head.val) }
        
        # Iteratively visit nodes to copy
        while next_nodes_to_copy:
            node = next_nodes_to_copy.pop(0)
            copied_node = copied_map[node]

            # Next and random are essentially the same, just pointers to other nodes
            if node.next:
                copied_node.next = self.copy_next_node(next_nodes_to_copy, copied_map, node.next)
            if node.random:
                copied_node.random = self.copy_next_node(next_nodes_to_copy, copied_map, node.random)
    
        return copied_map[head]


    def copy_next_node(self, next_nodes_to_copy, copied_map, next_node):
        # Create new node and visit next to fill in the node.next and node.random info.
        if next_node not in copied_map:
            copied_map[next_node] = Node(next_node.val)
            next_nodes_to_copy.append(next_node)

        return copied_map[next_node]