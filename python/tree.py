# 시간복잡도 : O(n)
from collections import deque

def levelOrder(root):
	visited = []
	if root is None:
		return 0
	q = deque()
	q.append(root)
	while q:
		cur_node = q.popleft()
		visited.append(cur_node.value)

		if cur_node.left:
			q.append(cur_node.left)
		if cur_node.right:
			q.append(cur_node.right)
	return visited

def traversal(root):
	if root is None:
		return 0
	traversal(root.left)
	traversal(root.right)

def preorder(root):
	if root is None:
		return
	print(root)
	preorder(root.left)
	preorder(root.right)

def inorder(root):
	if root is None:
		inorder(root.left)
		print(root)
		inorder(root.right)

def postorder(root):
	if root is None:
		return
	postorder(root.left)
	postorder(root.right)
	print(root)