package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 암호 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String input = br.readLine();
        StringBuilder result = new StringBuilder();
        int term = 7;

        for (int i = 0; i < N; i++) {
            char c = transPassword(input.substring(term * i, term * (i + 1)));
            result.append(c);
        }

        System.out.println(result.toString());
    }

    private static char transPassword(String substring) {
        char[] chars = substring.toCharArray();
        StringBuilder trans = new StringBuilder();

        for (char s : chars) {
            if (s == '#') {
                trans.append('1');
            } else {
                trans.append('0');
            }
        }
        int parseInt = Integer.parseInt(trans.toString(), 2);
        return (char) parseInt;
    }
}
