public class 가사검색 {

    class Solution {
        private static final int MAX_LEN = 10001;
        private Trie[] prefix = new Trie[MAX_LEN]; // ? 앞에 붙는 놈 (접두어) 찾기 전용
        private Trie[] suffix = new Trie[MAX_LEN]; // ? 뒤에 붙느 놈 (접미어) 찾기 전용

        private String reverse(String str){
            return (new StringBuilder(str)).reverse().toString();
        }

        public int[] solution(String[] words, String[] queries) {
            for(String word : words){
                int len = word.length();
                if(prefix[len] == null) prefix[len] = new Trie();
                if(suffix[len] == null) suffix[len] = new Trie();
                prefix[len].insert(reverse(word));
                suffix[len].insert(word);
            }
            int[] answer = new int[queries.length];
            for(int i = 0; i < answer.length; i++){
                int len = queries[i].length();
                if(queries[i].charAt(0) == '?'){
                    if(prefix[len] == null) answer[i] = 0;
                    else answer[i] = prefix[len].find(reverse(queries[i]));
                }else{
                    if(suffix[len] == null) answer[i] = 0;
                    else answer[i] = suffix[len].find(queries[i]);
                }
            }
            return answer;
        }

        private class Trie {
            private Trie[] children = new Trie[26];
            private int cnt = 0;
            public void insert(String word){
                Trie cur = this;
                for(char c : word.toCharArray()){
                    cur.cnt++;
                    int index = c - 'a';
                    if(cur.children[index] == null) {
                        cur.children[index] = new Trie();
                    }
                    cur = cur.children[index];
                }
                cur.cnt++;
            }
            public int find(String word){
                Trie cur = this;
                for(char c : word.toCharArray()){
                    if(c == '?') {
                        return cur.cnt;
                    }
                    int index = c - 'a';
                    if(cur.children[index] == null) {
                        return 0;
                    }
                    cur = cur.children[index];
                }
                return cur.cnt;
            }
        }
    }
}
