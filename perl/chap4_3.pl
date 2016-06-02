#!/bin/env perl

sub average{
    $sum = 0;
    foreach (@_){
        $sum += $_; 
    }
    return $sum/@_;
}

sub above_average{
    $ave = &average(@_);
    @above = ();
    foreach (@_){
        if ($_ > $ave){ push(@above,$_);} 
    }
    return @above
}

my @fred = &above_average(1..10);
print "\@fred is @fred\n";
print "(Should be 6 7 8 9 10)\n";
my @barney = &above_average(100,1..10);
print "\@narney is @barney\n";
print "(Should be just 100)\n";
