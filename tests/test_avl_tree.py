from questions.avl_tree import AVLTree

import time
import random

def test_AVLTree():
    avl = AVLTree()
    avl.insert(30)
    avl.insert(20)
    avl.insert(10)
    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30

    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    assert avl.root.key == 20
    assert avl.root.left.key == 10
    assert avl.root.right.key == 30

    avl = AVLTree()
    avl.insert(30)
    avl.insert(40)
    avl.insert(35)
    assert avl.root.key == 35
    assert avl.root.left.key == 30
    assert avl.root.right.key == 40

    avl = AVLTree()
    avl.insert(20)
    avl.insert(10)
    avl.insert(15)
    assert avl.root.key == 15
    assert avl.root.left.key == 10
    assert avl.root.right.key == 20

    avl = AVLTree()
    for i in range(1, 10001):
        avl.insert(i)
    assert avl.root.height < 20

    avl = AVLTree()
    numbers = list(range(1, 10001))
    random.shuffle(numbers)
    start_time = time.time()
    for num in numbers:
        avl.insert(num)
    elapsed_time = time.time() - start_time
    print(f"Time taken for 10,000 random insertions: {elapsed_time:.2f} seconds")
    assert avl.root.height < 20

    random.shuffle(numbers)
    start_time = time.time()
    for num in numbers:
        avl.delete(num)
    elapsed_time = time.time() - start_time
    print(f"Time taken for 10,000 random deletions: {elapsed_time:.2f} seconds")
    assert avl.root is None

    avl = AVLTree()
    numbers = list(range(1, 10001))
    random.shuffle(numbers)
    start_time = time.time()
    for num in numbers:
        avl.insert(num)
        avl.delete(num)
    elapsed_time = time.time() - start_time
    print(f"Time taken for 10,000 random insertions followed by immediate deletions: {elapsed_time:.2f} seconds")
    assert avl.root is None

    avl = AVLTree()
    numbers_desc = list(range(10000, 0, -1))
    numbers_asc = list(range(1, 10001))
    start_time = time.time()
    for num in numbers_desc:
        avl.insert(num)
    for num in numbers_asc:
        avl.delete(num)
    elapsed_time = time.time() - start_time
    print(f"Time taken for 10,000 descending order insertions followed by ascending order deletions: {elapsed_time:.2f} seconds")
    assert avl.root is None
