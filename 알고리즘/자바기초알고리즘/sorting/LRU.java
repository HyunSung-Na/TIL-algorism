package com.baekjun.demo.인프런.sorting;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class LRU {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] task = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] result = solution(input, task);

        Arrays.stream(result).forEach(it -> System.out.print(it + " "));
    }

    private static int[] solution(int[] input, int[] task) {
        int[] cache = new int[input[0]];

        for (int x : task) {
            int pos = -1;
            for (int i = 0; i < input[0]; i++) {
                if (x == cache[i])
                    pos = i;
            }

            if (pos == -1) {
                for (int i = input[0] - 1; i >= 1; i--) {
                    cache[i] = cache[i - 1];
                }
                cache[0] = x;
            } else {
                for (int i = pos; i >= 1; i--) {
                    cache[i] = cache[i - 1];
                }
                cache[0] = x;
            }
        }

        return cache;
    }
}
