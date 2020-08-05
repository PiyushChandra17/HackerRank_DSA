"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def check_loop(node, visited):
    if node.next:
        if node.next in visited:
            return True
        visited.append(node)
        return check_loop(node.next, visited)
    return False

def has_cycle(head):
    return check_loop(node=head, visited=[])