#!/bin/env perl

sub total{
    my $total = shift @_;
    foreach (@_){
        $total += $_;
    }
    return $total
}

my @fred = (1..100);
my $fred_total = &total(@fred);
print "The total of \@fred is $fred_total.\n";
