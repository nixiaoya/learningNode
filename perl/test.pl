#!/bin/env perl

@rocks = qw/bedrock slate lava /;

foreach $rock (@rocks){
    $rock = "\t$rock";
    $rock .= "\n";
}

print "The rocks are:\n",@rocks
