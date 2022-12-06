use std::fs;
use std::iter::FromIterator;
use std::collections::HashSet;


fn day06 (data: &str, n: usize) -> u16 {
    let message: Vec<char> = data.chars().collect();
    for (i, s) in message.windows(n as usize).enumerate() {
        let hs: HashSet<&char> = HashSet::from_iter(s);
        let unique_chars: Vec<_> = hs.into_iter().collect();
        if unique_chars.len() == n {
            return (i+n) as u16;
        }
    }
    return 3;
}


fn main() {
    let contents = fs::read_to_string("inputs/day06.txt")
        .expect("Should have been able to read the file");
    println!("Number of characters parsed (part a): {}", day06(&contents, 4));
    println!("Number of characters parsed (part b): {}", day06(&contents, 14));
}