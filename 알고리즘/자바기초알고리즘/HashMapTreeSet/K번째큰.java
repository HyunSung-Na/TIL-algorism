package com.baekjun.demo.인프런.HashMapTreeSet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class K번째큰 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] array = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int answer = solution(inputs, array);

        System.out.println(answer);
    }

    private static int solution(int[] inputs, int[] array) {
        int answer = -1;

        int N = inputs[0];
        int K = inputs[1];

        TreeSet<Integer> set = new TreeSet<>(Comparator.reverseOrder());

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int l = j + 1; l < N; l++) {
                    set.add(array[i] + array[j] + array[l]);
                }
            }
        }

        int cnt = 0;

        for (int x : set) {
            cnt++;
            if (cnt == K) return x;
        }

        return answer;
    }
}
