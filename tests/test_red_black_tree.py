from solutions.red_black_tree import RBNode, RBTree

def test_RBTree():
    rb = RBTree()

    # Insertion
    rb.insert(30)
    assert rb.root.key == 30
    assert rb.root.color == RBNode.BLACK

    rb.insert(20)
    assert rb.root.left.key == 20
    assert rb.root.left.color == RBNode.RED

    rb.insert(10)
    assert rb.root.left.key == 10
    assert rb.root.left.left.color == RBNode.BLACK

    rb.insert(25)
    assert rb.root.right.key == 30
    assert rb.root.left.right.key == None
    assert rb.root.left.right.color == RBNode.BLACK

    # Left Rotation
    rb.insert(35)
    assert rb.root.right.key == 30
    assert rb.root.right.right.key == 35
    assert rb.root.right.right.color == RBNode.RED

    rb.insert(40)  # This should trigger a left rotation at node 30
    assert rb.root.right.key == 30
    assert rb.root.right.left.key == 25
    assert rb.root.right.right.key == 35

    # Reset the tree for right rotation test
    rb = RBTree()

    # Right Rotation
    rb.insert(30)
    rb.insert(40)
    assert rb.root.right.key == 40
    assert rb.root.right.color == RBNode.RED

    rb.insert(35)  # This should trigger a right rotation at node 30
    assert rb.root.right.key == 40
    assert rb.root.right.left.key == None
    assert rb.root.right.right.key == None
