import scala.collection.mutable.Stack


object Solution extends App {

    def symmetricBrace(brace: Char): Char = { 

        if (brace == ')') return '('
        if (brace == ']') return '['
        if (brace == '}') return '{' 
        else return '0' 
    }   

    def isValid(s: String): Boolean = { 

        if (s.isEmpty) return true

        var stack = new Stack[Char]

        for (i <- 0 to (s.size-1)) {

            val elem = s(i)

            if (elem == '(' ||
                elem == '[' ||
                elem == '{')

                stack.push(elem)

            else if (elem == ')' ||
                     elem == ']' ||
                     elem == '}') {

                if (stack.isEmpty ||
                    stack.pop != symmetricBrace(elem))
                    
                    return false
            }   

            else return false
        }   

        if (stack.isEmpty) true
        else false
    }
}
