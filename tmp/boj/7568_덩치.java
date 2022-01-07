package problem_21_1_7.덩치_7568;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int N;
    static List<Person> persons = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            persons.add(new Person(Integer.parseInt(s[0]), Integer.parseInt(s[1])));
        }

        for (int i = 0; i < N; i++) {
            int cnt = 1;
            for (int j = 0; j < N; j++) {
                if (i == j) continue;
                Person p1 = persons.get(i);
                Person p2 = persons.get(j);
                if (p1.weight < p2.weight && p1.height < p2.height)
                    cnt++;
            }
            bw.write(cnt + " ");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

class Person {
    int weight;
    int height;

    public Person(int weight, int height) {
        this.weight = weight;
        this.height = height;
    }
}
