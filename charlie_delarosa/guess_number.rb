def guess_number guess
    number = 25
    puts "Your guess is too high" if guess > number
    puts "Your guess is too low" if guess < number
    puts "Your guess is right on!" if guess == number
end

puts "Guess a number: "
guess = gets.to_i
guess_number guess
