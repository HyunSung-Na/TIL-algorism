package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 가위바위보 {

    static ArrayList<String> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] person1 = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] person2 = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int i = 0; i < N; i++) {
            if (person1[i] == person2[i]) {
                result.add("D");
            } else if (checkWin(person1[i], person2[i])) {
                result.add("A");
            } else {
                result.add("B");
            }
        }

        result.forEach(System.out::println);
    }

    private static boolean checkWin(int i, int i1) {
        if (i == 3 && i1 == 1) {
            return false;
        }

        if (i > i1) {
            return true;
        } else if (i == 1 && i1 == 3) {
            return true;
        }

        return false;
    }
}
