package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 대소문자변환 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        StringBuffer answer = new StringBuffer();

        for (char c : input.toCharArray()) {
            if (c == Character.toLowerCase(c)) {
                answer.append(Character.toUpperCase(c));
            } else if (c == Character.toUpperCase(c)) {
                answer.append(Character.toLowerCase(c));
            }
        }

        System.out.println(answer);
    }
}
