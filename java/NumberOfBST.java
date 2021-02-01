
public class NumberOfBST {
    public int numTrees(int n) {
        long C = 1;
        for(int i=0; i<n; ++i){
            C = C * 2*(2*i+1)/(i+2);  
        }
        return (int) C;
    }

	public static void main(String[] args) {
		NumberOfBST catalan = new NumberOfBST();
		
		System.out.print(catalan.numTrees(19));
	}
}

