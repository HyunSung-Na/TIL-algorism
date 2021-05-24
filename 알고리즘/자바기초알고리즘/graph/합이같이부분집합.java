package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 합이같이부분집합 {

    static String answer = "NO";
    static int n, total = 0;
    static boolean flag = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        total = Arrays.stream(inputs).sum();

        dfs(0, 0, inputs);

        System.out.println(answer);
    }

    private static void dfs(int L, int sum, int[] inputs) {
        if (flag) return;
        if (sum > total / 2) return;
        if (L == n) {
            if ((total - sum) == sum) {
                answer = "YES";
                flag = true;
            }
        } else {
            dfs(L + 1, sum + inputs[L], inputs);
            dfs(L + 1, sum, inputs);
        }
    }


}
