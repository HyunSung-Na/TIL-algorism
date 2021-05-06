package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 가장짧은문자거리 {

    static int[] answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");

        answer = new int[inputs[0].length()];

        solution(inputs[0], inputs[1]);

        Arrays.stream(answer).forEach(i -> System.out.print(i + " "));
    }

    private static void solution(String input, String compare) {
        char[] chars = input.toCharArray();
        char c = compare.charAt(0);
        int p = 1000;

        for (int i = 0; i < input.length(); i++) {
            if (chars[i] == c) {
                p = 0;
                answer[i] = p;
            } else {
                p++;
                answer[i] = p;
            }
        }

        p = 1000;

        for (int j = input.length() - 1; j >= 0; j--) {
            if (chars[j] == c) {
                p = 0;
            } else {
                p++;
                answer[j] = Math.min(answer[j], p);
            }
        }
    }
}
