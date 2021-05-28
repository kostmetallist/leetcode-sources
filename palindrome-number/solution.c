bool isPalindrome(int x) {

    int rev_half = 0;

    if (x < 0) return false;

    if ((x % 10 == 0) && (x != 0)) return false;

    while (x > rev_half) {   
        rev_half = x%10 + rev_half*10;
        x /= 10; 
    }   

    if ((rev_half == x) || (rev_half/10 == x)) return true;
    else return false;
}
