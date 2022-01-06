package problem_21_1_6.개미_3048;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<Ant> ants = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        String a = br.readLine();
        for (int i = N - 1; i > -1; i--) {
            ants.add(new Ant(a.charAt(i), 0));
        }
        String b = br.readLine();
        for (int i = 0; i < M; i++) {
            ants.add(new Ant(b.charAt(i), 1));
        }
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            for (int i = 0; i < ants.size() - 1; i++) {
                Ant antA = ants.get(i);
                Ant antB = ants.get(i + 1);
                if (antA.team == 1 || antA.team == antB.team)
                    continue;
                ants.set(i, antB);
                ants.set(i + 1, antA);
                i++;
            }
        }
        ants.forEach(x -> System.out.print(x.name));
    }
}

class Ant {
    char name;
    int team;

    public Ant(char name, int team) {
        this.name = name;
        this.team = team;
    }
}
