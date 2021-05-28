object Solution {
    def removeElement(nums: Array[Int], value: Int): Int = {

        var finalLength = 0

        for (i <- nums.indices) {

            if (nums(i) != value) {

                nums(finalLength) = nums(i)
                finalLength += 1
            }
        }

        finalLength
    }
}
