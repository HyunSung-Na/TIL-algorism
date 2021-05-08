package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class 피보나치 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> result = new ArrayList<>();

        int N = Integer.parseInt(br.readLine());
        result.add(1);
        result.add(1);
        result.add(2);

        for (int i = 2; i < N - 1; i++) {
            result.add(result.get(i) + result.get(i - 1));
        }

        result.forEach(it -> System.out.printf(it + " "));
    }
}
