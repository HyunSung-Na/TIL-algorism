package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class 등수구하기 {

    static ArrayList<Integer> rank = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int num : input) {
            rank.add(num);
        }

        rank.sort(Comparator.reverseOrder());

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (rank.get(j) == input[i]) {
                    input[i] = j + 1;
                    break;
                }
            }
        }

        Arrays.stream(input)
                .forEach(it -> System.out.print(it + " "));
    }
}
