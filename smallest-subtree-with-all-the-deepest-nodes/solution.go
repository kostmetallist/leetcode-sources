package main

// CODE FOR SUBMISSION IS PLACED BELOW //

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

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
