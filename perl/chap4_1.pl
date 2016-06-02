#!/bin/env perl

sub total{
    my $total = shift @_;
    foreach (@_){
        $total += $_;
    }
    return $total
}

my @fred = qw{1 3 5 7 9};
my $fred_total = &total(@fred);
print "The total of \@fred is $fred_total.\n";
print "Enter some bumbers on seperate lines:";
my $user_total = &total(<STDIN>);
print "The total of those bumbers is $user_total.\n"
