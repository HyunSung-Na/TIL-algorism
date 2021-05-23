package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 팩토리얼 {

    static int dfs(int n) {
        if (n == 1) return 1;
        else {
            return n * dfs(n - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int dfs = dfs(Integer.parseInt(br.readLine()));
        System.out.println(dfs);
    }
}
