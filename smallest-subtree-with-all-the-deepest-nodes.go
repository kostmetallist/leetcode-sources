package main

import "fmt"

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

// `Node` is the most deep node whose subtree contains all the deepest nodes;
// `Distance` is a number of vertices from root to the deepest one (incl. both ends)
type DeepestInfo struct {
	Node *TreeNode
	Distance int
}


// returns DeepestInfo relative to a passed node
func diveIntoTree(node *TreeNode) DeepestInfo {
	if node == nil {
		return DeepestInfo{node, 0}
	}

	leftResult := diveIntoTree(node.Left)
	rightResult := diveIntoTree(node.Right)
	if diff := leftResult.Distance-rightResult.Distance; diff > 0 {
		return DeepestInfo{leftResult.Node, leftResult.Distance+1}
	} else if diff < 0 {
		return DeepestInfo{rightResult.Node, rightResult.Distance+1}
	}

	return DeepestInfo{node, leftResult.Distance+1}
}


func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	return diveIntoTree(root).Node
}

func main() {

	var root TreeNode
	root.Val = 3
	var l1_1 TreeNode
	l1_1.Val = 5
	root.Left = &l1_1
	var l1_2 TreeNode
	l1_2.Val = 1
	root.Right = &l1_2
	var l2_1 TreeNode
	l2_1.Val = 6
	l1_1.Left = &l2_1
	var l2_2 TreeNode
	l2_2.Val = 2
	l1_1.Right = &l2_2
	var l2_3 TreeNode
	l2_3.Val = 0
	l1_2.Left = &l2_3
	var l2_4 TreeNode
	l2_4.Val = 8
	l1_2.Right = &l2_4
	var l3_1 TreeNode
	l3_1.Val = 7
	l2_2.Left = &l3_1
	var l3_2 TreeNode
	l3_2.Val = 4
	l2_2.Right = &l3_2
	var l3_3 TreeNode
	l3_3.Val = 9
	l2_3.Left = &l3_3

	fmt.Println(subtreeWithAllDeepest(&root).Val)
}
