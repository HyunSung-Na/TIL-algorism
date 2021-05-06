package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 특정문자뒤집기 {

    static String reverse(String input) {
        char[] chars = input.toCharArray();
        int rt = chars.length - 1;
        int lt = 0;

        while (lt < rt) {
            if (!Character.isAlphabetic(chars[lt])) {
                lt++;
            } else if (!Character.isAlphabetic(chars[rt])) {
                rt--;
            } else {
                char tmp = chars[rt];
                chars[rt] = chars[lt];
                chars[lt] = tmp;

                lt++;
                rt--;
            }
        }

        return String.valueOf(chars);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();

        System.out.println(reverse(input));
    }
}
