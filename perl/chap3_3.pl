#!/bin/env perl

chomp(@index_list = <STDIN>);

@_sorted = sort @index_list;

print join("\t",@_sorted),"\n";
