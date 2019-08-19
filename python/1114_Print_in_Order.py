"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and 
thread C will call third(). 
Design a mechanism and modify the program to ensure that second() 
 is executed after first(), and third() is executed after second().

"""

from threading import Event

class Foo:
    def __init__(self):
        self.firstJobDone = Event()
        self.secondJobDone = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        # Notify the thread that is waiting for this event.
        self.firstJobDone.set()
        

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # Wait for the first job to be done
        self.firstJobDone.wait()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        # Notify the thread that is waiting for the second job.
        self.secondJobDone.set()
        
        # for the next batch of events ? 
        #self.firstJobDone.clear()


    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        self.secondJobDone.wait()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
        #self.secondJobDone.clear()