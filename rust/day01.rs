use std::fs;
use std::time::{Instant};
use itertools::Itertools;



fn day1_a_copied(data: &str) -> u64 {
    let totals: Vec<u64> = include_str!("../inputs/day1.txt")
        .split("\n\n")
        .map(|elf| {
            elf.split("\n")
                .map(|food| food.parse::<u64>().unwrap_or(0)).sum()
    })
        .sorted().rev().collect();

    return totals[0]
}


fn day1_a(data: &str) -> i32 {
    let mut max_cal: i32 = 0;
    let mut current_cal: i32 = 0;
    for cal in data.split("\n") {
        if cal.parse::<f64>().is_ok() {
            current_cal = cal.parse::<i32>().unwrap() + current_cal;
        } else {
            if current_cal > max_cal {
                max_cal = current_cal;
            }
            current_cal = 0;
        }
    }
    return max_cal;
}

fn day1_b(data: &str) -> i32 {
    let mut top_3_cals: [i32; 3] = [0; 3];
    let mut current_cal: i32 = 0;
    for cal in data.split("\n") {
        if cal.parse::<f64>().is_ok() {
            current_cal = cal.parse::<i32>().unwrap() + current_cal;
        } else {
            if current_cal > top_3_cals[0] {
                top_3_cals[0] = current_cal;
                top_3_cals.sort();
            }
            current_cal = 0;
        }
    }
    return top_3_cals.iter().sum();
}

fn main() {

    extern crate itertools;
    let contents = fs::read_to_string("inputs/day1.txt")
        .expect("Should have been able to read the file");
    for _ in 0..5 {
        let start = Instant::now();
        let max_cal_a: i32 = day1_a(&contents);
        let duration = start.elapsed();
        println!("Maximum calories (part a): {}", max_cal_a);

        println!("Time elapsed in day1_a() is: {:?}", duration);
    }

    for _ in 0..5 {
        let start = Instant::now();
        let max_cal_a: i32 = day1_a(&contents);
        let duration = start.elapsed();
        println!("Maximum calories (part a copied solution): {}", max_cal_a);

        println!("Time elapsed in day1_a_copied() is: {:?}", duration);
    }

    let max_cal_b: i32 = day1_b(&contents);
    println!("Maximum calories (part b): {}", max_cal_b);
}