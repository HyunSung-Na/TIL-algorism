package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 유효한팰린드롬 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();

        System.out.println(solution(input));
    }

    private static String solution(String input) {
        String answer = "NO";
        String toUpperCase = input.toUpperCase().replaceAll("[^A-Z]", "");
        StringBuilder builder = new StringBuilder(toUpperCase).reverse();

        if (toUpperCase.equals(builder.toString())) {
            return "YES";
        }

        return answer;
    }
}
