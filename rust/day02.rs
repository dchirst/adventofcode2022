use std::fs;

fn day01_a(data: &str) -> i32 {
    for round in data.split("\n") {
        let chars = round.as_bytes();
        let (opp, you): (char, char) = (chars[0] as char, chars[2] as char);
        println!("{}", opp)
    }
    return 3
}


fn main() {
    let contents = fs::read_to_string("inputs/day1.txt")
        .expect("Should have been able to read the file");

    let score_a: i32 = day01_a(&contents);
    println!("Score for Day 2 (part a): {}", score_a)
}