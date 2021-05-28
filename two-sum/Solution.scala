object Solution extends App {

    // I understood condition "You may not use the same element twice"
    // in such way: i can't mark as successfull two equal indices - that 
    // situation might be in the case of even value of <target>

    def twoSum(nums: Array[Int], target: Int): Array[Int] = { 

        val last = nums.size-1

        for (i <- 0 to last) {

            val suspect = nums(i)

            for (j <- i+1 to last) {

                if (suspect+nums(j) == target) return Array(i, j)  
            }   
        }   

        // in case of unsuccesful search
        Array(-1, -1) 
    }   
}
