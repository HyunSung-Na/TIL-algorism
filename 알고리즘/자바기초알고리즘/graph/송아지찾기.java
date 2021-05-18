package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 송아지찾기 {

    static int[] dis = {1, -1, 5};
    static int[] ch;
    static Queue<Integer> queue = new LinkedList<>();

    static int bfs(int n, int m) {
        ch = new int[10001];
        ch[n] = 1;
        queue.offer(n);
        int L = 0;

        while (!queue.isEmpty()) {
            int len = queue.size();

            for (int i = 0; i < len; i++) {
                int x = queue.poll();

                if (x == m) return L;

                for (int j = 0; j < 3; j++) {
                    int nx = x + dis[j];

                    if (nx >= 1 && nx <= 10000 && ch[nx] == 0) {
                        ch[nx] = 1;
                        queue.offer(nx);
                    }
                }
            }

            L++;
        }

        return L;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        System.out.println(bfs(inputs[0], inputs[1]));
    }
}
