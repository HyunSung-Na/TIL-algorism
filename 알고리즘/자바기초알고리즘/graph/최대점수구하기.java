package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 최대점수구하기 {

    static ArrayList<Integer> score = new ArrayList<>();
    static ArrayList<Integer> timeArray = new ArrayList<>();
    static int N;
    static int time;
    static int maxScore = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        N = inputs[0];
        time = inputs[1];

        for (int i = 0; i < N; i++) {
            int[] sample = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            score.add(sample[0]);
            timeArray.add(sample[1]);
        }

        dfs(0, 0, time);
        System.out.println(maxScore);
    }

    private static void dfs(int start, int sum, int time) {
        if (time < 0) return;
        if (start == N) {
            maxScore = Math.max(maxScore, sum);
        } else {
            dfs(start + 1, sum + score.get(start), time - timeArray.get(start));
            dfs(start + 1, sum, time);
        }
    }
}
