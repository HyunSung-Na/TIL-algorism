package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class 동전교환 {

    static int minCoin = Integer.MAX_VALUE;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        int[] coin = Arrays.stream(br.readLine().split(" "))
                            .sorted(Comparator.reverseOrder())
                            .mapToInt(Integer::parseInt)
                            .toArray();

        M = Integer.parseInt(br.readLine());
        dfs(0, 0, coin);
        System.out.println(minCoin);
    }

    private static void dfs(int start, int sum, int[] coin) {
        if (sum > M) return;
        if (minCoin <= start) return;
        if (sum == M) {
            minCoin = Math.min(minCoin, start);
        } else {
            for (int i = 0; i < N; i++) {
                dfs(start + 1, sum + coin[i], coin);
            }
        }
    }
}
