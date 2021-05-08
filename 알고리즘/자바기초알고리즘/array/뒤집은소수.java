package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 뒤집은소수 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Arrays.stream(br.readLine().split(" "))
                .map(StringBuilder::new)
                .map(StringBuilder::reverse)
                .mapToInt(it -> Integer.parseInt(it.toString()))
                .filter(it -> isPrime(it))
                .forEach(it -> System.out.print(it + " "));

    }

    public static boolean isPrime(int num) {

        if (num == 1) {
            return false;
        }

        for(int i = 2; i < num; i++) {
            if( num%i == 0) {
                return false;
            }
        }

        return true;
    }
}
