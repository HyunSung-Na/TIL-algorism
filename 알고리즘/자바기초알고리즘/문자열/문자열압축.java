package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 문자열압축 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();

        String answer = solution(input);

        System.out.println(answer);
    }

    private static String solution(String input) {
        char[] chars = input.toCharArray();
        StringBuilder builder = new StringBuilder();
        int r = 1;

        for (int i = 1; i < chars.length; i++) {
            if (chars[i] == chars[i - 1]) {
                r++;
            } else {
                if (r > 1) {
                    builder.append(chars[i - 1]);
                    builder.append(r);
                } else {
                    builder.append(chars[i - 1]);
                }
                r = 1;
            }
        }

        if (r > 1) {
            builder.append(chars[chars.length - 1]);
            builder.append(r);
        } else {
            builder.append(chars[chars.length - 1]);
        }

        return builder.toString();
    }
}
