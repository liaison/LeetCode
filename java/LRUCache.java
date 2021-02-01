import java.util.Hashtable;

/**
 * 
 * Design and implement a data structure for Least Recently Used (LRU) cache.
 *  It should support the following operations: get and set.
 * 
 * get(key) - Get the value (will always be positive) of the key if the key
 * exists in the cache, otherwise return -1.
 * 
 * set(key, value) - Set or insert the value if the key is not already present.
 * When the cache reached its capacity, it should invalidate the least recently
 * used item before inserting a new item.
 * 
 * More importantly, the complexity of both operations should be constant O(1).
 *
 * To achieve the goals, one idea is to keep a hashtable which points to a 
 *  double-linked list.
 *
 * @author Lisong Guo <lisong.guo@me.com>
 * @date Jan 01, 2015
 */
public class LRUCache {

        /**
         * A double-linked list that keeps all the values.
         */
        class DLinkedNode {
            int key;
            int value;
            DLinkedNode pre;
            DLinkedNode post;
        }

        /**
         * Always add the new node right after head;
         */
        private void addNode(DLinkedNode node) {
            node.pre = head;
            node.post = head.post;

            head.post.pre = node;
            head.post = node;
        }

        /**
         * Remove an existing node from the linked list.
         */
        private void removeNode(DLinkedNode node) {
            DLinkedNode pre = node.pre;
            DLinkedNode post = node.post;

            pre.post = post;
            post.pre = pre;
        }

        /**
         * Move certain node in between to the head.
         */
        private void moveToHead(DLinkedNode node) {
            this.removeNode(node);
            this.addNode(node);
        }

        /**
         * pop the current tail.
         */
        private DLinkedNode popTail() {
            DLinkedNode res = tail.pre;
            this.removeNode(res);
            return res;
        }

        private Hashtable<Integer, DLinkedNode> cache =
            new Hashtable<Integer, DLinkedNode>();

        //! The current number of items maintained by this cache.
        private int count;

        //! The maximum number of items that this cache would keep.
        private int capacity;

        //! The head and tail pointer of the double-linked list,
        //   which facilitate the update and purge of elements.
        private DLinkedNode head, tail;

        public LRUCache(int capacity) {
            this.count = 0;
            this.capacity = capacity;

            head = new DLinkedNode();
            head.pre = null;

            tail = new DLinkedNode();
            tail.post = null;

            head.post = tail;
            tail.pre = head;
        }

        /**
         * Retrieve an element from the cache in O(1) complexity.
         */
        public int get(int key) {

            DLinkedNode node = cache.get(key);
            if (node == null) {
                // should raise exception here.
                return -1;
            }
            // move the accessed node to the head;
            this.moveToHead(node);
            return node.value;
        }

        /**
         * Add or refresh the element in the cache.
         * As long as the element got updated from time to time,
         *  it would stay in the cache without being purged out.
         */
        public void set(int key, int value) {
            DLinkedNode node = cache.get(key);

            // Add the new element into the cache.
            if (node == null) {
                DLinkedNode newNode = new DLinkedNode();
                newNode.key = key;
                newNode.value = value;

                this.cache.put(key, newNode);
                this.addNode(newNode);

                ++count;

                // The capacity of this cache has been reached,
                //  we have to purge out the tail element, i.e.
                //  the least active (the most stale) element.
                if (count > capacity) {
                    // pop the tail
                    DLinkedNode tail = this.popTail();
                    this.cache.remove(tail.key);
                    --count;
                }
            } else {
                // update the value.
                node.value = value;
                this.moveToHead(node);
            }
        }

        public static void main(String[] args) {
            LRUCache cache = new LRUCache(2);

            cache.set(1, 1);
            System.out.println(cache.get(1));

            cache.set(2, 2);

            // This would make the oldest element (i.e. 1) purged out.
            cache.set(3, 4);

            // return -1, since it should have been purged out.
            System.out.println(cache.get(1));
        }

}
