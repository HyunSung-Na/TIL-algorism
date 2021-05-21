package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 순열구하기 {

    static int[] pm;
    static int[] ch;
    static int[] arr;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        N = inputs[0];
        M = inputs[1];

        arr = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();

        ch = new int[N];
        pm = new int[M];
        dfs(0);
    }

    private static void dfs(int index) {
        if (index == M) {
            for (int x : pm) {
                System.out.print(x + " ");
            }
            System.out.println();
        } else {
            for (int i = 0; i < N; i++) {
                if (ch[i] == 0) {
                    pm[index] = arr[i];
                    ch[i] = 1;
                    dfs(index + 1);
                    ch[i] = 0;
                }
            }
        }
    }
}
