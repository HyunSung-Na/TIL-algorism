package com.baekjun.demo.재귀;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class baekjun암호만들기 {

    static void go(int N, String[] alpha, String password, int i) {
        if (password.length() == N) {
            if (check(password))
                System.out.println(password);
            return;
        }

        if (i >= alpha.length)
            return;

        go(N, alpha, password + alpha[i], i + 1);
        go(N, alpha, password, i + 1);
    }

    private static boolean check(String password) {
        int ja = 0;
        int mo = 0;

        for (char x : password.toCharArray()) {
            if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u')
                mo += 1;
            else {
                ja += 1;
            }
        }

        return ja >= 2 && mo >= 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> numbers = Arrays.stream(br.readLine().split(" ")).
                map(Integer::new).collect(Collectors.toList());
        String[] alpha = br.readLine().split(" ");

        Arrays.sort(alpha);

        int N = numbers.get(0);

        go(N, alpha, "", 0);
    }
}
