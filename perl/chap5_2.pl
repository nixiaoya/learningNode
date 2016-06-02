#!/bin/env perl

print (join("",(1..9)),join("",(0..9))x5,"\n");

chomp(@inputs=<STDIN>);

#foreach(@inputs){
#    printf "%20s",$_;
#}
printf "%20s\n" x @inputs,@inputs;
