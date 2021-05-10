package com.baekjun.demo.인프런.sorting;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 삽입정렬 {

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

        for (int i = 1; i < n; i++) {
            int temp = array[i];
            int j;
            for (j = i - 1; j >= 0; j--) {
                if (array[j] > temp) {
                    array[j + 1] = array[j];
                } else {
                    break;
                }
            }
            array[j + 1] = temp;
        }

        return array;
    }
}
