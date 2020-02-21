package main

// Given a binary tree rooted at root, the depth of each node is the shortest 
// distance to the root. A node is deepest if it has the largest depth possible
// among any node in the entire tree. The subtree of a node is that node, 
// plus the set of all descendants of that node. Return the node with the 
// largest depth such that it contains all the deepest nodes in its subtree.

// The number of nodes in the tree will be between 1 and 500.
// The values of each node are unique.


type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	return root
}

func main() {

	var root TreeNode
}