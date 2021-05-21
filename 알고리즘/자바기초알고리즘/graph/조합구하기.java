package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 조합구하기 {

    static int[][] dy = new int[35][35];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ints = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int answer = dfs(ints[0], ints[1]);
        System.out.println(answer);
    }

    private static int dfs(int n, int m) {
        if (n == m || m == 0) return 1;
        if (dy[n][m] > 0) return dy[n][m];
        else {
            return dy[n][m] = dfs(n - 1, m - 1) + dfs(n - 1, m);
        }
    }
}
