package main

import "fmt"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
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
