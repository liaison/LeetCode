import java.util.List;


/**
 *  utility function toolbox 
 *  
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 *
 */

public class Utils {

	
    public static void printListOfList(List<List<Integer>> result){
    
    	for(List<Integer> list : result){
    		System.out.print("[");
    		for(Integer i : list){
    			System.out.print(i + ",");
    		}
    		System.out.println("]");
    	}
    }
    
    
    public static void printArray(int [] array){
    	for(int i=0; i<array.length; i++){
    		System.out.print(array[i] + ",");
    	}
    	System.out.println("");
    }
    
    
    public static void printIntervalList(List<Interval> list){
    	for(Interval iter : list){
    		System.out.print("[" + iter.start + "," + iter.end + "]\t");
    	}
    	
    	System.out.println();
    }
}
