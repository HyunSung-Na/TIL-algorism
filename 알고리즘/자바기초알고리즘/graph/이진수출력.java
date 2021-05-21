package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 이진수출력 {

    static void dfs(int n) {
        if (n == 0) {
            return;
        } else {
            System.out.print(n % 2 + " ");
            dfs(n / 2);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int input = Integer.parseInt(br.readLine());

        dfs(input);
    }
}
