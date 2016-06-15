#!/bin/env perl

%hash = ( 
    "fred" => "flinstone",
    "barney" => "rubble",
    "wilma" => "flinstone",
    ); 

while (<STDIN>){
    chomp;
    if (exists $hash{$_}){
        print "Value is: $hash{$_}","\n";
    } else {
        print "none key matched.","\n"; 
    }
}
