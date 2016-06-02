#!/bin/env perl

chomp(@index_list = <STDIN>);

@name_list = ("fred","betty","barney","dino","wilma","pebbles","bamm-bamm");
$total_index = $#name_list + 1;

foreach $index (@index_list) {
    if ($index <= $total_index && $index > 0){
        print ${name_list}[$index-1],"\n";
    }else{
        print "Invalid index number ",$index,"\n"; 
    }
}


