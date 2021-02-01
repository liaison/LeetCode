import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.NoSuchElementException;


/**
 *  Java Iterator interface reference:
 *  https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
 * @author Lisong
 */
public class PeekingIterator implements Iterator<Integer> {
	
	private Iterator<Integer> _iter;
	private Integer _nextValue;
	
	public PeekingIterator(Iterator<Integer> iterator) {
		_iter = iterator;
		
	    try {
	    	_nextValue = _iter.next();	
	    } catch (NoSuchElementException e) {
	    	_nextValue = null;
	    }   
	}

    /**
     *  Returns the next element in the iteration without advancing the iterator.
     */
	public Integer peek() {
        return _nextValue;
	}

	/**
	 *  hasNext() and next() should behave the same as in the Iterator interface.
	 */
	@Override
	public Integer next() {
		if(_nextValue == null)
			throw new NoSuchElementException();

	    Integer ret = _nextValue;
	    try {
	    	_nextValue = _iter.next();	
	    } catch (NoSuchElementException e) {
	    	_nextValue = null;
	    }   
	    return ret;
	}


	@Override
	public boolean hasNext() {
		return (_nextValue != null);
	}

	
	@Override
	public void remove() {
		// TODO Auto-generated method stub	
	}


	public static void main(String[] args) {
		
		ArrayList<Integer> list = new ArrayList<Integer>();
		
		for(int i=1; i<=3; ++i) {
			list.add(i);
		}
		
		Iterator<Integer> iter = list.iterator();
		PeekingIterator pk = new PeekingIterator(iter);
		
		assertTrue(pk.peek() == 1);

		assertTrue(pk.next() == 1);

		assertTrue(pk.peek() == 2);

		assertTrue(pk.next() == 2);

		assertTrue(pk.hasNext());
		assertTrue(pk.next() == 3);

		assertFalse(pk.hasNext());
	}

}

