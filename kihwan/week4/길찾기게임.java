import java.util.Arrays;
import java.util.Comparator;

public class 길찾기게임 {

    int[][] result;
    int idx;

    public int[][] solution(int[][] nodeinfo) {
        Node[] node = new Node[nodeinfo.length];
        for(int i = 0; i < nodeinfo.length; i++) {
            node[i] = new Node(nodeinfo[i][0], nodeinfo[i][1], i + 1, null, null);
        }
        Arrays.sort(node, (n1, n2) -> {
            if(n1.y == n2.y) return n1.x - n2.x;
            else return n2.y - n1.y;
        });
        Node root = node[0];
        for(int i = 1; i < node.length; i++) {
            insertNode(root, node[i]);
        }
        result = new int[2][nodeinfo.length];
        idx = 0;
        preOrder(root);
        idx = 0;
        postOrder(root);
        return result;
    }

    public void insertNode(Node parent, Node child) {
        if(parent.x > child.x) {
            if(parent.left == null) parent.left = child;
            else insertNode(parent.left, child);
        } else {
            if(parent.right == null) parent.right = child;
            else insertNode(parent.right, child);
        }
    }

    public void preOrder(Node root) {
        if(root != null) {
            result[0][idx++] = root.value;
            preOrder(root.left);
            preOrder(root.right);
        }
    }

    public void postOrder(Node root) {
        if(root != null) {
            postOrder(root.left);
            postOrder(root.right);
            result[1][idx++] = root.value;
        }
    }
    class Node {
        int x;
        int y;
        int value;
        Node left, right;
        public Node(int x, int y, int value, Node left, Node right) {
            this.x = x;
            this.y = y;
            this.value = value;
            this.left = left;
            this.right = right;
        }
    }

}
