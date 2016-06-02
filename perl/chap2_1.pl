#!/bin/env perl

$PI = 3.14;

chomp($r = <STDIN>);

if ($r){

    if ($r < 0){
        $area = 0;
        $perimeter = 0;
    }else{
        $area = $PI*$r**2;
        $perimeter = 2*$PI*$r;
    }
    print "Area is $area\n"; 
    print "Perimeter is $perimeter\n";

}else {
    print "input error !";
}


