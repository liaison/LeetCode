import static org.junit.Assert.*;

import org.junit.Test;



/**
 *
 * All the problems that involve bit operations.
 *
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 09, 2014
 *
 */
public class BitOps {


        public double pow(double x, int n) {
                if(n == 0){
                        return 1;
                }else if(x == 0 || n == 1){
                        return x;
                }else{
                        if(n < 0){
                                return 1 / pow_rec(x, -n);
                        }else{
                                return pow_rec(x, n);
                        }
                }
        }

        private double pow_rec(double x, int n) {
                double res = 1;
                while(n > 0){
                        if((n & 1) == 1){
                                res *= x;
                        }
                        x *= x;
                        n >>= 1;
                }

                return res;
        }

        /**
         * Implement int sqrt(int x) i.e compute and return the square root of x.
         *
         * This solution would exceed the time limit.
         */
        public int sqrt(int x) {
            int mid = 0;
            int low = 0, high = x;

            while(low < high - 1){
                mid = (low + high) >> 1;
                int mid_power = mid * mid;
                if(mid_power < x){
                    low = mid;
                }else if(mid_power > x){
                    high = mid;
                }else{
                    return mid;
                }
            }
            // approximation
            return low;
        }

        /**
         * The time complexity of this solution is O(1),
         *   i.e. 15 times of iteration.
         * https://oj.leetcode.com/discuss/8897/share-my-o-log-n-solution-using-bit-manipulation
         */
        public int bsqrt(int x){
            long ans = 0;         // long is necessary, due to overflow of ans * ans
            long bit = 1l << 16;  // 1L: one in long.

            // Deduce the bits of result one by one.
            while(bit > 0){
                // OR operator, set the specific bit to one and keep the rest.
                ans |= bit;
                if(ans * ans > x){
                    // XOR operator, revert the current bit from 1 to 0,
                    //   and preserve the high bits in the result.
                    ans ^= bit;
                }
                bit >>= 1;
            }

            return (int)ans;
        }

        @Test
        public void testBSqurt() {
            BitOps bto = new BitOps();
            assertEquals(bto.bsqrt(4), 2);
        }

        /**
         * Given two binary strings, return their sum (also a binary string).

        For example,
                a = "11"
                b = "1"
                Return "100".

         */
    public String addBinary(String a, String b) {
        int s_a = a.length();
        int s_b = b.length();

        int size = Math.max(s_a, s_b);
        int diff = Math.abs(s_a - s_b);

        int carry = 0;
        StringBuffer res = new StringBuffer();


        for(int i=size-1; i>=0; i--){
            int cal = 0;

            if( s_a > s_b ){
                cal = a.charAt(i) - '0';
                if(i-diff >= 0){
                    cal = cal + (b.charAt(i-diff) - '0');
                }
            } else {
                cal = b.charAt(i) - '0';
                if(i-diff >= 0){
                        cal = cal + (a.charAt(i-diff) - '0');
                }
            }

            cal = cal + carry;

            res.append(cal % 2);
            carry = cal / 2;
        }

        if(carry == 1)
            res.append("1");

        return res.reverse().toString();
    }

    @Test
    public void testAddBinary() {
        BitOps bto = new BitOps();
        assertEquals(bto.addBinary("11", "1"), "100");
    }

    /**
     * @param args
     */
    public static void main(String[] args) {
        
        int x = 8;
        BitOps solution = new BitOps();

        long startTime = System.currentTimeMillis();

        System.out.println(solution.bsqrt(x));

        long endTime = System.currentTimeMillis();
        long elapsedTime = endTime - startTime;

        System.out.println("Time: " + elapsedTime);


        String a = "11";
        String b = "110001";
        //String a = "1010";
        //String b = "1011";

        System.out.println(solution.addBinary(a, b));


        System.out.println(solution.pow(2, -3));

    }

}




