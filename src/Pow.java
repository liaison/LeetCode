
/**
 * 
 * Power operator 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 04, 2015
 *
 */
public class Pow {

    public double pow(double x, int n) {
        boolean isNeg = false;
        
    	if(n == 0){
        	return 1;
        }else if(n == 1 || x == 0){
        	return x;
        }else if(n < 0){
        	isNeg = true;
        	n = -n;
        }
        
        double res = 1.0;
    	if(n % 2 == 1){
    		res = x;
    	}
    	
    	double half = pow(x, n/2);
    	res = res * half * half;
    	
    	if(isNeg){
    		return 1/res;
    	}else{
    		return res;
    	}
    }
	
	public static void main(String[] args) {
		Pow solution = new Pow();
		
		System.out.println(solution.pow(0, -1));
	}

}
