import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine().trim());
        
        Map<String, Long> recipe = new HashMap<>();
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            long x = Long.parseLong(st.nextToken());
            recipe.put(s, recipe.getOrDefault(s, 0L) + x);
        }

        List<Long> amounts = new ArrayList<>(recipe.values());
        boolean isGold = false;

        for (int i = 0; i < amounts.size(); i++) {
            for (int j = 0; j < amounts.size(); j++) {
                if (i == j) continue;

                long ai = amounts.get(i);
                long aj = amounts.get(j);

                if (Math.floor(ai * 1.618) == aj) {
                    isGold = true;
                    break;
                }
            }
            if (isGold) break;
        }

        System.out.println(isGold ? "Delicious!" : "Not Delicious...");
    }
}