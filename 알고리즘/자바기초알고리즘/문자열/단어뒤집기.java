package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 단어뒤집기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder builder = new StringBuilder();
        int input = Integer.parseInt(br.readLine());

        for (int i = 0; i < input; i++) {
            String userInput = br.readLine();
            StringBuilder reverse = builder.append(userInput).reverse();

            System.out.println(reverse);

            reverse.delete(0, reverse.length());
        }

    }
}
