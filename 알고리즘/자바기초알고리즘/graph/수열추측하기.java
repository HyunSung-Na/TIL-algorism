package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 수열추측하기 {

    static int N, f;
    static int[] p, b;
    static int[] check;
    static boolean flag = false;
    static int[][] dy = new int[35][35];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        N = inputs[0];
        f = inputs[1];
        b = new int[N];
        p = new int[N];
        check = new int[N + 1];

        for (int i = 0; i < N; i++) {
            b[i] = combi(N - 1, i);
        }

        dfs(0, 0);
    }

    private static int combi(int n, int r) {
        if (dy[n][r] > 0) return dy[n][r];
        if (n == r || r == 0) return 1;
        else {
            return dy[n][r] = combi(n - 1, r - 1) + combi(n - 1, r);
        }
    }

    private static void dfs(int index, int sum) {
        if (flag) return;
        if (index == N) {
            if (sum == f) {
                for (int x : p) {
                    System.out.print(x + " ");
                }
                flag = true;
            }
        } else {
            for (int i = 1; i <= N; i++) {
                if (check[i] == 0) {
                    check[i] = 1;
                    p[index] = i;
                    dfs(index + 1, sum + (p[index] * b[index]));
                    check[i] = 0;
                }
            }
        }
    }
}
