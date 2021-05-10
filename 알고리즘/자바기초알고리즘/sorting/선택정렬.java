package com.baekjun.demo.인프런.sorting;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 선택정렬 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] array = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] result = solution(N, array);

        Arrays.stream(result).forEach(it -> System.out.print(it + " "));
    }

    private static int[] solution(int n, int[] array) {

        for (int i = 0; i < n - 1; i++) {
            int idx = i;
            for (int j = i + 1; j < n; j++) {
                if (array[j] < array[idx]) {
                    idx = j;
                }
            }

            int temp = array[i];
            array[i] = array[idx];
            array[idx] = temp;
        }

        return array;
    }
}
