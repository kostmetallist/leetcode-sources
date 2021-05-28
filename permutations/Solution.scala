object Solution extends App {

    def permute(nums: Array[Int]): List[List[Int]] = {

        if (nums.length == 1)
            return List[List[Int]](List(nums(0)))

        var output: List[List[Int]] = List[List[Int]]()

        for (prev <- permute(nums.tail)) {
            for (i <- (prev.indices :+ prev.length)) {

                val separated = prev.splitAt(i)
                output :+= separated._1 ++ List(nums.head) ++ separated._2
            }
        }

        output
    }
}
