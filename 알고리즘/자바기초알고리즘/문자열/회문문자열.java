package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 회문문자열 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();

        String answer = reverseString(input);

        System.out.println(answer);
    }

    private static String reverseString(String input) {
        String toUpperCase = input.toUpperCase();
        char[] chars = toUpperCase.toCharArray();

        int lt = 0;
        int rt = chars.length - 1;

        while (lt < rt) {
            if (chars[lt] != chars[rt]) {
                return "NO";
            }

            lt++;
            rt--;
        }

        return "YES";
    }
}
