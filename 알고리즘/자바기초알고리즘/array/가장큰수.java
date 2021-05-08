package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 가장큰수 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> result = new ArrayList<>();
        int N = Integer.parseInt(br.readLine());

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        result.add(inputs[0]);

        for (int i = 1; i < N; i++) {
            if (inputs[i - 1] < inputs[i]) {
                result.add(inputs[i]);
            }
        }

        result.forEach(it -> System.out.print(it + " "));
    }
}
