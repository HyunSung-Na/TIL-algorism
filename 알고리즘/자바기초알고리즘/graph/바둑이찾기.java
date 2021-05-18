package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 바둑이찾기 {

    static int W;
    static int N;
    static ArrayList<Integer> arrayList = new ArrayList<>();
    static int maxNum = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        N = inputs[1];
        W = inputs[0];

        for (int i = 0; i < N; i++) {
            arrayList.add(Integer.parseInt(br.readLine()));
        }

        dfs(0, 0);
        System.out.println(maxNum);
    }

    private static void dfs(int start, int sum) {
        if (sum > W) return;
        if (start == N) {
            maxNum = Math.max(maxNum, sum);
        } else {
            dfs(start + 1, sum + arrayList.get(start));
            dfs(start + 1, sum);
        }

    }
}
