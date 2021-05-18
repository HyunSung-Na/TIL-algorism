package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class 경로탐색인접리스 {
    static ArrayList<ArrayList<Integer>> graph;
    static int[] ch;
    static int answer = 0;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        graph = new ArrayList<ArrayList<Integer>>();
        ch = new int[N + 1];

        for (int p = 0; p <= N; p++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < M; i++) {
            int a = Integer.parseInt(br.readLine());
            int b = Integer.parseInt(br.readLine());
            graph.get(a).add(b);
        }

        ch[1] = 1;
        dfs(1);
        System.out.println(answer);
    }

    private static void dfs(int v) {
        if (v == N) {
            answer++;
        } else {
            for (int nv : graph.get(v)) {
                if (ch[nv] == 0) {
                    ch[nv] = 1;
                    dfs(nv);
                    ch[nv] = 0;
                }
            }
        }
    }
}
