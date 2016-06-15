#!/bin/env perl

%hash = (); 

while (<>){
    chomp;
    if (!exists $hash{$_}){
        $hash{$_} = 1;
    } else {
        $hash{$_} += 1; 
    }
}

#while (($key,$value) = each %hash){
#    print "$key , counts: $value\n";
#}

@keys = sort (keys %hash);

foreach $key (@keys){
    print "$key,counts:$hash{$key}\n";
}
