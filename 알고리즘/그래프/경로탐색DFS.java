package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 경로탐색DFS {

    static int[][] graph;
    static int[] ch;
    static int answer = 0;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        graph = new int[N + 1][N + 1];
        ch = new int[N + 1];

        for (int i = 0; i < M; i++) {
            int a = Integer.parseInt(br.readLine());
            int b = Integer.parseInt(br.readLine());
            graph[a][b] = 1;
        }

        ch[1] = 1;
        dfs(1);
        System.out.println(answer);
    }

    private static void dfs(int v) {
        if (v == N) {
            answer++;
        } else {
            for (int i = 0; i <= N; i++) {
                if (graph[v][i] == 1 && ch[i] == 0) {
                    ch[i] = 1;
                    dfs(i);
                    ch[i] = 0;
                }
            }
        }
    }
}
