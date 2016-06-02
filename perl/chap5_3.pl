#!/bin/env perl

sub showRefence{
    my ($length) = @_;
    if ( $length > 9){
        $add = ($length-9)/10+1;
    }else{
        $add = 1;
    }

    print (join("",0..9)  x $add,"\n");
}

chomp(@inputs=<STDIN>);

my $len = shift @inputs;
my $format = "%${len}s\n" x @inputs;
&showRefence($len);
printf $format,@inputs;
