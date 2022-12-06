use std::fs;
use std::collections::HashSet;
use std::iter::FromIterator;


fn get_priority(c: &char) -> u32 {
    let v: u32 = *c as u32;
    return if v > 90 {
        v - 96
    } else {
        v - 38
    }
}

fn day03_a(data: &str) -> u32 {
    let mut priority_sum: u32 = 0;

    for rucksack in data.split("\n") {
        let (comp1, comp2): (&str, &str) = rucksack.split_at(rucksack.len() / 2);
        let (comp1set, comp2set): (HashSet<char>, HashSet<char>) = (HashSet::from_iter(comp1.chars()), HashSet::from_iter(comp2.chars()));
        let intersection: Vec<_> = comp1set.intersection(&comp2set).collect();
        priority_sum += get_priority(intersection[0]);
    }

    return priority_sum;

}


fn day03_b(data: &str) -> u32 {
    let mut priority_sum: u32 = 0;
    let rucksacks: Vec<_> = data.split("\n").collect();
    for i in (0..(rucksacks.len()- 3)).step_by(3) {
        let (comp1, comp2, comp3): (&str, &str, &str) = (rucksacks[i], rucksacks[i+1], rucksacks[i+2]);
        let (comp1set, comp2set, comp3set): (HashSet<char>, HashSet<char>,  HashSet<char>) =
            (HashSet::from_iter(comp1.chars()), HashSet::from_iter(comp2.chars()), HashSet::from_iter(comp3.chars()));
        let sets = [comp1set, comp2set, comp3set];
        let intersection = sets
        .iter()
        .skip(1)
        .fold(sets[0].clone(), |acc, hs| {
            acc.intersection(hs).cloned().collect()
        });
        priority_sum += get_priority(&intersection.iter().next().unwrap().clone());

    }
    return priority_sum;
}


fn main() {
    let contents = fs::read_to_string("inputs/day03.txt")
        .expect("Should have been able to read the file");
    let priorities_a = day03_a(&contents);
    println!("Sum of priorities (part a): {}", priorities_a);
    let priorities_b = day03_b(&contents);
    println!("Sum of priorities (part b): {}", priorities_b);
}