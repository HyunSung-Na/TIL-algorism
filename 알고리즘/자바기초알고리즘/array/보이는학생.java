package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 보이는학생 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> result = new ArrayList<>();
        int N = Integer.parseInt(br.readLine());
        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int maxNum = 0;

        for (int i = 0; i < N; i++) {
            if (inputs[i] > maxNum) {
                maxNum = inputs[i];
                result.add(inputs[i]);
            }
        }

        System.out.println(result.size());
    }
}
