package com.baekjun.demo.인프런.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 친구인가 {

    static int[] board;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        N = inputs[0];
        M = inputs[1];

        board = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            board[i] = i;
        }

        for (int i = 0; i < M; i++) {
            int[] relation = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            union(relation[0], relation[1]);
        }

        int[] answer = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int fa = find(answer[0]);
        int fb = find(answer[1]);

        if (fa != fb) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }

    private static void union(int a, int b) {
        int fa = find(a);
        int fb = find(b);

        if (fa != fb) board[fa] = fb;
    }

    private static int find(int v) {
        if (v == board[v]) return v;
        else {
            return board[v] = find(board[v]);
        }
    }
}
